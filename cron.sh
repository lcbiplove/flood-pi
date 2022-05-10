#!/bin/bash

FILE_NAME="main.py"

crontab -u $USER -l| grep $PWD/$FILE_NAME > /dev/null
if [ $? -eq 0 ]
then
	echo "$FILE_NAME is already running"
else
	echo "* * * * * cd $PWD && $PWD/.venv/bin/python $FILE_NAME >> /tmp/sensor_out.log 2>> /tmp/sensor_err.log" | crontab -
	echo "Cron job added. '$PWD/$FILE_NAME' will run every minute."
fi
