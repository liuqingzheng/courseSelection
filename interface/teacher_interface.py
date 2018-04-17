
from conf import setting
from lib import common
import os
from models import models


def check_course(teacher_name):
    '''
    查看教授的课程
    :param teacher_name:
    :return:
    '''
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    teach_course_list = teacher_obj.get_teach_course()
    return teach_course_list


def check_all_course():
    base_dir_course = os.path.join(setting.BASE_DB, 'course')
    course_list = common.get_all_file(base_dir_course)
    return course_list


def choose_course(teacher_name, course_name):
    '''
    讲该课程绑定到老师身上
    :param teacher_name:
    :param course_name:
    :return:
    '''
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    teacher_obj.bind_to_course(course_name)


def check_student_by_course(course_name):
    course_obj = models.Course.get_obj_by_name(course_name)
    return course_obj.student_name_list


def change_student_scour(teacher_name, student_name, course_name, score):
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    student_obj = models.Student.get_obj_by_name(student_name)
    teacher_obj.change_student_score(student_obj, course_name, score)
