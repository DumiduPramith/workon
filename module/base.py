import sys
import os
from database import Database
from workon_adder import add_path
from delete import delete_entry
from manual import arg_dict

# err= 'Error Occurred Contact Developer'

class Arguments():
    def limit_argumeent(limit=3):
        if len(sys.argv) > limit:
            print('Too many Arguments')
            print('Hint: Max 2 Arguments are allowed')
            os._exit(1)
    
    def argument_chkr():
        count=1
        for arg in sys.argv[1:2]:
            count+=1
            if arg.startswith('-'):
                Arguments.arg_define(arg,count)
            else:
                Arguments.limit_argumeent(2)
                name=Arguments.get_name_by_position(count-1)
                cond,path=Database.get_data('path',name)
                Arguments.check_database_condition_writef(cond,'@{}'.format(path))
                # File.read_path_file()

    def arg_define(arg,position):
        Arguments.check_arg_available()
        Arguments.check_arg_support()
        for i in str(arg).strip('-'):
            if i == 'v':
                name=Arguments.get_name_by_position(position)
                cond,path=Database.get_data('venv',name)
                Arguments.check_database_condition_writef(cond,'#{}'.format(path))
                cond,path=Database.get_data('path',name)
                Arguments.check_database_condition_writef(cond,'@{}'.format(path))
                # return True
            elif i == 'l':
                Others.call_get_path()
                # Others.call_get_venv(False)
                # return False
            elif i == 'a':
                add_path('path')
            elif i == 'd':
                delete_entry('path')
        return True
    def check_database_condition_writef(cond,path):
        if cond:
            File.write_file(path)

    def get_name_by_position(position):
        try:
            return str(sys.argv[position])
        except:
            print('get name by position error')

    def check_arg_support():
        try:
            if 'l' in sys.argv[1]:
                try:
                    if sys.argv[2]:
                        #File.write_file('-l Not Support with Work Name')
                        print('-l Not Support with Work Name')
                        os._exit(1)
                except:
                    pass
                if len(sys.argv[1]) >= 3:
                    if 'v' or 'p' in sys.argv[1] and 'l' in sys.argv[1]:
                        if 'v' in sys.argv[1]:
                            Others.call_get_venv()
                        if 'p' in sys.argv[1]:
                            Others.call_get_path()
                        os._exit(1)
                    # else:
                    #     print('-l not Support With Other Arguments')
                    #     os._exit(1)
            elif 'a' in sys.argv[1]:
                try:
                    if sys.argv[2]:
                        #File.write_file('-l Not Support with Work Name')
                        print('-a Not Support with Work Name')
                        os._exit(1)
                except:
                    pass
                if len(sys.argv[1]) >= 3:
                    if 'v' in sys.argv[1] and 'a' in sys.argv[1]:
                        if 'v' in sys.argv[1]:
                            add_path('venv')
                        os._exit(1)
                    # else:
                    #     print('-a not Support With Other Arguments')
                    #     os._exit(1)
            elif 'd' in sys.argv[1]:
                try:
                    if sys.argv[2]:
                        #File.write_file('-l Not Support with Work Name')
                        print('-d Not Support with Work Name')
                        os._exit(1)
                except:
                    pass
                if len(sys.argv[1]) >= 3:
                    if 'v' in sys.argv[1] and 'd' in sys.argv[1]:
                        if 'v' in sys.argv[1]:
                            delete_entry('venv')
                        os._exit(1)
                    # else:
                    #     print('-d not Support With Other Arguments')
                    #     os._exit(1)
            else:
                sys.argv[2]
        except:
            print('input valid')
            os._exit(1)

    def check_arg_available():
        if sys.argv[1]=='-':
            print('- Need Valid Argument')
        else:
            targ= sys.argv[1].strip('-')
            try:
                for arg in targ:
                    arg_dict[arg]
            except:
                print('Not Valid Argument')
                os._exit(1)

class File():
    def write_file(msg):
        with open('/etc/workon/temp.txt','a') as tempf:
            tempf.write(msg+'\n')

class Others:
    def call_get_path():
        table='path'
        # main_name_space, main_path_space= Print.list_header()
        Database.get_list(table)
    
    def call_get_venv(condition= True):
        table='venv'
        # main_name_space, main_path_space= Print.list_header(condition)
        Database.get_list(table)
