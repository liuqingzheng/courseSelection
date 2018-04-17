import os


def login_auth(auth_type):
    from core import admin, student, teacher
    def auth(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'admin':
                if not admin.admin_info['name']:
                    print('请先登录')
                    admin.admin_login()
                else:
                    return func(*args, **kwargs)
            elif auth_type == 'teacher':
                if not teacher.teacher_info['name']:
                    print('请先登录')
                    teacher.teacher_login()
                else:
                    return func(*args, **kwargs)
            elif auth_type == 'student':
                if not student.student_info['name']:
                    print('请先登录')
                    student.student_login()
                else:
                    return func(*args, **kwargs)

        return wrapper

    return auth


def get_all_file(file_dir):
    file_list = []
    for _, _, files in os.walk(file_dir):
        for file in files:
            file_list.append(file)
    return file_list
