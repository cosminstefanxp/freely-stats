
class ProjectDetails:
    def __init__(self, pid, name, buyer_id, buyer_name, buyer_country, state, short_descr, jobs, accepted_bidder_id, accepted_bidder_username, exchg):
        self.id = int(pid)
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
        self.exchg = exchg
          
    @staticmethod
    def fromCSV(csv_line):
        try:
            pid, name, buyer_id, buyer_name, buyer_country, state, description, jobs, accepted_bidder_id, accepted_bidder_username, exchg = csv_line.split(",", 11)
        except ValueError:
            print csv_line
            return None
        return ProjectDetails(pid, name, buyer_id, buyer_name, buyer_country, state, description, jobs, accepted_bidder_id, accepted_bidder_username, exchg)
       
          
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
        out = "%d || %s || %d" % (self.id, self.name, self.buyer_id) 
        out += " || " + self.buyer_name + " || " + self.buyer_country + " || " + self.state + " || " + self.short_descr
        out += " || " + str(self.accepted_bidder_id) + " || " + self.accepted_bidder_username
        return out.encode('utf-8')
    

         
