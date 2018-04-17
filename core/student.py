
from interface import common_interface, student_interface, school_interface
from lib import common

student_info = {
    'name': None,
}


def student_register():
    if student_info['name']:
        print('已登录，不能注册')
        return
    print('学生注册')
    while True:
        name = input('please input your name(q to exit)>>:').strip()
        if name == 'q':break
        password = input('please input your password>>:').strip()
        conf_password = input('please config password>>:').strip()
        if password == conf_password:
            flag, msg, obj_id = student_interface.student_register(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)


        else:
            print('password not equles')


def student_login():
    if student_info['name']:
        print('已登录，不能重复登录')
        return
    print('学生登录')
    while True:
        name = input('please input your name(q to exit)>>:').strip()
        if name == 'q': break
        password = input('please input your password>>:').strip()
        flag, msg = common_interface.login_interface(name, password, 'student')
        if flag:
            student_info['name'] = name
            print(msg)
            break
        else:
            print(msg)
            continue


@common.login_auth(auth_type='student')
def choose_school():
    print('选择校区')
    while True:
        # 循环打印校区
        school_name_list = school_interface.check_all_school()
        if not school_name_list:
            print('暂无校区，请联系管理员创建校区')
            return
        for i, school in enumerate(school_name_list):
            print('%s schoolName：%s' % (i, school))
        choose = input('请先选择校区（输入数字）>>:')
        if choose == 'q': break
        if choose.isdigit():
            choose = int(choose)
            if choose >= 0 and choose < len(school_name_list):
                flag, msg = student_interface.choose_school(student_info['name'], school_name_list[choose])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print('请选择存在的学校')
        else:
            print('请输入数字')


@common.login_auth(auth_type='student')
def choose_course():
    print('选择课程')

    while True:
        flag, msg, course_name_list = student_interface.get_can_choose_course(student_info['name'])
        if not course_name_list:
            print('暂无可选择课程')
            return
        for i, course_name in enumerate(course_name_list):
            print('%s :%s' % (i, course_name))

        choice = input('please choice course(number)>>:').strip()
        if choice == 'q':break
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(course_name_list):
                flag, msg = student_interface.choose_course(student_info['name'], course_name_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('please input course exisit')
                continue
        else:
            print('please input number')


@common.login_auth(auth_type='student')
def check_score():
    print('查看成绩')
    score_dic = student_interface.get_score(student_info['name'])
    if score_dic:
        print(score_dic)
    else:
        print('暂无成绩')


func_dic = {
    '1': student_register,
    '2': student_login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,

}

def student_view():
    while True:
        print('''
        1、注册
        2、登录
        3、选择校区
        4、选择课程       
        5、查看成绩
        
        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()
