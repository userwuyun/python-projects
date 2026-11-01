
class Student:
    def __init__(self,stu_id,name,gender,tel,age,info):
        self.stu_id = stu_id
        self.name = name
        self.gender = gender
        self.tel = tel
        self.age = age
        self.info = info

    def __str__(self):
        return ",".join([str(self.stu_id),self.name,self.gender,self.tel,str(self.age),self.info])

    @staticmethod
    def generate(stu_str: str):
        arr = stu_str.split(",")
        return Student(int(arr[0]),arr[1],arr[2],arr[3],int(arr[4]),arr[5])



# s = Student.generate("1001,张三,男,22,123,无")
