
class User:
    def __init__(self, uid, username, country, city, jobs, rating, currency):
        self.id = int(uid)
        self.username = username
        self.country = country
        self.city = city
        self.jobs = jobs            #user's skills
        self.jobs_string = ",".join(jobs)
        self.rating = rating
        self.currency = currency
        
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["username"] = self.username
        out["country"] = self.country
        out["city"] = self.city
        out["jobs"] = self.jobs
        out["rating"] = self.rating
        out["currency"] = self.currency
        return out
    
    def __str__(self):
        return self.id + " || " + self.username + " || " + self.country + " || " + self.city + " || " + self.jobs_string + " || " + self.rating + " || " + self.currency
