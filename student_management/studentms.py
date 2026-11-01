from student import Student

class StudentMS:
    def __init__(self,file_path = "stu.txt"):
        self.file_path = file_path
        self.stu_dict = {}
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                all_stu_line = f.readlines()
                for line in all_stu_line:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        stu = Student.generate(line)
                        self.stu_dict[stu.name] = stu
                    except ValueError as e:
                        print(f"跳过这一行坏数据{e}")
            print(f"数据加载完毕，共{len(self.stu_dict)}个数据")
        except FileNotFoundError:
            print("暂无档案，将创建新档案")

    def save_data(self):
        with open(self.file_path,"w",encoding = "utf8") as f:
            for stu in self.stu_dict.values():
                f.write(str(stu))
                f.write("\n")
            print("数据已保存")

    def add(self):
        print("准备添加学生，请依序填入学生信息。")
        name = input("请输入学生姓名：").strip()
        if name in self.stu_dict:
            print(f"学生{name}，已存在，是否继续")
            is_continue = input("继续请输入y，否则输入其他内容：")
            if is_continue != "y":
                return
        gender = input("请输入学生性别:").strip()
        tel = input("请输入学生电话：").strip()
        while True:
            try:
                age = int(input("请输入学生年龄："))
                break
            except ValueError:
                print(f"输入错误，请重新输入")
                continue
        info = input("请输入学生其它信息：").strip()
        stu_id = self.next_id()
        stu = Student(stu_id,name,gender,tel,age,info)
        self.stu_dict[name] = stu
        self.save_data()
        print("保存成功")

    def delete(self):
        print("准备删除学生信息")
        name = input("请输入要删除的学生姓名").strip()
        if name not in self.stu_dict:
            print(f"学生{name}信息不存在")
            return
        del self.stu_dict[name]
        print("学生信息删除成功")
        self.save_data()
        print("保存成功")
        if input(f"确认删除 {name}？(y/n)：").strip() != "y":
            return

    def next_id(self):
        if not self.stu_dict:
            return 1001
        max_id = max(stu.stu_id for stu in self.stu_dict.values())
        return max_id + 1

    def modify(self):
        print("准备修改学生信息")
        name = input("请输入要修改的学生姓名：").strip()
        if name not in self.stu_dict:
            print("学生信息不存在")
            return
        old_stu = self.stu_dict[name]
        print(f"当前信息 -> 性别:{old_stu.gender}, 电话:{old_stu.tel}, 年龄:{old_stu.age}, 其他:{old_stu.info}")
        print("（不修改的项请直接按回车跳过）")
        new_gender = input(f"请输入新性别 (原:{old_stu.gender})：").strip()
        new_tel = input(f"请输入新电话 (原:{old_stu.tel})：").strip()
        new_age_str = input(f"请输入新年龄 (原:{old_stu.age})：").strip()
        new_info = input(f"请输入新信息 (原:{old_stu.info})：").strip()
        if new_gender:
            old_stu.gender = new_gender
        if new_tel:
            old_stu.tel = new_tel
        if new_info:
            old_stu.info = new_info

        if new_age_str:
            try:
                old_stu.age = int(new_age_str)
            except ValueError:
                print("年龄格式错误，保留原年龄")
        self.save_data()
        print(f"{name} 的信息修改成功！")
        print(f"新信息：{old_stu}")

    def query_one(self):
        print("查询学生信息")
        name = input("请输入要查询的学生姓名：").strip()
        if name not in self.stu_dict:
            print("学生信息不存在")
            return None
        tool_stu = self.stu_dict[name]
        print(f"姓名：{tool_stu.name} | 性别:{tool_stu.gender} | 电话:{tool_stu.tel} | 年龄:{tool_stu.age} | 其他:{tool_stu.info}")
        return None

    def query_all(self):
        print("查询全部学生信息")
        if not self.stu_dict:
            print("暂无学生信息")
            return None
        total_stu = self.stu_dict.values()
        for i in total_stu:
            print(f"姓名：{i.name} | 性别:{i.gender} | 电话:{i.tel} | 年龄:{i.age} | 其他:{i.info}")
        return None