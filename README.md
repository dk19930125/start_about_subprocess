# start_about_subprocess
pi autostart 
树莓派自启动  起进程  加检测debug



使用进程启动效果等与 sh start.sh

#start.sh


;*#! /bin/sh

export PATH=$PATH:/usr/local/bin

cd /path/

nohup python project.py >> run_status.log 2>&1 &


