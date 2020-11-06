import sys
import os

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

arg_dict = {
    'v' : 'Virtual Environment',
    'l' : 'List View All Available Directories'
}

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
                if Arguments.arg_define(arg,count):
                    File.read_path_file(count)
            else:
                Arguments.limit_argumeent(2)
                File.read_path_file()

    def arg_define(arg,count):
        Arguments.check_arg_available()
        Arguments.check_arg_support()
        for i in str(arg).strip('-'):
            if i == 'v':
                File.read_virtualenv_file(count)
            if i == 'l':
                print('wait')
                return False
        return True

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
                    print('-l not Support With Other Arguments')
                    os._exit(1)
            else:
                sys.argv[2]
        except:
            print('input valid')
            os._exit(1)

    def check_arg_available():
        for arg in sys.argv[1].strip('-'):
            try:
                arg_dict[arg]
            except:
                print('Not Valid Argument')
                os._exit(1)

class File():
    def read_virtualenv_file(count):
        with open(os.path.join(BASE_DIR,'virtualenv.txt'),'r') as path_virtualenv:
            for line in path_virtualenv:
                name, location, description = line.split(':')
                if File.name_chkr(name,count) == 1:
                    File.write_file('#{}'.format(location))
                    #print('#{}'.format(location))
                else:
                    print('virtual env not found')

    def read_path_file(count=1):
        condition = True
        with open(os.path.join(BASE_DIR,'paths.txt'),'r') as path_f:
            for line in path_f:
                name, location, description = line.split(':')
                if File.name_chkr(name,count) == 1:
                    File.write_file('@{}'.format(location))
                    #print('@{}'.format(location))
                    condition = False
            if condition:
                print('Workon Name Not Found')


    def name_chkr(name,count=1): #check input name
        if sys.argv[count] == str(name):
            return 1
        else:
            return 0

    def write_file(msg):
        with open(os.path.join(BASE_DIR,'temp.txt'),'a') as tempf:
            tempf.write(msg+'\n')