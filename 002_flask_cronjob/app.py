from flask import Flask, request, json, Response, jsonify, make_response
from apscheduler.schedulers.background import BackgroundScheduler

# Instantiating the Flask application
application = Flask(__name__)

# Instantiating the scheduler for the cronjob
sched = BackgroundScheduler(daemon = True)
sched.start()

# Defining a cronjob function to run alongside the Flask app
@sched.scheduled_job(trigger = 'cron', minute = '*')
def print_hello():
    print('Hello world!')

# Defining a single API endpoint
@application.route('/test')
def test_func():
    js = json.dumps({'Test': 'Successful!'})
    return Response(json.dumps(js), status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    # Starting Flask application
    application.run(host = '0.0.0.0')
