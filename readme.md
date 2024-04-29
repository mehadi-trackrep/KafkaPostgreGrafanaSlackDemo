**Grafana to Slack integration:-**
 - At first, we have to create a Slack app with the targeted channel then we will get the incoming webhook URL.
 - Then in Grafana, enter the Alerting window. And then
  add the webhook url with the required information in the `Contact points`. Save & exit.
 - Now, add the `alert rules` for firing the alert in slack. It will be the DB query with our appropriate condition/expression & save with a folder.
 - Then finally, add the contact point in the `Notification policies`.
  
