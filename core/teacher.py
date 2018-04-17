
from interface import common_interface, teacher_interface
from lib import common
teacher_info = {
    'name': None
}


def teacher_login():
    if teacher_info['name']:
        print('已登录，不能重复登录')
        return
    print('老师登录')
    while True:
        name = input('please input your name>>:').strip()
        if 'q' == name:break
        password = input('please input your password>>:').strip()
        flag, msg = common_interface.login_interface(name, password, 'teacher')
        if flag:
            teacher_info['name'] = name
            print(msg)
            break
        else:
            print(msg)
            continue


@common.login_auth(auth_type='teacher')
def check_course():
    print('查看教授课程')
    course_list = teacher_interface.check_course(teacher_info['name'])
    if not course_list:
        print('您暂无教授课程，请去选择教授课程')
        return
    for course in course_list:
        print(course)


@common.login_auth(auth_type='teacher')
def choose_course():
    print('选择教授课程')
    while True:
        course_list = teacher_interface.check_all_course()
        if not course_list:
            print('暂无课程可以选择，请联系管理员创建课程')
            return
        for i, course in enumerate(course_list):
            print('%s :%s' % (i, course))
        choice = input('请选择您要教授的课程:').strip()
        if choice =='q':break
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(course_list):
                teacher_interface.choose_course(teacher_info['name'], course_list[choice])
                break
            else:
                print('请选择存在的课程')
        else:
            print('请输入数字')


@common.login_auth(auth_type='teacher')
def check_student():
    print('查看课程下学生')
    course_list = teacher_interface.check_course(teacher_info['name'])
    if not course_list:
        print('您暂无教授课程，请先选择课程')
        return
    for i, course in enumerate(course_list):
        print('%s : %s' % (i, course))
    choice = input('请选择要查看的课程').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(course_list):
            student_list = teacher_interface.check_student_by_course(course_list[choice])
            for i, student in enumerate(student_list):
                print('%s : %s' % (i, student))
        else:
            print('请选择存在的课程')
    else:
        print('只能输入数字')


@common.login_auth(auth_type='teacher')
def modify_score():
    print('修改成绩')
    while True:
        course_list = teacher_interface.check_course(teacher_info['name'])
        if not course_list:
            print('您暂无教授的课程，请先选择教授课程')
            break
        for i, course in enumerate(course_list):
            print('%s : %s' % (i, course))
        choice = input('请选择要查看的课程').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(course_list):
                student_list = teacher_interface.check_student_by_course(course_list[choice])
                if not student_list:
                    print('该课程下暂无学生')
                    break
                for i, student in enumerate(student_list):
                    print('%s : %s' % (i, student))

                choice_student = input('请选择要修改的学生').strip()
                if choice_student.isdigit():
                    choice_student = int(choice_student)
                    if choice_student >= 0 and choice_student < len(student_list):
                        print('选择了学生：%s' % student_list[choice_student])
                        score = input('请输入要修改的分数：').strip()
                        if score.isdigit():
                            score = int(score)
                            # teacher_name,student_name,course_name,score
                            teacher_interface.change_student_scour(teacher_info['name'], student_list[choice_student],
                                                                   course_list[choice], score)
                            break
                        else:
                            print('只能输入数字')
            else:
                print('请选择存在的课程')
        else:
            print('只能输入数字')


func_dic = {
    '1': teacher_login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': modify_score,

}


def teacher_view():
    while True:
        print('''
        1、登录
        2、查看教授课程
        3、选择教授课程
        4、查看课程下学生
        5、修改学生成绩
        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()
