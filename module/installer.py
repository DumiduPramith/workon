import os, zipfile, subprocess

def extract_zip():
    dir = '/usr/bin/main.zip'
    target_dir = '/usr/bin/workon'
    if os.path.isfile(dir):
        with zipfile.ZipFile(dir,"r") as zip_ref:
            zip_ref.extractall(target_dir)
    else:
        print('Zip File Not Found')
        os._exit(1)
def main():
    p1= subprocess.run(['/bin/bash', '-i', '-c', 'workon'],capture_output=True, text=True)
    if p1.returncode == 127:
        try:            
            os.system("""echo "alias workon='source /usr/bin/workon/workon.sh'" >> ~/.bashrc""")
        except:
            print('alias add failed')
            os._exit(1)
    else:
        print("Workon Name Already Exist")
        os._exit(1)
    extract_zip()


if __name__ == '__main__':
    main()