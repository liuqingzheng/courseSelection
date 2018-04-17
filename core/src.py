import core.teacher,core.student,core.admin

func_dic = {
    '1': core.admin.admin_view,
    '2': core.teacher.teacher_view,
    '3': core.student.student_view
}


def run():
    while True:
        print('''
        请选择登录角色：
        1、管理员视图
        2、老师视图
        3、学生视图
        
        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()
