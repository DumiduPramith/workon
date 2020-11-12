import os
from database import Database

def add_path(table):
    cwd =os.getcwd()
    if table == 'path':
        print(cwd)
        workon_name, description= input_fun(table)
        val= Database.insert_data(table ,workon_name, cwd, description)
        if val == True:
            print('Workon Name {} Added Successfuly'.format(workon_name))
        else:
            print('Err')

    elif table == 'venv':
        while True:
            print('Fill Your Virtual env Path')
            env = input(str(cwd))
            env = cwd+env
            if '\\:*?<>"|' in env:
                print('Invalid Path')
                os._exit(1)
            else:
                if check_dir(env):
                    env= space_finder(env)
                    break
                else:
                    print('Dir Not Found')
        workon_name, description= input_fun(table)
        val =Database.insert_data(table ,workon_name, env, description)
        if val == True:
            print('Workon Name {} Added Successfuly'.format(workon_name))
        else:
            print('Err')


def input_fun(table):
    while True:
        workon_name = input(str('Enter Workon Name: '))
        if workon_name == '':
            print('Workon Name Cannot be empty')
        elif len(workon_name) >= 10:
            print('Workon Name Max Allow 10 Characters Only')
        elif ' ' in workon_name:
            print('Workon Name Not Allowed Spaces (" ")')
        elif Database.check_exist(table,workon_name):
            print('Workon Name Already Exist. Enter Another')
        else:
            break
    while True:
        print('Enter Workon description or Enter For None')
        description= input(str(': '))
        if len(description) >= 40:
            print('Description Max Allow 40 Characters Only')
        elif description == '':
            description = 'None'
            break
        else:
            break
    return workon_name, description

def space_finder(path):
	p_list = path.split('/')
	new_list= ''
	for item in p_list:
		if item == '':
			continue
		elif ' ' in item:
			length = len(item)
			temp =""
			if item[0] == "'" or item[0] == '"' and item[length-1] == "'" or item[length-1] == '"':
				new_list+='/{}'.format(item)
			else:
				temp+="/'{}'".format(item)
			new_list+=temp
		else:
			new_list+='/{}'.format(item)
	return new_list

def check_dir(dir):
    temp_dir=''
    if "'" in dir or '"' in dir:
        p_list = dir.split('/')
        for item in p_list:
            if item == '':
                continue
            elif "'" in item:
                a= item.strip("'")
                temp_dir+='/{}'.format(a)
            elif '"' in item:
                a= item.strip('"')
                temp_dir+='/{}'.format(a)
            else:
                temp_dir+='/{}'.format(item)
        return os.path.isfile(temp_dir)
    else:
        return os.path.isfile(dir)
