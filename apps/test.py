class Person:

    def __init__(self):
        self._age = None

    # 获取操作
    @property
    def age(self):
        if self._age > 0:
            return self._age
        else:
            return 0

    # 设置值
    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age

    # get set方法


if __name__ == '__main__':
    user = Person()
    user.age = 1
    print(user.age)
