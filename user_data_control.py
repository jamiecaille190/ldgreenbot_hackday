import json
from user import User

class UserDataContol:

    def __init__(self):
        self.user_data = {}
    
    def get_points_by_action(self, action):
        if action == "reduce_button":
            return 3
        elif action == "recycle_button":
            return 2
        elif action == "reuse_button":
            return 2
        return 0

    def add_points(self, name, points):
        if name in self.user_data:
            self.user_data[name].update_points(self.user_data[name].get_points() + points)
        else:
            self.user_data[name] = User(name, points)
        
        return self.user_data[name]

    def get_user(self, name):
        print(self.user_data)
        if name in self.user_data:
            return self.user_data[name]

        print("get_user: User {" + name + "} does not exists")

    def user_parser(self, payload):
        return User(payload["name"], payload["points"])
    
    def get_leaderboard(self):
        # returns a list of users sorted by points
        # i.e. [('Adam', 10),('Eve', 4),('Peeves', 2)...]
        return sorted(self.user_data.items(), key=lambda x: x[1].get_points())
    