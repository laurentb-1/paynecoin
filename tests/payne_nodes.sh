#!/bin/bash
if [ -z "$1" ] || ( [ $1 != "init" ] && [ $1 != "list" ] && [ $1 != "kill" ] ) 
then
    echo "argument must be one of: 'init [port]', 'list', or 'kill'"
else
    if [ $1 = "init" ]
    then
        if [ -z "$2" ]
        then
            END=0
        else
            END=$(($2-1))
        fi
        BASE_PORT=5000
        for i in $(seq 0 $END)
            do
                PORT=$(($BASE_PORT+$i))
                nohup python paynecoin/api.py -p $PORT > /dev/null 2>&1 &
            done
    elif [ $1 = "list" ]
    then
        ps ax | grep paynecoin/api.py | grep -v grep
    elif [ $1 = "kill" ]
    then
        ps ax | grep paynecoin/api.py | grep -v grep | awk '{print $1}' | xargs kill
    fi
fi
