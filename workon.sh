#!/bin/bash
python3 /usr/bin/workon/module/workon.py $1 $2 $3 $4 $5
function identifier()
{
    if [ ${line:0:1} == '#' ]
    then
        length=${#line}
        templine_venv=${line:1:$length}
        activatevenv
        #echo $templine_venv
    elif [ ${line:0:1} == '@' ]
    then
        length=${#line}
        templine_dir=${line:1:$length}
        changedir
        #echo $templine_dir
    elif [ ${line:0:1} == '%' ]
    then
        length=${#line}
        templine=${line:1:$length}
        #echo $templine
    fi
}

function changedir()
{   
    cd $templine_dir
}

function activatevenv()
{
    source $templine_venv
}

file=/etc/workon/temp.txt
if [[ -f "$file" ]]
then
    while read line; do
        identifier line
    done <<<$(cat /etc/workon/temp.txt)
    rm /etc/workon/temp.txt
fi