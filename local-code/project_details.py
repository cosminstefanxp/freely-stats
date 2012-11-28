
class Project_details:
    def __init__(self, id, name, buyer_id, buyer_name, buyer_country, state, short_descr, jobs, accepted_bidder_id, accepted_bidder_username):
        self.id = int(id)
        self.name = name
        self.buyer_id = int(buyer_id)
        self.buyer_name = buyer_name
        self.buyer_country = buyer_country
        self.state = state
        self.short_descr = short_descr

        self.jobs = jobs
        self.accepted_bidder_id = int(accepted_bidder_id)
      #  self.bidders = bidders  #no idea how to get them
        self.accepted_bidder_username = accepted_bidder_username
          
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["name"] = self.name
        out["buyer_id"] = self.buyer_id
        out["buyer_name"] = self.buyer_name
        out["buyer_country"] = self.buyer_country
        out["state"] = self.state
        out["short_descr"] = self.short_descr
        out["jobs"] = self.jobs
        out["accepted_bidder_id"] = self.accepted_bidder_id
        out["accepted_bidder_username"] = self.accepted_bidder_username
        return out
        
    def __str__(self):
        str = "%d || %s || %d"%(self.id, self.name, self.buyer_id)
        str = str + self.buyer_name + " || " + self.buyer_country + " || "+ self.state + " || " + self.short_descr
        return  str.encode('utf-8')
    

         
