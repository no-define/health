# health
punch card with selenium

# Run
pipenv run python card.py

# Crontab命令:<br>
`crontab -l`:显示当前用户的crontab任务。<br>
`crontab -e`:编辑当前用户的crontab任务。<br><br>

crontab任务配置格式: `* * * * * command` <br>
&emsp;示例1：`*/1 * * * * python /Users/zy/PycharmProjects/GuassTest/test1.py >> /Users/zy/testresult.log 2>&1`<br>
&emsp;示例2：`*/10 * * * * cd ~/sentry/sentry &&    /home/op/.local/share/virtualenvs/sentry-UYqSYN2w/bin/python ~/sentry/sentry/detect.py >> ~/sentry/sentry.log 2>&1`(其中 > /dev/null 2>&1 为输出重定向，忽略日志输出)<br>
<br> 
