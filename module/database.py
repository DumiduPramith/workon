import sqlite3
import os, sys
if __name__ == 'module.database':
    from module.make_table import main
else:
    from make_table import main

name_length=0
path_length=0
description_length=0

def connection(quary,condition=True):
    conn = sqlite3.connect('/etc/workon/workon.db')
    c = conn.cursor()
    c.execute(quary)
    if condition:
        return c.fetchall()
    conn.commit()
    conn.close()

class Database:
    def insert_data(tname,name,path,description=None):
        condition= False
        q = 'INSERT INTO {} (name,path,description) VALUES ("{}","{}","{}")'.format(tname,name,path,description)
        try:
            connection(q,condition)
            return True
        except:
            return False

    def get_data(tname,name): # tname = Table name
        q = 'SELECT path FROM {} WHERE name="{}"'.format(tname,name)
        # print(q)
        val= connection(q)
        # print(val)
        if len(val) == 0:
            print('{} Name not found'.format(tname))
            return False, None
        elif len(val) >= 2:
            print('get data error')
            os._exit(1)
        else:
            temp= val[0]
            return True,temp[0]

    def get_list(table):
        q= 'SELECT name,path,description FROM {}'.format(table)
        list= connection(q)
        head = ('name','path','description')
        list.insert(0,head)
        main(list)
            
    def check_exist(table,workon_name):
        q = "SELECT name FROM {} WHERE name='{}'".format(table,workon_name)
        data = connection(q)
        if len(data) == 0:
            return False
        else:
            return True
