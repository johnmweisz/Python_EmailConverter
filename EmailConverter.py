import mailbox
import csv
from datetime import datetime
from email.header import decode_header, make_header

# Creates new CSV file
writer = csv.writer(open("Converted.csv", "w"))

# Dictionary to store emails added
emails = {}

# Optional table header
# writer.writerow(["Date", "From", "Subject"])

# Loops through all messages in mbox file
for message in mailbox.mbox('mail2.mbox'):
    # Prevents duplicates
    if not str(message['from']).lower() in emails:
        # Date formatting
        sDate = str(message['date']).replace(',', '')
        dateArr = sDate.split()
        try:
            float(dateArr[0])
        except:
            dateArr = dateArr[:5]
            dateStr = " ".join(dateArr)
            try:
                datetime.strptime(dateStr, '%a %d %b %Y %X').strftime('%x %X')
            except:
                Date = dateStr
            else:
                Date = datetime.strptime(dateStr, '%a %d %b %Y %X').strftime('%x %X')
        else:
            dateArr = dateArr[:4]
            dateStr = " ".join(dateArr)
            try:
                datetime.strptime(dateStr, '%d %b %Y %X').strftime('%x %X')
            except:
                Date = dateStr
            else:
                Date = datetime.strptime(dateStr, '%d %b %Y %X').strftime('%x %X')

        # Handle encoded chars in Subject
        try:
            make_header(decode_header(str(message['subject'])))
        except:
            Subject = str(message['subject'])
        else:
            Subject = make_header(decode_header(str(message['subject'])))

        # Handle encoded chars in From Name
        try:
            make_header(decode_header(str(message['from']).replace('"', '')))
        except:
            From = str(message['from']).replace('"', '')
        else:
            From = make_header(decode_header(str(message['from']).replace('"', '')))
        
        # Write line to file
        writer.writerow([Date, From, Subject])

        # Add email to emails dictionary
        emails[str(message['from']).lower()] = 1