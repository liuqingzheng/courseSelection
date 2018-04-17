from interface import common_interface, admin_interface, school_interface
from lib import common

admin_info = {
    'name': None
}


def admin_register():
    print('管理员注册')
    if admin_info['name']:
        print('已登录，不能注册')
        return
    while True:
        name = input('please input your name(q to exit)>>:').strip()
        if 'q' == name: break
        password = input('please input password>>:').strip()
        conf_password = input('please confim password>>:').strip()

        if password == conf_password:
            flag, msg = admin_interface.admin_register(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                continue
        else:
            print('password not equles')


def admin_login():
    if admin_info['name']:
        print('已登录，不能重复登录')
        return
    print('管理员登录')
    while True:
        name = input('please input your name(q to exit)>>:').strip()
        if 'q' == name: break
        password = input('please input your password>>:').strip()
        flag, msg = common_interface.login_interface(name, password, 'admin')
        if flag:
            admin_info['name'] = name
            print(msg)
            break

        else:
            print(msg)


@common.login_auth(auth_type='admin')
def creat_school():
    print('创建学校')
    while True:
        school_name = input('please input school name>>:').strip()
        if school_name == 'q': break
        school_address = input('please input school address>>:').strip()

        flag, msg = admin_interface.creat_school(admin_info['name'], school_name, school_address)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth(auth_type='admin')
def creat_teacher():
    print('创建老师')
    while True:
        teacher_name = input('please input teacher name>>:').strip()
        if teacher_name == 'q': break
        # 这里可以继续录入老师的年龄，性别，级别，薪资等
        flag, msg = admin_interface.creat_teacher(admin_info['name'], teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth(auth_type='admin')
def creat_course():
    print('创建课程')
    while True:
        # 创建课程之前先选择学校
        school_name_list = school_interface.check_all_school()
        if not school_name_list:
            print('学校为空，创建课程前请先创建学校')
            return
        for i, school in enumerate(school_name_list):
            print('%s schoolName：%s' % (i, school))
        choose = input('请先选择校区（输入数字）>>:')
        if choose == 'q': break
        if choose.isdigit():
            choose = int(choose)
            if choose >= 0 and choose < len(school_name_list):
                course_name = input('please input course name>>:').strip()
                flag, msg = admin_interface.creat_course(admin_info['name'], school_name_list[choose], course_name)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('请输入存在的校区')
        else:
            print('must input number')



func_dic = {
    '1': admin_register,
    '2': admin_login,
    '3': creat_school,
    '4': creat_teacher,
    '5': creat_course

}


def admin_view():
    while True:
        print('''
        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程
        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()
