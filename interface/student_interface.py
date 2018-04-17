
from models import models



def student_register(name, password):
    '''
    学生注册接口
    :param name:
    :param password:
    :return:
    '''
    obj = models.Student.get_obj_by_name(name)
    if not obj:
        student = models.Student()
        student.register(name, password)
        return True, 'student %s register success' % name, student.name
    else:
        return False, 'userName exisit,please change', None


def choose_school(student_name, school_name):
    '''
    选择学校接口
    :param student_name:
    :param school_name:
    :return:
    '''
    obj = models.Student.get_obj_by_name(student_name)
    #先检查是否选择了校区，选择了校区不能再选
    if  obj.school:
        return False,'您已经选择过校区了'
    else:
        obj.choose_school(school_name)
        return True, '%s choose %s school，success' % (student_name, school_name)

def get_school_by_student(student_name):
    '''
    通过学生姓名获取所在学校接口
    :param student_name:
    :return:
    '''
    obj_student = models.Student.get_obj_by_name(student_name)
    return obj_student.school

def get_can_choose_course(student_name):
    '''
    查询该学生能选的课程，通过学生的学校拿到课程
    :param student_name:
    :return:
    '''
    obj_student = models.Student.get_obj_by_name(student_name)
    if obj_student.school:
        # 通过学生，拿到学生所在学校，通过学校，拿出学校所有课程
        obj_school = models.School.get_obj_by_name(obj_student.school)
        return True, 'success', obj_school.course_name_list

    else:
        return False, 'please choose school first', None


def choose_course(student_name, course_name):
    '''
    选择课程接口
    :param student_name:
    :param course_name:
    :return:
    '''
    obj_student = models.Student.get_obj_by_name(student_name)
    obj_course = models.Course.get_obj_by_name(course_name)
    obj_student.choose_course(course_name)
    obj_course.add_student(student_name)

    return True, '%s choose %s course，success' % (student_name, course_name)


def get_score(student_name):
    '''
    获取分数接口
    :param student_name:
    :return:
    '''
    obj_student = models.Student.get_obj_by_name(student_name)
    return obj_student.scores
