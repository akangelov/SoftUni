#Mankind

import re

def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not (regex.search(string) == None):
        raise Exception("Invalid faculty number!")

if __name__ == '__main__' :


    class Human:
        def __init__(self, f_name, l_name):
            self.f_name = f_name
            self.l_name = l_name


        @property
        def f_name(self):
            return self.__f_name

        @f_name.setter
        def f_name(self, value: str):
            if len(value) < 3:
                raise Exception("Expected length at least 4 symbols! Argument: firstName")
            if not value[0].isupper():
                raise Exception("Expected upper case letter! Argument: firstName")
            self.__f_name = value

        @property
        def l_name(self):
            return self.__l_name

        @l_name.setter
        def l_name(self, value: str):
            if len(value) < 3:
                raise Exception("Expected length at least 3 symbols! Argument: lastName ")
            if not value[0].isupper():
                raise Exception("Expected upper case letter! Argument: lastName")
            self.__l_name = value


    class Student(Human):
        def __init__(self, f_name, l_name, fac_number):
            Human.__init__(self, f_name, l_name)
            self.fac_number = fac_number

        @property
        def fac_number(self):
            return self.__fac_number

        @fac_number.setter
        def fac_number(self, value):
            if not 5 <= len(value) <= 10:
                raise Exception("Invalid faculty number!")
            run(value)
            self.__fac_number = value


        def __str__(self):
            return f"First Name: {self.f_name}\nLast Name: {self.l_name}\nFaculty number: {self.fac_number}"


    class Worker(Human):
        def __init__(self, f_name, l_name, w_sal, wh_per_day):
            Human.__init__(self, f_name, l_name)
            self.w_sal = w_sal
            self.wh_per_day = wh_per_day
            self.sal_per_hour = float((w_sal/(wh_per_day*5)))

        @property
        def w_sal(self):
            return self.__w_sal

        @w_sal.setter
        def w_sal(self, value):
            if value <= 10:
                raise Exception("Expected value mismatch! Argument: weekSalary")
            self.__w_sal = value

        @property
        def wh_per_day(self):
            return self.__wh_per_day

        @wh_per_day.setter
        def wh_per_day(self, value):
            if not 1 <= value <= 12:
                raise Exception("Expected value mismatch! Argument: workHoursPerDay")
            self.__wh_per_day = value


        def __str__(self):
            return f"First Name: {self.f_name}\nLast Name: {self.l_name}\nWeek Salary: {self.w_sal:.2f}\nHours per day: {self.wh_per_day:.2f}\nSalary per hour: {self.sal_per_hour:.2f} "


    try:
        data_list = input().split()

        first_name = str(data_list[0])
        last_name = str(data_list[1])
        faculty_number = str(data_list[2])

        student = Student(first_name, last_name, faculty_number)

        data_list = input().split()

        first_name = str(data_list[0])
        last_name = str(data_list[1])
        week_sal = float(data_list[2])
        hours_per_day = float(data_list[3])

        worker = Worker(first_name, last_name, week_sal, hours_per_day)

        print(student)
        print()
        print(worker)
    except Exception as ex:
        print(ex)