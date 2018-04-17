from lib import common
from conf import setting
import os


def check_all_school():
    base_dir_school = os.path.join(setting.BASE_DB, 'school')
    school_list = common.get_all_file(base_dir_school)
    return school_list
