import os, zipfile, subprocess

def extract_zip():
    dir = '/etc/main.zip'
    target_dir = '/etc/workon'
    if os.path.isfile(dir):
        with zipfile.ZipFile(dir) as zip:
            for zip_info in zip.infolist():
    	        if zip_info.filename[-1] == '/':
    		        continue
    	        elif zip_info.filename.startswith('workon-manager-main/'):
    		        zip_info.filename = zip_info.filename.replace('workon-manager-main/','')
    	        zip.extract(zip_info,target_dir)
        print("Files Extract Successfuly")
    else:
        print('Zip File Not Found')
        os._exit(1)
def main():
    try:
        p1= subprocess.run(['python3', '--version', '>/dev/null'],stdout=subprocess.PIPE)
        ver = p1.stdout.decode('UTF-8').strip('\n').split(' ')[1].split('.')
        if int(ver[1] < 6):
            try:
                subprocess.check_output(['/bin/bash', '-i', '-c', 'workon'])
                returncode = 0
            except subprocess.CalledProcessError:
                returncode = 127
        else:
            p1= subprocess.run(['/bin/bash', '-i', '-c', 'workon'],capture_output=True, text=True)
            returncode = p1.returncode
    except:
        # remove created file and folder in installer.sh and exit code
        if os.path.isfile('/etc/main.zip'):
            os.system("rm /etc/main.zip")
        if os.path.isdir('/etc/workon'):
            os.system('rm -rf /etc/workon')
        os._exit(1)
    
    if returncode == 127 or returncode == 1:
        try:            
            os.system("""echo "alias workon='source /etc/workon/workon.sh'" >> /etc/bash.bashrc""")
        except:
            print('alias add failed')
            os._exit(1)
    else:
        print("Workon Name Already Exist")
        os._exit(1)
    extract_zip()
    print('============================')
    print('Thanks For Using Workon-Manager')
    print('Successfuly Installed')
    print('Type Workon or workon man for help')
    print('============================')


if __name__ == '__main__':
    main()