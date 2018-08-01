from telethon.tl.functions.channels import GetParticipantsRequest

from time import sleep
from telethon import TelegramClient, events
import telethon.sync
api_id = 217790
api_hash ='b69bd04d4eb99526c6ca18157273dd01'
phone_number = '+998935770488'
client = TelegramClient('session_name', api_id, api_hash)
client.start()

@client.on(events.NewMessage)
def my_event_handler(event):
    if 'ping' in event.raw_text:
        client.send_message('spame_r', 'Pong!')
client.run_until_disconnected()

