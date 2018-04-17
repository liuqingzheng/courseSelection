from db import models


def login_interface(name, password, type):
    '''
    登录的通用接口
    :param name:
    :param password:
    :param type:
    :return:
    '''
    if type == 'admin':
        obj = models.Admin.get_obj_by_name(name)
    elif type == 'teacher':
        obj = models.Teacher.get_obj_by_name(name)
    elif type == 'student':
        obj = models.Student.get_obj_by_name(name)
    else:
        return False, 'error'
    if obj:
        if password == obj.password:
            return True, '%s :%s login success' % (type, name)
        else:
            return False, 'password error'
    else:
        return False, '%s: %s is not exisit' % (type, name)
