
class Project:
    def __init__(self, id, name, start_date, end_date, buyer, state, shrt_descr, jobs, bid_count, avg_bid, seller, bidders, accepted_bidder):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.buyer = buyer
        self.state = state
        self.shrt_descr = shrt_descr
        self.jobs = jobs
        self.bid_count = bid_count
        self.avg_big = avg_bid
        self.seller = seller
        self.bidders = bidders  #no idea how to get them
        self.accepted_bidder = accepted_bidder
        
    def __init__(self, id, name, start_date, jobs, bid_count, avg_bid):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.jobs = jobs
        self.bid_count = bid_count
        self.avg_bid = avg_bid

        self.end_date = -1
        self.buyer = -1
        self.state = -1
        self.shrt_descr = ''
        self.seller = -1
        self.bidders = []
        self.accepted_bidder = -1
        
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["name"] = self.name
        out["start_date"] = self.start_date
        out["end_date"] = self.end_date
        out["buyer"] = self.buyer
        out["state"] = self.state
        out["shrt_descr"] = self.shrt_descr
        out["jobs"] = self.jobs
        out["bid_count"] = self.bid_count
        out["avg_bid"] = self.avg_bid
        out["seller"] = self.seller
        out["bidders"] = self.bidders
        out["accepted_bidder"] = self.accepted_bidder
        return out
        
    def __str__(self):
        return self.id + " || " + self.name + " || " + self.start_date + " || " + self.jobs + " || " + self.bid_count + " || " + self.avg_bid
    

         
