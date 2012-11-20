
class Project:
    def __init__(self, id, name, start_date, end_date, buyer, state, shrt_descr, jobs, bid_count, avg_bid, seller, bidders):
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

        
    def to_dict(self):
        dict = []
        dict["id"] = self.id
        dict["name"] = self.name
        dict["start_date"] = self.start_date
        dict["end_date"] = self.end_date
        dict["buyer"] = self.buyer
        dict["state"] = self.state
        dict["shrt_descr"] = self.shrt_descr
        dict["jobs"] = self.jobs
        dict["bid_count"] = self.bid_count
        dict["avg_bid"] = self.avg_bid
        dict["seller"] = self.seller
        dict["bidders"] = self.bidders
        return dict
    

         