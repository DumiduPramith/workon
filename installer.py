from module.database import Database, connection
import os, zipfile, subprocess

def create_table():
    condition=False
    path_table = '''CREATE TABLE path (
        path_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL,
        description TEXT
    )'''
    connection(path_table,condition)
    venv_table = '''CREATE TABLE venv (
        venv_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL,
        description TEXT
    )'''
    connection(venv_table,condition)

def extract_zip():
    dir = '/usr/bin/main.zip'
    target_dir = os.path.join(os.getenv("HOME"),'workon')
    if os.path.isfile(dir):
        with zipfile.ZipFile(dir,"r") as zip_ref:
            zip_ref.extractall("targetdir")
    else:
        print('Zip File Not Found')
        os._exit(1)
def main():
    p1= subprocess.run(['/bin/bash', '-i', '-c', 'workon'],capture_output=True, text=True)
    if p1.returncode == 127:
        try:            
            os.system("""echo "alias workon='source ~/workon/workon.sh'" >> ~/.bashrc""")
        except:
            print('alias add failed')
            os._exit(1)
        try:
            create_table()
            print('sucess')
        except:

            print('create table failed')
            os._exit(1)
    else:
        print("Workon Name Already Exist")
        os._exit(1)
    extract_zip()


if __name__ == '__main__':
    main()