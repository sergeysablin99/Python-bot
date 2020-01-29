import json

class User:
    events = dict()
    data_dir = ''

    def __init__(self, events=None):
        if events is None:
            events = {}
        self.events = events

    def get_event(self, date):
        return self.events.get(date)


class UserList:
    all_users = dict()  # Contains dict(user_id, User)

    def __init__(self, data_dir="./data/base.json"):
        self.data_dir = data_dir
        f = open(data_dir, 'r')
        for key, value in json.loads(f.read()).items():
            self.all_users[key] = User(value)
        f.close()

    def add_rec(self, user_id, user_events=None):
        if user_events is None:
            user_events = {}
        if self.all_users.get(user_id) is None:
            self.all_users[user_id] = user_events
        else:
            self.all_users[user_id] = {**self.all_users[user_id], **user_events}
        self.update_file()

    def update_file(self):
        f = open(self.data_dir, 'w')
        f.write(json.dumps(self.all_users))
        f.close()
