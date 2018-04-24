class A():
    def __init__(self, name, value, num, school):
        self.name = name
        self.value = value
        self.__num = num
        self.school = school

    def show(self):
        return "({0.name}, {0.value})".format(self)

    def __str__(self):
        return "(called by __str__ method, {0.name}, {0.value})".format(self)

    @property
    def private_num(self):
        return self.__num

    @private_num.setter
    def private_num(self, numvalue):
        self.__num = numvalue

    def check_public(self):
        if self.name != "lalala":
            return "not lalala"
        else:
            return "matched"

    def check_private(self):
        if self.private_num != "1000":
            return "not 1000"
        else:
            return "matched"

    def __added_num(self, value):
        num_to_add = int(self.private_num) + value
        return num_to_add

    def increase_value(self):
        new_value = self.__added_num(1000)
        return "(called by increase_value , {0})".format(new_value)

    def return_public(self):
        return self.__name

    @property
    def return_school(self):
        return self.__school


# print(__name__)

if __name__ == "__main__":
    myclass = A("liufanl", "27", "1991", "SFU")
    # print("run by Ref itself,", myclass.name, myclass.value)
    # print("also run by Ref itself," , myclass.show())
    # print("run by Ref itself and predefined function," , str(myclass))
    # print("return private number," , myclass.private_num)
    # print("set private number")
    # myclass.private_num = 2018
    # print("return new private number," , myclass.private_num)
    # print("check result:", myclass.check_public())
    # print("check result:", myclass.check_private())
    # print("increase_value result:", myclass.increase_value())
    """
    --- Not Work!
    print ("private function result:", myclass.__added_num(8))

    ---Not Work, AttributeError: 'A' object has no attribute '_A__name'
    print("check result:", myclass.return_public())
    """
    print("return school name:", myclass.return_school())
else:
    print("imported by some other program")