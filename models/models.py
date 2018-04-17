import hashlib
import time
from db import db_handler


class BaseClass:
    '''
    所有类的基类
    '''

    @classmethod
    def get_obj_by_name(cls, name):
        return db_handler.select(name, cls.__name__)

    def save(self):
        db_handler.save(self)


class Admin(BaseClass):
    '''
    管理员类
    '''

    def register(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def creat_school(self, school_name, address):
        school = School(school_name, address)
        school.save()

    def creat_course(self, course_name):
        course = Course(course_name)
        course.save()

    def creat_teacher(self, teacher_name, password):
        teacher = Teacher(teacher_name, password)
        teacher.save()


class Teacher(BaseClass):
    '''
    老师类
    '''

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course_list = []

    def bind_to_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def get_teach_course(self):
        return self.course_list

    def change_student_score(self, student, course_name, score):
        student.scores[course_name] = score
        student.save()


class Student(BaseClass):
    '''
    学生类，继承人类的基类
    '''

    def __init__(self):
        self.course_list = []
        self.scores = {}

    def register(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def choose_school(self, school_name):
        self.school = school_name
        self.save()

    def choose_course(self, course_name):
        self.course_list.append(course_name)
        self.scores[course_name] = 0
        self.save()

    def get_course(self):
        course_list = []
        for course in self.course_list:
            course_list.append(db_handler.select(course, 'course'))
        return course_list

    def get_scores(self):
        return self.scores


class School(BaseClass):
    '''
    学校类
    '''

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.course_name_list = []

    def add_course(self, course):
        self.course_name_list.append(course)
        self.save()

    def get_course(self):
        course_list = []
        for course in self.course_name_list:
            course_list.append(db_handler.select(course, 'course'))
        return course_list


class Course(BaseClass):
    def __init__(self, name):
        self.name = name
        self.student_name_list = []

    def add_student(self, student_name):
        self.student_name_list.append(student_name)
        self.save()

    def get_student(self):
        student_list = []
        for student in self.student_name_list:
            student_list.append(db_handler.select(student, 'student'))

        return student_list
