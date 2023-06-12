 
# Import necessary libraries
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from model import PaddlePaddle
from translate import translate_to_sc as trans
import time
import random

# Create a Flask app instance
app = Flask(__name__)

# Set LINE channel access token and secret
LINE_CHANNEL_ACCESS_TOKEN='8uzlDY5sfT+sl80f+p1yTe4IlfHz2sHBFbncsULlbGxTebGYs4JJyCwN2K/k5aI7oxpJulOxQtSAD4sprjtTsfhnYrZuTcm8hve/f14ONVD/Xe8QrGrlHjgST+9JA8OKDLQGNX2aDQRafTS+zyw8xgdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET='e7a3ee921bce85f8a17db0ce9a2ba299'
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Create a route for the webhook
@app.route("/callback", methods=['POST'])
def callback():
    print("callbacked")
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print("signature get")

    # Get request body as text
    body = request.get_data(as_text=True)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):

    print("\n\nGet message from client:\n", event.message.text, "\n\n")
    user_input = trans(event.message.text)
    print("user input: "+ user_input)
    model = PaddlePaddle(worktype="classification")
    user_output_list = model.forward(user_input)

    #-------------------------------------------------------------
    """can only send one message"""
    # Send the same message back to the user
    # for message in user_output_list:
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=message)
    #     )
    #     time.sleep(random.uniform(1,5))
    #-------------------------------------------------------------

    #-------------------------------------------------------------
    """can send multiple messages, but simultaneously"""
    messages = []
    for message in user_output_list:
        messages.append(TextSendMessage(text=message))

    # Send multiple messages back to the user
    line_bot_api.reply_message(
        event.reply_token,
        messages
    )
    #-------------------------------------------------------------






if __name__ == "__main__":
    app.run()