from make_table import main
arg_dict = {
    'v' : 'Virtual Environment',
    'l' : 'List View All Available Directories',
    'a' : 'Add new Workon Directry',
    'av' : 'Add new Workon Environment',
    'lv' : 'List All Virtual Environment',
    'lp' : 'List All Paths',
    'd' : 'Delete Path',
    'dv' : 'Delete Virtual Environments'
}

manual_dict = {
    'man' : 'list user manual (eg. workon man)',
    'a' : 'Add new Workon Directry (eg. workon -a)',
    'av' : 'Add new Workon Environment (ag. workon -av)',
    'l' : 'List View All Available Directories (eg. workon -l)',
    'lv' : 'List All Virtual Environment',
    'd' : 'Delete Path',
    'dv' : 'Delete Virtual Environments'
}

def manual():
    man_list = [('Argument','Description')] # manual list
    for item in manual_dict:
        temp = (item, manual_dict[item])
        man_list.append(temp)
    main(man_list, 'Workon Manual')
