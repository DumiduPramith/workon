# Workon-Manager

Manager Script

1 • RECOMMEND OS UBUNTU

2 • RECOMMEND PYTHON3

3 • TO INSTALL, RUN THIS SCRIPT AS ROOT

# 4 • AFTER INSTALLATION TYPE WORKON MAN FOR HELP

# FOR INSTALL Workon-Manager
============================================================================

if [ $(whoami) == 'root' ]; then wget https://raw.githubusercontent.com/DumiduPramith/workon-manager/main/installer.sh; wget https://raw.githubusercontent.com/DumiduPramith/workon-manager/main/installer.py; chmod +x installer.sh; ./installer.sh; else clear; echo 'please run as root'; fi

============================================================================

# FOR UNSTALL Workon-Manager
============================================================================

if [ $(whoami) == 'root' ]; then bash /etc/workon/unstaller.sh; else clear; echo 'please run as root'; fi

============================================================================

# USER MANUAL
============================================================================
# Environment mean Python Virtual environment
    'man' : list user manual (eg. workon man)
    'a' : 'Add new Workon Directry' (eg. workon -a)
    'av' : 'Add new Workon Environment' (ag. workon -av)
    'l' : 'List View All Available Directories' (eg. workon -l)
    'lv' : 'List All Virtual Environment' 
    'd' : 'Delete Path'
    'dv' : 'Delete Virtual Environments'
============================================================================