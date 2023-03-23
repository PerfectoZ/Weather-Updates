from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

from Email import SendMail
from Request import Fetch

from Name import Work

scheduler = BackgroundScheduler()
scheduler.add_job(function=Work, trigger='interval', min=1)
scheduler.start()

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
