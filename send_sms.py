#!/usr/bin/env python

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

import optparse
import sys
 
# Find these values at https://twilio.com/user/account
account_sid = "ACf847691632ddb462720f2a668f8dc73e"
auth_token = "8c8e6eb32ad9d87f9a38e84d1b24bea2"
client = TwilioRestClient(account_sid, auth_token)
 
parser = optparse.OptionParser()

parser.add_option('-u', '--sms_url',
    action="store", dest="sms_url",
    help="sms url string", default="spam")

options, args = parser.parse_args()

if options.sms_url == "spam":
  print "**** HEY! You forgot the URL for the SMS: ***"
  print "**** Usage: send_sms -u <URL_string> ***"
  sys.exit()

print '\n\n ************************ SENDING SMS WITH URL: ', options.sms_url ," *************************\n\n"

body_url = "Visitor @FrontDoor: " + options.sms_url
message = client.sms.messages.create(to="+919030059841", from_="+12018857211",
                                     body=body_url)