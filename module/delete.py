from database import connection, Database
import os
def delete_entry(table):
    Database.get_list(table)
    print("Which {} Do you Want Delete? Enter Workon Name".format(table))
    del_name= input(str(' : '))
    status= Database.check_exist(table,del_name)
    if status:
        q = "DELETE FROM {} WHERE name='{}'".format(table,del_name)
        try:
            connection(q)
            print('{} {} Successfuly Deleted'.format(del_name,table))
        except:
            print('Error Occured')
            os._exit(1)
    else:
        print('Entered Workon Name not found')
        os._exit(1)
# delete_entry('path')