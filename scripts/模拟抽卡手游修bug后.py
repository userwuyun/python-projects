import random


# ================= 玩家类（负责资源管理、记录账本） =================
class Player:
    def __init__(self, name):
        self.name = name
        self.primogems = 32000  # 初始原石
        self.fates = 10  # 初始抽卡券
        self.pity_counter = 0  # 保底计数（移到玩家这里了！）
        self.guaranteed_up = False  # 大保底状态（移到玩家这里了！）
        self.pull_history = []  # 抽卡历史记录

    def consume(self, pulls):
        """扣除抽卡资源：优先扣券，不够再扣原石"""
        if self.fates >= pulls:
            self.fates -= pulls
            return
        needed_primogems = (pulls - self.fates) * 160
        if self.primogems >= needed_primogems:
            self.primogems -= needed_primogems
            self.fates = 0
        else:
            raise ValueError(f"资源不足！需要 {pulls} 抽，当前资源不够。")

    def add_record(self, rarity, name):
        """记录抽卡结果，并更新保底计数器"""
        self.pull_history.append({"rarity": rarity, "name": name})
        self.pity_counter += 1
        if rarity == "六星":
            self.pity_counter = 0  # 抽到六星，保底重置

    def show_status(self):
        """打印玩家当前资源状态"""
        total_pulls = self.primogems // 160 + self.fates
        pity_threshold = 70
        pity_left = max(0, pity_threshold - self.pity_counter)

        print("\n" + "=" * 30)
        print(f"👤 玩家昵称：{self.name}")
        print("-" * 30)
        print(f"💎 原石余额：{self.primogems}  (可兑换 {self.primogems // 160} 抽)")
        print(f"🎫 抽卡券：  {self.fates} 张")
        print(f"🎯 总计可抽：{total_pulls} 次")
        print("-" * 30)
        print(f"⏳ 保底进度：已垫 {self.pity_counter} 抽，距离保底还剩 {pity_left} 抽")
        if self.guaranteed_up:
            print("✨ 大保底状态：已触发 (下一个六星必定是 UP 角色！)")
        else:
            print("✨ 大保底状态：未触发 (下一个六星有 50% 概率歪)")
        print("=" * 30 + "\n")

    def show_history(self):
        """打印抽卡历史"""
        if not self.pull_history:
            print("📝 暂无抽卡记录")
            return
        print("\n" + "=" * 30)
        print("📜 历史抽卡记录：")
        for i, record in enumerate(self.pull_history, 1):
            print(f"  第 {i} 抽：【{record['rarity']}】{record['name']}")
        print("=" * 30 + "\n")

    def show_lucky(self):
        """
        展示玩家的出卡情况
        """
        if not self.pull_history:
            print("📭 暂无抽卡记录")
            return

        print("\n" + "=" * 30)
        print("🍀 出货记录统计")

        ssr = 0
        total = 0  # ⚠️ 避坑：不要把变量命名为 all，它是 Python 内置函数

        # 遍历历史记录，record 是字典
        for record in self.pull_history:
            total += 1
            if record["rarity"] == "六星":  # 通过字典的键取值
                ssr += 1

        # 计算概率（防除零错误）
        if total > 0:
            ssr_rate = (ssr / total) * 100
            print(f"一共抽出 {ssr} 个六星")
            print(f"六星概率为: {ssr_rate:.2f}%")
        else:
            print("暂无数据")

        print("=" * 30 + "\n")


# ================= 抽卡系统类（负责概率、保底逻辑） =================
class GachaSystem:
    def __init__(self):
        self.SSR_PITY = 70
        self.CARD_POOL = {
            "六星": ["终焉星龙·奥菲斯", "永夜女王·瑟琳", "创世齿轮·阿卡夏"],
            "五星": ["苍穹执旗者·罗兰", "焚天红莲·朱璃", "深海歌姬·汐音", "星陨剑圣·格兰"],
            "四星": ["银月游侠·塞拉", "赤鸢剑客·红叶", "幽蓝调律师·诺特", "岩心守卫·托尔"],
            "三星": ["霜刃剑客·凛", "火铳游侠·杰特", "林语德鲁伊·芙萝"],
            "二星": ["见习星术士·米娅", "巡夜弩手·洛恩", "药剂学徒·可可"],
            "一星": ["微光尘灵", "锈铁机偶", "纸鸢小妖"]
        }
        self.BASE_RATES = {
            "六星": 0.015, "五星": 0.085, "四星": 0.3,
            "三星": 0.45, "二星": 0.1, "一星": 0.05
        }

    def get_rarity(self, player):
        """决定抽出的稀有度（保底逻辑在这里）"""
        # 1. 判断是否触发大保底（70抽）
        if player.pity_counter + 1 >= self.SSR_PITY:
            return "六星"

        # 2. 正常概率抽取
        rand = random.random()
        cumulative = 0
        for rarity, rate in self.BASE_RATES.items():
            cumulative += rate
            if cumulative >= rand:
                return rarity
        return "一星"

    def _pick_card(self, player, rarity):
        """决定具体抽到哪个角色（处理大保底歪不歪）"""
        if rarity == "六星":
            if player.guaranteed_up:  # 大保底
                player.guaranteed_up = False  # 用掉大保底
                return "终焉星龙·奥菲斯"

            if random.random() < 0.5:  # 小保底没歪
                return "终焉星龙·奥菲斯"
            else:  # 小保底歪了
                player.guaranteed_up = True  # 触发大保底，下次必中
                return random.choice(self.CARD_POOL["六星"])
        else:
            return random.choice(self.CARD_POOL[rarity])

    def draw_one(self, player):
        """单抽逻辑"""
        player.consume(1)  # 扣费
        rarity = self.get_rarity(player)
        card_name = self._pick_card(player, rarity)
        player.add_record(rarity, card_name)  # 玩家记账
        return rarity, card_name

    def draw_ten(self, player):
        """十连抽逻辑"""
        results = []
        has_sr_or_above = False

        for _ in range(10):
            rarity, card_name = self.draw_one(player)
            results.append((rarity, card_name))
            # 【修复点】判断中文稀有度
            if rarity in ["六星", "五星", "四星"]:
                has_sr_or_above = True

        # 十连保底：如果十连全是三星及以下，把最后一个强行换成四星
        if not has_sr_or_above:
            results[-1] = ("四星", random.choice(self.CARD_POOL["四星"]))
            # 注意：这里只是修改了返回值，如果要严格记录到玩家历史里，需要额外处理
        return results


# ================= 主程序 =================
if __name__ == "__main__":
    player = Player("旅行者")
    gacha = GachaSystem()

    while True:
        print("\n" + "=" * 15 + " 抽卡系统 " + "=" * 15)
        print("1. 查询资源")
        print("2. 查询记录")
        print("3. 十连")
        print("4. 单抽")
        print("5. 退出")
        print("6. 出货情况")
        print("=" * 40)

        try:
            i = int(input("请输入需要的操作 (1~6): "))
        except ValueError:
            print("❌ 请输入数字 1~6")
            continue

        if i < 1 or i > 6:
            print("❌ 请输入 1~6")
            continue

        elif i == 1:
            player.show_status()

        elif i == 2:
            player.show_history()

        elif i == 3:
            try:
                results = gacha.draw_ten(player)
                print(f"\n🎉 十连完成！本次抽取结果：")
                for rarity, name in results:
                    print(f"   【{rarity}】{name}")
            except ValueError as e:
                print(f"❌ 抽卡失败：{e}")

        elif i == 4:
            try:
                rarity, name = gacha.draw_one(player)
                print(f"\n🎉 单抽完成！获得了【{rarity}】{name}")
            except ValueError as e:
                print(f"❌ 抽卡失败：{e}")

        elif i == 6:
            player.show_lucky()

        elif i == 5:
            print("👋 欢迎下次再来！")
            break
