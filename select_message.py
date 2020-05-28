class SelectMessage:
    """Constructs the select message for choosing reduce/recycle/reuse"""

    SELECT_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "How have you been green today?"
            ),
        },
    }

    BUTTON_ACTIONS = {
        "type": "actions",
        "block_id": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Reduce (3 points)"
                },
                "style": "primary",
                "value": "reduce_button",
                "action_id": "reduce_button_click"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Recycle (2 points)"
                },
                "style": "primary",
                "value": "recycle_button",
                "action_id": "recycle_button_click"
            },
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Reuse (2 points)"
                },
                "style": "primary",
                "value": "reuse_button",
                "action_id": "reuse_button_click"
            },
        ]
    }

    DIVIDER_BLOCK = {"type": "divider"}

    
    NOTGREEN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "I didn't do this! How can I be more Green"
            ),
        },
    }
    LEADER_BOARD = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "View Leaderboard"
            ),
        },
    }
    def __init__(self, channel):
        self.channel = channel
        self.username = "LDGreenBot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.SELECT_BLOCK,
                self.DIVIDER_BLOCK,
                self.BUTTON_ACTIONS,
                #self.DIVIDER_BLOCK,
                #self.NOTGREEN_BLOCK,
                #self.LEADER_BOARD
            ],
        }