import os
# data=[('name','path','description','number')]
max_val=[]
item_count = 0
def convert_to_str(data):
    temp_list=[]
    temp_tup_list=[]
    for tup in data:
        for item in tup:
            temp_tup_list.append(str(item))
        temp_list.append(tuple(temp_tup_list))
        temp_tup_list = []
    return temp_list

def get_max_val(data):
    global max_val
    col= len(data[0])
    for loc in range(len(data)):
        if col > len(data[loc]):
            print('Wrong data')
            os._exit(1)
        elif loc == 0:
            for item in data[0]:
                max_val.append(len(item))
        else:
            tup = data[loc]
            for i in range(col):
                if max_val[i] < len(tup[i]):
                    max_val[i] = len(tup[i])
    # print(max_val)

def print_f_line():
    global max_val
    line=''
    for item in max_val:
        for i in range(item+3):
            if i == 0:
                line+='+'
            else:
                line+='-'
    line+='+'
    print(line)

def print_data(data,tup_loc):
    global max_val
    global item_count
    item_count = len(data)-1
    line=''
    n_loc = 0
    name_len= 0
    for item in max_val:
        for i in range(item+3):
            if name_len != 0:
                name_len-=1
                continue
            elif i == 0:
                line+='|'
            elif i == 2:
                name= data[tup_loc]
                # print(n_loc)
                name_len= len(name[n_loc])-1
                line+= name[n_loc]
            else:
                line+=' '
        n_loc+=1
    line+="|"
    n_loc =0
    print(line)

def print_total_line():
    global max_val
    global item_count
    max_len= len(max_val)*3
    line=''
    total_line =''
    count= 0
    for val in max_val:
        max_len+=val
    for num in range(max_len):
        if count != 0:
            line+='-'
            count-=1
            continue
        elif num == 0:
            line+='+'; total_line+='|'
        elif num == int(max_val[1]/2+max_val[0]):
            tot = 'Total    =     {}'.format(item_count)
            total_line+=tot
            count= len(tot)
            line+='-' ; total_line+=' '
        else:
            line+='-'; total_line+=' '
    line+='+'; total_line+='|'
    print(total_line)
    print(line)

def main(data):
    global max_val
    condition = True
    str_list=convert_to_str(data)
    # print(data)
    get_max_val(str_list)
    print_f_line()
    for tup_loc in range(len(str_list)):
        print_data(str_list,tup_loc)
        if condition:
            print_f_line()
            condition = False
    print_f_line()
    print_total_line()
    max_val = []

# main(data)
