import requests
import json
import datetime
import re
from user import UserList


class Server:
    group_id = 191177272
    access_token = 'access_token=f068c796542cba0f4dbdd0f6e39ba656a489731d36cfdcbdf7cee30de822ae000aa9e1aa8293bc61d77c7'
    v = 'v=5.103'  # Текущая версия VkAPI
    body = 'https://api.vk.com/method/'  # Тело запроса
    data = UserList()

    def __init__(self):
        self.server = str()
        self.key = str()
        self.ts = str()
        self.get_long_poll_server()

    def get_long_poll_server(self):
        method = 'groups.getLongPollServer?group_id=191177272'
        reply = requests.get("&".join([Server.body + method, Server.v, Server.access_token]))
        data = json.loads(reply.text)
        self.server = data['response']['server']
        self.key = data['response']['key']
        self.ts = data['response']['ts']

    def simple_request(self):
        method = self.server + '?act=a_check&key=' + self.key + '&ts=' + self.ts + "&wait=25"
        return requests.get(method)

    def simple_loop(self):
        reply = json.loads(self.simple_request().text)
        self.ts = reply['ts']
        if reply['updates']:
            message = reply['updates'][0]['object']['message']['text']
            if 'Напомни' in message:
                date = re.search('$d{2}-$d{2}-$d{4}', message)
                if str(date) != '':
                    message = str(message).replace('Напомни ', '').replace(str(date), '')
                else:
                    message = 'Не могу разобрать команду'
                    date = datetime.datetime.now().isoformat('|')
            else:
                message = 'Не могу разобрать команду'
                date = datetime.datetime.now().isoformat('|')
            user_id = reply['updates'][0]['object']['message']['from_id']
            self.data.add_rec(str(user_id), {date: message})
        self.simple_loop()


server = Server()
server.simple_loop()
