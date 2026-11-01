from student import Student
from studentms import StudentMS

class MainProgram:
    def __init__(self):
        self.ms = StudentMS()

    def stu_program(self):
        while True:
            print("\n" + "-" * 62)
            print("  1. 添加学生     2. 修改学生     3. 删除学生")
            print("  4. 查询学生     5. 显示全部     0. 退出系统")
            print("-" * 62)
            try:
                num = int(input("请输入需要的操作(0~5):"))
            except ValueError:
                print("请输入数字")
                continue
            if num < 0 or num > 5:
                print("输入的操作无效，请重新输入。")
                continue

            elif num == 1:
                self.ms.add()

            elif num == 2:
                self.ms.modify()

            elif num == 3:
                self.ms.delete()

            elif num == 4:
                self.ms.query_one()

            elif num == 5:
                self.ms.query_all()

            elif num == 0:
                break

            else:
                print("输入有误")

if __name__ == "__main__":
    MainProgram().stu_program()




