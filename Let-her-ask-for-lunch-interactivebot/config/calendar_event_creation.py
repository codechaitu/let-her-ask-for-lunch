
DEFAULT_MEMBER = 'codechaitu@mercari.com'
HELLO_MESSAGE_EN = "Hello, I am codechaitu's assistant. Chaitu says, "
HELLO_MESSAGE_JP = "こんにちは、私はcodechaituのアシスタントです。"

CALENDAR_EVENT = {
    "lunch": {
        "name": "LUNCH",
        "message": HELLO_MESSAGE_EN + " Hey, it's been long time we went for lunch, looking forward to see you soon...\n "
                                 + " 久しぶり ですね、いつか一緒にランチしようよ。。。",
        "attachmentText": "Is it ok tomorrow from 13:00 to 14:00 ?",

        # These are for calendar invition details
        "startTime": "T13:00:00+09:00",
        "endTime": "T14:00:00+09:00",
        "summary": 'Chat with Chaitu - Lunch',
        "location": 'Will let you know in slack',
        "description": "Let's meet and have lunch",
    },
    "coffee": {
        "name": "COFFEE",
        "message": HELLO_MESSAGE_EN + " Hey, it's been long time we went for coffee, looking forward to see you soon...\n　"
                                 + " 久しぶり ですね, いつか一緒にコーヒしようよ。。。",
        "attachmentText": "Is it ok tomorrow from 17:30 to 18:00 ?",

        # These are for calendar invition details
        "startTime": "T17:30:00+09:00",
        "endTime": "T18:00:00+09:00",
        "summary": 'Chat with Chaitu - Coffee',
        "location": 'Will let you know in slack',
        "description": "Let's meet and have coffee",
    },
    "meet": {
        "name": "MEETING",
        "message": HELLO_MESSAGE_EN + " Hey, it's been long time we met, looking forward to see you soon...\n "
                                 + " 久しぶり ですね, 私はあなたに会いたいです",
        "attachmentText": "Is it ok tomorrow from 18:00 to 18:30 ?",

        # These are for calendar invition details
        "startTime": "T18:00:00+09:00",
        "endTime": "T18:30:00+09:00",
        "summary": 'Chat with Chaitu - Meeting',
        "location": 'Will let you know in slack',
        "description": "Let's meet and have some conversation",
    }
}
