class EmailNotification:
    def send(self):
        print("Sending email notification")


class SMSNotification:
    def send(self):
        print("Sending SMS notification")


notifications = [EmailNotification(), SMSNotification()]

for notification in notifications:
    notification.send()