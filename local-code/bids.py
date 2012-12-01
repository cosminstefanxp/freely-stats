class Bid:
    def __init__(self, provider_userid, provider, bid_amount, descr, rating):
        self.provider_userid = provider_userid
        self.provider = provider
        self.bid_amount = bid_amount
        self.descr = descr
        self.rating = rating
        
    def to_dict(self):
        out = {}
        out["provider_userid"] = self.provider_userid
        out["provider"] = self.provider
        out["bid_amount"] = self.bid_amount
        out["descr"] = self.descr
        out["rating"] = self.rating
        return out