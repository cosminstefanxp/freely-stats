
class User:
    def __init__(self, id, username, coutry, city, jobs, rating, currency):
        self.id = id
        self.username = username
        self.coutry = coutry
        self.city = city
        self.jobs = jobs            #user's skills
        self.rating = rating
        self.currency = currency
        
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["username"] = self.username
        out["country"] = self.coutry
        out["city"] = self.city
        out["jobs"] = self.jobs
        out["rating"] = self.rating
        out["currency"] = self.currency
        return out
    

         