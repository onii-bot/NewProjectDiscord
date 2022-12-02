import requests
import json
import time
import os

channel_id = 906249210398126120
url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
payload = {'content': 'test'}
header = {
  'authorization':
  os.environ["token"]
}

prev_id = 0
i = 0
while 1:
  print(f"Checking Now , times checked {i}")
  messages = requests.get(url, headers=header).content
  messages = json.loads(messages)
  new_id = messages[0]['id']
  if prev_id != new_id:
    payload = {'content':f'@everyone {messages[0]["content"]}'}
    requests.post("https://discord.com/api/v9/channels/744107902587109401/messages",data=payload,headers=header)
    prev_id = new_id
  i = i + 1
  time.sleep(1200)
  
