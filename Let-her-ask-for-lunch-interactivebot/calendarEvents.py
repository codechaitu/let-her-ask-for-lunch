from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from config.calendar_event_creation import *
import main
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def createEvent(service):
    tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    eventDetails = CALENDAR_EVENT[main.EVENT]
    startDateTime = tomorrow+eventDetails["startTime"]
    endDateTime = tomorrow+eventDetails["endTime"]

    event = {
        'summary': eventDetails['summary'],
        'location': eventDetails['location'],
        'description': eventDetails['description'],
        'start': {
            'dateTime': startDateTime,
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': endDateTime,
            'timeZone': 'Asia/Tokyo',
        },
        'attendees': [
            {'email': main.EMAIL},
            {'email': DEFAULT_MEMBER},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return(event.get('htmlLink'))


def bookCalendar():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    eventLink = createEvent(service)
    return eventLink



