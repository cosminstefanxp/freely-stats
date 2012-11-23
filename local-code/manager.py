import web.FreelanceOAuthClient as freelance_auth
import job
import json
import foa as FileOA
import cgi
import urllib2
import project

class Parser:
    def parseProjects(self, raw_data):
        raw_json = json.loads(raw_data)
        raw_projects = raw_json['json-result']['items']
        projects = {}
        for raw_project in raw_projects:
            id = raw_project['projectid']
            name = raw_project['projectname']
            bids = raw_project['bids']
            avg_bid = raw_project['averagebid']
            jobtypecsv = raw_project['jobtypecsv']
            startdate = raw_project['startdate']
            #def __init__(self, id, name, start_date, end_date, 
            #buyer, state, shrt_descr, jobs, bid_count, avg_bid, 
            #seller, bidders, accepted_bidder):
            projects[id] = project.Project(id, name, startdate, jobtypecsv, bids, avg_bid)
        return projects
    
    def parseProjectDetails(self, raw_data):
        raw_json = json.loads(raw_data)
        
    def parseUsers(self, raw_data):
        print "TODO"
        
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

class Manager:
    def __init__(self):
        self.auth = freelance_auth.FreelanceOAuthClient() 
        self.parser = Parser()
        self.foa = FileOA.Foa()
        
    def write_jobs(self):
        url = "Job/getCategoryJobList.json"
        resp = self.auth.send_request(url)
        
        jobs = self.parser.parseAllCategories(resp)
        jobs.sort(key=lambda x: x.projects_count, reverse=True)
        self.foa.writeJobsToFile(jobs, file_name="jobs_in_all_categories.json")
        
        
        jobs = self.parser.parseMainCategories(resp)
        jobs.sort(key=lambda x: x.projects_count, reverse=True)
        self.foa.writeJobsToFile(jobs, file_name="jobs_in_main_categories.json")
        
        top_jobs = jobs[:100]
        self.foa.writeJobsToFile(top_jobs, file_name="jobs_TOP100_in_main_categories.json")
        
    def write_jobs_for_main_categories(self):
        url = "Job/getCategoryJobList.json"
        resp = self.auth.send_request(url)
        jobs = self.parser.parseMainCategories(resp)
        jobs.sort(key=lambda x: x.projects_count, reverse=True)
        top_jobs = jobs[:100]
        #self.foa.writeJobsToFile(top_jobs, file_name="jobs_TOP100_in_main_categories.json")
        
        print "finished getting top jobs..."
        top_job_names = [job.name for job in top_jobs]
     #   print top_job_names
        escaped_top_job_names = [urllib2.quote(job_name) for job_name in top_job_names]
        joined = ",".join(escaped_top_job_names)
        
        print "Joined job names" + joined + "\n\n\n\n\n"
        
        url = "Project/searchProjects.json?searchjobtypecsv="+joined
        resp = self.auth.send_request(url)
        
        print "\n"
        print resp
        projects = self.parser.parseProjects(resp)
        #print projects

manager = Manager()
#manager.write_jobs()
manager.write_jobs_for_main_categories()



'''
auth = freelance_auth.FreelanceOAuthClient()  
parser = Parser()
foa = FileOA.Foa()

# 1 2 4
#
url = "Job/getCategoryJobList.json"
resp = auth.send_request(url)

jobs = parser.parseAllCategories(resp)
jobs.sort(key=lambda x: x.projects_count, reverse=True)
foa.writeJobsToFile(jobs, file_name="jobs_in_all_categories.json")


jobs = parser.parseMainCategories(resp)
jobs.sort(key=lambda x: x.projects_count, reverse=True)
foa.writeJobsToFile(jobs, file_name="jobs_in_main_categories.json")

top_jobs = jobs[:100]
foa.writeJobsToFile(top_jobs, file_name="jobs_TOP100_in_main_categories.json")



top_job_names = [job.name for job in top_jobs]
print top_job_names
escaped_top_job_names = [urllib2.quote(job_name) for job_name in top_job_names]
joined = ",".join(escaped_top_job_names)

print joined + "\n\n\n\n\n\n\n\n"

url = "Project/searchProjects.json?searchjobtypecsv="+joined
resp = auth.send_request(url)
projects = parser.parseProjects(resp)
print projects
'''