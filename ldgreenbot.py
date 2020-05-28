import os
import logging
import json
import requests
from flask import Flask, request
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from onboarding_tutorial import OnboardingTutorial
from select_message import SelectMessage
from user_data_control import UserDataContol
import ssl as ssl_lib
import certifi
from user import User

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)

USER_DATA = UserDataContol()

# Store the complete list of slack users here.
user_db = []

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

@slack_events_adapter.on("app_mention")
def send_select_message(payload):
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    select_message = SelectMessage(channel_id)

    message = select_message.get_message_payload()

    response = slack_web_client.chat_postMessage(**message)

    # ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.
@slack_events_adapter.on("team_join")

@app.route('/slack/action', methods=['POST'])
def update_score_and_respond():
    payload = json.loads(request.form.get('payload'))
    name = payload['user']['name']
    action = payload['actions'][0]['value']
    points_earned = USER_DATA.get_points_by_action(action)
    USER_DATA.add_points(name, points_earned)
    print(name + " just received " + str(points_earned) + " points!")

    response_url = payload['response_url']
    response_message = generate_response_message(name, points_earned)
    requests.post(response_url, generate_response_message(name, points_earned))

    return "success"

def generate_response_message(name, points_earned):
    response = {
        "replace_original": "true",
        "text": (name + " just earned " + str(points_earned) + " LD Green points! They now have " + str(USER_DATA.get_user(name).get_points()) + " points!")
    }
    return json.dumps(response)

# ============== Middleware ============= #
# Endpoints for frontend to call in order to obtain data

def formatLeaderboard(leaderboard):
    # leaderboad is a list of tuples [(name: str, point: int), (n, p)...]
    # this function will convert it into a list of objects
    # i.e. [{"name" : "John", "score" : 10}, {"name": "Pierre", "score": 5}...]
    lst = []
    for item in leaderboard:
        d = {"name" : item[0], "score" : item[1]}
        lst.append(d)
    return d

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    # JSONify leaderboard and ship it off
    # should look like

    output = {}
    return json.dumps(formatLeaderboard(USER_DATA.get_leaderboard()))


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(port=3000)