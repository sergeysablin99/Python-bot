import ast
import json


class User:
    events = dict()

    def __init__(self, events=None):
        if events is None:
            events = {}
        self.events = events

    def get_event(self, date):
        return self.events.get(date)


class UserList:
    all_users = dict()  # Contains dict(user_id, User)
    data_dir = ''

    def __init__(self, data_dir="./data/base.json"):
        self.data_dir = data_dir
        f = open(data_dir, 'r')
        if f.seek(0, 0):
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
        f = open(self.data_dir, 'r')
        old_users = f.read()
        if old_users:
            old_users = ast.literal_eval(old_users)
        else:
            old_users = dict()
        f.close()
        new_users = self.all_users
        for user in old_users:
            if user not in self.all_users:
                new_users[user] = old_users[user]
            else:
                # new_users[user] = dict(old_users[user]).update(dict(self.all_users[user]))
                new_users[user] = {**old_users[user], **self.all_users[user]}
                print(new_users)
        f = open(self.data_dir, 'w')
        if not new_users == {}:
            f.write(json.dumps(new_users))
        f.close()
