import json 
import bids
from bids import *
import project
import project_details
import job
import user
class Parser:
    def parseProjects(self, raw_data):
        raw_json = json.loads(raw_data)
        raw_projects = raw_json['json-result']['items']
        projects = {}
        flag = 0
        for raw_project in raw_projects:
            id = raw_project['projectid']
            name = raw_project['projectname']
            bids = raw_project['bids']
            avg_bid = raw_project['averagebid']
            jobtypecsv = raw_project['jobtypecsv']
            startdate = raw_project['startdate']
            if flag == 0:
                print "NEW" + startdate
                flag = 1
            #def __init__(self, id, name, start_date, end_date, 
            #buyer, state, shrt_descr, jobs, bid_count, avg_bid, 
            #seller, bidders, accepted_bidder):
            projects[id] = project.Project(id, name, startdate, jobtypecsv, bids, avg_bid)
        print "OLD " + startdate
        return projects
    
    def parseProjectDetails(self, raw_data):
        raw_json = json.loads(raw_data)
        
        details = raw_json['json-result']
        # print details
        if "count" in details:
            if details["count"] == 0:
                return None 
        seller_id = "-1"
        seller_username = " "
        if "seller" in details:
            for seller in details["seller"]:
                if seller["awardStatus"] == "awarded":
                    seller_id = seller["id"]
                    seller_username = seller["username"]
                #self, id, name, buyer_id, buyer_name, buyer_country, state, short_descr, jobs, accepted_bidder_id, accepted_bidder_username
        if "buyer" in details:  
            buyer_id = details["buyer"]["id"]
            buyer_username = details["buyer"]["username"]
        else:
            buyer_id = -1
            buyer_username = ""
            
        return project_details.Project_details(details["id"], details["name"], buyer_id, buyer_username, details["buyer"]["address"]["country"], details["state"], details["short_descr"],details["jobs"], seller_id, seller_username)
        
        
    def parseUsers(self, raw_data):
        #TODO:
        raw_json = json.loads(raw_data)
        if "user" not in raw_json:
            return None 
        city = ""
        country =""
        if "address" in raw_json["user"]:
            if "country" in raw_json["user"]["address"]:
                country = raw_json["user"]["address"]["country"]
            if "city" in raw_json["user"]["address"]:
                city = raw_json["user"]["address"]["city"]     
         #id, username, country, city, jobs, rating, currency):
        jobs = ";".join(raw_json["user"]["jobs"])
        return user.User(raw_json["user"]["id"], raw_json["user"]["username"], country, city, jobs, raw_json["user"]["rating"]["avg"], raw_json["user"]["currency"])
 
        
    def parseBids (self, raw_data):
        raw_json = json.loads(raw_data)
        if "count" in raw_json['json-result']:
            if raw_json['json-result']["count"] == 0:
                return None 
        raw_bids = raw_json['json-result']["items"]
        bids = {}
        for raw_bid in raw_bids:
        # provider_userid, provider, bid_amount, descr, rating):
            bid = Bid(raw_bid["provider_userid"], raw_bid["provider"], raw_bid["bid_amount"], raw_bid["descr"], raw_bid["rating"])
            bids[raw_bid["provider_userid"]] = bid
        return bids
        
    def parseAllCategories(self, raw_data):
        raw_json = json.loads(raw_data)
        raw_categories = raw_json['json-result']['items']["category"]
        jobs = []
        for raw_category in raw_categories:
            cat_id = raw_category["id"]
            print raw_category["id"],
            print "    " + raw_category['name'] 
            raw_jobs = raw_category["job"]
            for raw_job in raw_jobs:  
                print "\t",
                print  raw_job['name'],
                print "  ",
                print raw_job['project_count']            
                id = raw_job['id']
                name = raw_job['name']
                count = int(raw_job['project_count'])
                seo_url = raw_job['seo_url']
                jobs.append(job.Job(id, name, count, seo_url))
            print "\n\n"
        return jobs
    
    def parseMainCategories(self, raw_data):
        raw_json = json.loads(raw_data)
        raw_categories = raw_json['json-result']['items']["category"]
        jobs = []
        for raw_category in raw_categories:
            cat_id = raw_category["id"]
            print raw_category["id"],
            print "    " + raw_category['name'] 
            if cat_id == 1 or cat_id == 2 or cat_id == 4:
                raw_jobs = raw_category["job"]
                for raw_job in raw_jobs:  
                    print "\t",
                    print  raw_job['name'],
                    print "  ",
                    print raw_job['project_count']            
                    id = raw_job['id']
                    name = raw_job['name']
                    count = int(raw_job['project_count'])
                    seo_url = raw_job['seo_url']
                    jobs.append(job.Job(id, name, count, seo_url))
                    
            print "\n\n"
        return jobs