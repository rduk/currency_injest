# currency_injest

Overview :
We have a model.py and currency_injest_9am.py files.
  Model = Setting up the sqlite table for storing the rates
  currency_injest_9am = WHich uses model and is suppose to run daily to get hold of daily rates
  
Instructions:
  pip3 install -r requirements.txt (to install dependancy)
  Run model.py once(for the first time) and this will store data of last 30 days so that we have atleast 30 days data when the system       initialize for the first time.
  Later on we can set up currency_injest_9am.py in a cron setup to run every day except weekends at 9.00AM : 0 9 * * 1-5
  
Deployment:
  As a one off, run model.py
    python model.py
  Cron tab setup to schedule currency_injest_9am on weekdays
    0 9 * * 1-5 currency_injest_9am.py
    
  To monitor we can use standard MAILTO= function. If a cronjob produces output on STDERR, it will be mailed to the address we choose

Alternative to scheduling and monitoring this tas.
  We could very well use <b>celery/rabbitMQ</b> to schedule this whole task on daily basis by making use of <b>CeleryBeats</b>.
  We can then use <b>Celery Flower</b> to monitor celery tasks and workers.
