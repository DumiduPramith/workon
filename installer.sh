#!/bin/bash
function check_pkg(){
    if [[ $(dpkg --get-selections|grep -w "python3"|head -1) =~ "python3" ]]
    then
        :
    else
        apt-get install python3 -y &>/dev/null
    fi
    if [[ $(dpkg --get-selections|grep -w "curl"|head -1) =~ "curl" ]]
    then
        :
    else
        apt-get install curl -y &>/dev/null
    fi
}

function download_zip(){
    curl -L -o /etc/main.zip https://github.com/DumiduPramith/workon/archive/main.zip
}

function main(){
    check_pkg
    download_zip
    mkdir /etc/workon
    dir=$(pwd)
    python3 $dir/installer.py
    python3 /etc/workon/module/database_create.py
    chmod -R ugo+rwx /etc/workon
    rm -rf /etc/main.zip
}

if [ $(whoami) == 'root' ]
then
    main
else
    echo 'Please run as root'
fi
exit
