class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は未成年です。")

human1 = Human("太郎",10)
human2 = Human("次郎",5)
human3 = Human("三郎",30)
human4 = Human("花子",15)
human5 = Human("花絵",25)

human_lists = [human1, human2, human3, human4, human5]

for i in human_lists:
    Human.check_adult(i)

