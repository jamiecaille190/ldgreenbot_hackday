import json

class User:

    def __init__(self, name, points=0):
        self.name = name
        self.points = points
    
    def get_points(self):
        return self.points
    
    def get_name(self):
        return self.name
    
    def update_points(self, points):
        self.points = points
        return self.points

    def toJson(self):
        return json.dumps(self.__dict__)