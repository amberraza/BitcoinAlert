# BitcoinAlert
Bitcoin price alert is sent to your phone whenever the price goes down the given threshold. The job is scheduled to run every hour. Following are the steps to send the alert:
  - Import the twilio Client class from twilio.rest module and BlockingScheduler class from apscheduler module.
  - Initialize the account id and authorization token given by twilio.
  - Get the current price via google search.
  - Initialize the client for the alert.
  - Check for the threshold value.
  - Send the alert to the given phone if the condition is met.
  - Schedule the job.
  - Start the scheduler.
