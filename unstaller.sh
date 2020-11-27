#!/bin/bash
function main()
{
    if [[ -d '/etc/workon' ]]; then
    rm -rf /etc/workon
    else echo 'Workon folder not found'
    fi
    lin=$(cat /etc/bash.bashrc | grep -n "workon" | cut -f1 -d:)
    if [[ $lin != '' ]]; then
    sed -i $lin'd' /etc/bash.bashrc
    echo 'Workon-Manager Successfully Deleted'
    else echo "workon name not found"
    echo "May be already deleted"
    fi
}

if [ $(whoami) == 'root' ]
then
    main
else
    echo 'Please run as root'
fi
exit
