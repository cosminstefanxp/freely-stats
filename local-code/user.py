
class User:
    def __init__(self, id, username, coutry, jobs):
        self.id = id
        self.username = username
        self.coutry = coutry
        self.jobs = jobs            #user's skills
        
    def to_dict(self):
        dict = []
        dict["id"] = self.id
        dict["username"] = self.username
        dict["country"] = self.coutry
        dict["jobs"] = self.jobs
        return dict
    

         