import os, zipfile, subprocess

def extract_zip():
    dir = '/etc/main.zip'
    target_dir = '/etc/workon'
    if os.path.isfile(dir):
        with zipfile.ZipFile(dir) as zip:
            for zip_info in zip.infolist():
    	        if zip_info.filename[-1] == '/':
    		        continue
    	        zip_info.filename = os.path.basename(zip_info.filename)
    	        zip.extract(zip_info,target_dir)
        print("Files Extract Successfuly")
    else:
        print('Zip File Not Found')
        os._exit(1)
def main():
    p1= subprocess.run(['/bin/bash', '-i', '-c', 'workon'],capture_output=True, text=True)
    if p1.returncode == 127 or p1.returncode == 1:
        try:            
            os.system("""echo "alias workon='source /usr/bin/workon/workon.sh'" >> /etc/bash.bashrc""")
        except:
            print('alias add failed')
            os._exit(1)
    else:
        print("Workon Name Already Exist")
        os._exit(1)
    extract_zip()


if __name__ == '__main__':
    main()