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

def manual():
    man_list = [('Argument','Description')] # manual list
    for item in arg_dict:
        temp = (item, arg_dict[item])
        man_list.append(temp)
    main(man_list, 'Workon Manual')
