
class User:
    def __init__(self, id, username, coutry, city, jobs):
        self.id = id
        self.username = username
        self.coutry = coutry
        self.city = city
        self.jobs = jobs            #user's skills
        
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["username"] = self.username
        out["country"] = self.coutry
        out["jobs"] = self.jobs
        return out
    

         