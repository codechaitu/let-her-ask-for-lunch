from flask import Flask, request, make_response, render_template
import json
from config.slack_config import *
from calendarEvents import *
from slacker import Slacker

# Slack client for Web API requests
slack = Slacker(SLACK_API_TOKEN)

# Global values used, when we get response from requested user. bookCalendar needs these values. Assaiging default values
EVENT = "meet"
EMAIL = "pqr@tlm.com"
TO = ""

# Flask webserver for incoming traffic from Slack
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('event.html')



@app.route("/event", methods=['POST'])
def event():
    global EVENT
    global EMAIL
    global TO
    # TO = request.args['to']
    # EVENT = request.args['event']  # can be lunch, coffee or just a casual meeting
    TO = request.form['user_id']
    EVENT = request.form.get('event')
    userInfo = slack.users.info(TO)
    EMAIL = userInfo.body["user"]["profile"]["email"]
    eventDetails = CALENDAR_EVENT[EVENT]

    toMessageAttachment = [{
        "text": eventDetails["attachmentText"],
        "callback_id": "event_callback_id",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "actions": [
            {
                "name": eventDetails["name"],
                "text": "Yes",
                "type": "button",
                "value": "Yes"
            },
            {
                "name": eventDetails["name"],
                "text": "No",
                "type": "button",
                "value": "No"
            }

        ]
    }]
    slack.chat.post_message(channel=TO, text=eventDetails["message"], attachments=toMessageAttachment)

    return EVENT + " Requested, waiting for response"


@app.route("/slack/response", methods=["POST"])
def handleResponse():
    global TO
    global EVENT
    userInfo = slack.users.info(TO)
    # Parse the request payload
    form_json = json.loads(request.form["payload"])

    val = form_json["actions"][0]["value"]
    if val == "Yes":
        eventLink = bookCalendar()
        response_text_to_owner = CONFIRMATION_REPLY_YES + ", userInfo: " + str(userInfo.body["user"]["profile"]["real_name"]) + ", EVENT: "+str(EVENT)
        response_text_to_user = "Thank you. I made a calendar invitation."
    else:
        response_text_to_owner = CONFIRMATION_REPLY_NO + ", userInfo: " + str(userInfo.body["user"]["profile"]["real_name"]) + ", EVENT: "+str(EVENT)
        response_text_to_user = "Thank you. I will notify codechaitu about it."

    slack.chat.post_message(channel=CODE_OWNER, text=response_text_to_owner, attachments=[])

    return make_response(response_text_to_user, 200)


if __name__ == '__main__':
    app.run(debug=True)
