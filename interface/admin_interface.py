from models import models


def admin_register(name, password):
    '''
    管理员注册接口
    :param name:
    :param password:
    :return:
    '''
    obj = models.Admin.get_obj_by_name(name)
    if not obj:
        admin = models.Admin()
        admin.register(name, password)
        return True, 'admin %s register success' % name
    else:
        return False, 'userName exisit,please change'


def creat_school(admin_name, school_name, address):
    '''
    创建学校接口
    :param admin_name:
    :param school_name:
    :param address:
    :return:
    '''
    obj = models.School.get_obj_by_name(school_name)
    if not obj:  # 学校不存在，继续创建
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.creat_school(school_name, address)
        return True, 'school creat success'
    else:
        return False, 'school is exisit'


def creat_teacher(admin_name, teacher_name, password='456'):
    '''
    创建老师接口，默认密码为456，后期可以写一个修改密码的接口
    :param admin_name:
    :param teacher_name:
    :param password:
    :return:
    '''
    obj = models.Teacher.get_obj_by_name(teacher_name)
    if not obj:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.creat_teacher(teacher_name, password)
        return True, 'teacher creat success'

    else:
        return False, 'teacher is exisit'


def creat_course(admin_name, school_name, course_name):
    '''
    创建课程接口
    :param admin_name:
    :param school_name:
    :param course_name:
    :return:
    '''
    course_obj = models.Course.get_obj_by_name(course_name)
    if not course_obj:
        admin_obj= models.Admin.get_obj_by_name(admin_name)
        # 管理员创建课程
        admin_obj.creat_course(course_name)

        # 把课程关联到学校，保存
        school_obj = models.School.get_obj_by_name(school_name)
        school_obj.add_course(course_name)
        return True, 'course creat success'
    else:
        return False, 'course is exisit'
