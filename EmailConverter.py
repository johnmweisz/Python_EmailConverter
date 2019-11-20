import mailbox
import csv
from email.header import decode_header, make_header

writer = csv.writer(open("Converted.csv", "w"))
emails = {}

for message in mailbox.mbox('mail.mbox'):
    if not message['from'] in emails:
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
        
        writer.writerow([ message['date'], From, Subject ])

        emails[str(message['from'])] = 1