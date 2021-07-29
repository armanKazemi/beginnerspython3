import sys


class Student(object):

    def __init__(self, name, age, email, major):
        self.name = name
        self.age = age
        self.email = email
        self.major = major

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}, email: {self.email}, major: {self.major}'


class Class:
    """Class class"""

    STUDENT = 'student'
    FOOTBALL = 'football'
    BASKETBALL = 'basketball'
    VOLLEYBALL = 'volleyball'

    def __init__(self):
        self.students = []
        self.football_major = []
        self.basketball_major = []
        self.volleyball_major = []

    def see_list(self, name_list):
        if name_list == self.STUDENT:
            purpose = self.students
        elif name_list == self.FOOTBALL:
            purpose = self.football_major
        elif name_list == self.BASKETBALL:
            purpose = self.basketball_major
        elif name_list == self.VOLLEYBALL:
            purpose = self.volleyball_major
        else:
            purpose = []

        if len(purpose) == 0:
            print('There is not information to display.')

        for i in range(len(purpose)):
            print('\t' + str(i+1) + '. ' + str(purpose[i]))

        print()
        input('Press any key to continue...')
        print()

    def edit_student(self):
        pass

    def add_student(self):
        student = Student('', 0, '', '')

        name = input('Please enter your name: ')
        student.set_name(name)

        while True:
            age = input('How old are you? ')
            if age.isnumeric():
                student.set_age(int(age))
                break

            print('You should enter an integer.')

        email = input('Please enter your email address: ')
        student.set_email(email)

        print('Please chose one of these majors.' + '\n' +
              '\t1. ' + self.FOOTBALL + '\n' +
              '\t2. ' + self.BASKETBALL + '\n' +
              '\t3. ' + self.VOLLEYBALL)

        while True:
            major = input('Pick one: ')
            if major.isnumeric() and '1' <= major <= '3':
                if int(major) == 1:
                    student.set_major(self.FOOTBALL)
                elif int(major) == 2:
                    student.set_major(self.BASKETBALL)
                elif int(major) == 3:
                    student.set_major(self.VOLLEYBALL)
                break
            print('Enter in correct way.')
        print()
        return student

    def set_new_student(self, student):
        self.students.append(student)

        if student.get_major() == self.VOLLEYBALL:
            self.volleyball_major.append(student)
        elif student.get_major() == self.BASKETBALL:
            self.basketball_major.append(student)
        elif student.get_major() == self.FOOTBALL:
            self.football_major.append(student)

    def menu(self):
        while True:
            print('\t1. Add new student.\n' +
                  '\t2. Edit student information.\n' +
                  '\t3. See the student list.\n' +
                  '\t4. See the football list.\n' +
                  '\t5. See the basketball list.\n' +
                  '\t6. See the volleyball list.\n' +
                  '\t7. Exit.')

            option = input('Please pick one of the above options: ')

            if option.isnumeric() and 1 <= int(option) <= 7:
                return int(option)
            else:
                print('Please pick in correct way.\n')

    def main(self):
        print('Welcome to Panda Jojo school.')

        while True:
            selection = self.menu()
            if selection == 1:
                student = self.add_student()
                self.set_new_student(student)
            elif selection == 2:
                self.edit_student()
            elif selection == 3:
                self.see_list(self.STUDENT)
            elif selection == 4:
                self.see_list(self.FOOTBALL)
            elif selection == 5:
                self.see_list(self.BASKETBALL)
            elif selection == 6:
                self.see_list(self.VOLLEYBALL)
            elif selection == 7:
                sys.exit()


if __name__ == '__main__':
    cl = Class()
    cl.main()
