#!/bin/bash
rm -rf /etc/workon
lin=$(cat /etc/bash.bashrc | grep -n "workon" | cut -f1 -d:)
if [[ $lin != '' ]]; then
sed -i $lin'd' /etc/bash.bashrc
else echo "workon name not found"
echo "Something went wrong"
fi
echo 'Workon-Manager Successfully Deleted'