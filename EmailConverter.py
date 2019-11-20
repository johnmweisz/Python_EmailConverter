import mailbox
import csv
from datetime import datetime
from email.header import decode_header, make_header

writer = csv.writer(open("Converted.csv", "w"))
emails = {}

# Optional table header
# writer.writerow(["Date", "From", "Subject"])

for message in mailbox.mbox('mail.mbox'):
    if not message['from'] in emails:
        try:
            datetime.strptime(message['date'][:-6], '%a, %d %b %Y %X').strftime('%x %X')
        except:
            Date = message['date']
        else:
            Date = datetime.strptime(message['date'][:-6], '%a, %d %b %Y %X').strftime('%x %X')
        try:
            make_header(decode_header(message['subject']))
        except:
            Subject = message['subject']
        else:
            Subject = make_header(decode_header(message['subject']))
        try:
            make_header(decode_header(message['from']))
        except:
            From = message['from']
        else:
            From = make_header(decode_header(message['from']))
        
        writer.writerow([Date, From, Subject])

        emails[str(message['from'])] = 1