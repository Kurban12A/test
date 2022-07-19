class Studend:
    def __init__(self, name, groupNumber, age):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age


    def setName(self):
        self.name = input()
        return self.name


    def setAge(self):
        self.age = input()
        return self.age


    def setGroupNumber(self):
        self.groupNumber = input()
        return self.groupNumber


    def getName(self, name):
        lst_name = []
        if self.name != '':
            lst_name.append(self.name)
            return lst_name
        else:
            print('Err_name')

    def getAge(self, age):
        lst_age = []
        if self.age != '':
            lst_age.append(self.age)
            return lst_age
        else:
            print('Err_age')

    def getGroupNumber(self, groupNumber):
        lst_groupNumber = []
        if self.groupNumber != '':
            lst_groupNumber.append(self.groupNumber)
            return lst_groupNumber
        else:
            print('Err_groupNumber')


student = Studend('Иванов', '29', 'Helsom')

print(student.setName())
print(student.setAge())
print(student.setGroupNumber())
print(student.getName(student))
print(student.getAge(student))
print(student.getGroupNumber(student))
