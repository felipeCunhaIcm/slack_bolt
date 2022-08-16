import logging
from os import environ

import slack
from app.controllers.menu import controller_message

from slack_bolt import App

token = environ['SLACK_TOKEN']
signing_secret = environ['ASSIG_SECRET']
msg_loading = environ['MESSAGE_LOADING']

app = App(token=token, signing_secret=signing_secret)

client = slack.WebClient(token=token)
BOT_ID = client.api_call("auth.test")["user_id"]

logging.basicConfig(level=logging.INFO)


@app.event('message')
def menu(body):
    try:
        event = body.get('event', {})
        logging.info(f"Evento: {event}")

        txt = str(event.get('text')).replace('*', '')
        logging.info(f"Texto: {txt}")

        ts = event.get('ts')
        user_id = event.get('user')
        _channel = event.get('channel')

        users_info = client.users_info(user=user_id)
        mail = users_info['user']['profile']['email']

        logging.info(f"user_id: {user_id} | mail: {mail}")

        if user_id != BOT_ID:
            client.chat_postMessage(channel=_channel, thread_ts=ts, text=msg_loading.replace(
                'bot-name', environ['BOT_NAME']))
            txt_return = controller_message(txt, mail, user_id)
            del txt
            client.chat_postMessage(channel=user_id, text=txt_return)
            del txt_return
            logging.info("Processo finalizado.")

    except Exception as error:
        logging.error(f'[menu] {error}')


if __name__ == "__main__":
    app.start(8000)  # POST http://localhost:8000/slack/events
