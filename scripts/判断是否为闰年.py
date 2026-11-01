def check_year():
    while True:
        print("=" * 10, "检测闰年小程序", "=" * 10)
        print("=" * 34)
        print("输入9999退出程序")
        try:
            year = int(input("请输入年份："))
        except ValueError:
            print("请输入数字")
            continue
        if year == 9999:
            print("感谢使用，再见。")
            break
        elif 0 < year:
            if year % 4 == 0 and not year % 100 == 0:
                print(f"{year}年是闰年")
            elif year % 400 == 0:
                print(f"{year}年是闰年")
            else:
                print(f"{year}年不是闰年")
        else:
            print("输入的年份不合法")


if __name__ == "__main__":
    check_year()
