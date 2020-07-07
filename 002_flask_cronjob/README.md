# Data Science Quick Tip #002: Running a Cronjob from Within a Flask API!
This repo contains the code supporting the blog post discussing how to run a cronjob within a Flask API. In this README, we'll quickly touch on the required pieces to run this code as well as how to invoke this script.

## Required Installations
If not installed already, you will need to pip install the following packages.
- ```APscheduler==3.6.3```
- ```flask==1.1.1```

## Script Invocation
I have this script to run very simply using the following command in your terminal:

```python app.py```

This will start up the Flask API, at which point you can sit back and watch the statement ```Hello world!``` printed at the beginning of every minute.

If you would also like to invoke the test endpoint I created, simply open another window in your terminal and issue the following command:

```curl 0.0.0.0/5000/test```
