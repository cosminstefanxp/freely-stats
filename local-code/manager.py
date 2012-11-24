import web.FreelanceOAuthClient as freelance_auth
import job
import json
import foa as FileOA
import cgi
import urllib2
import project
from distutils.file_util import copy_file

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
        
    def write_jobs_to_json(self):
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
        
    def write_jobs_to_csv(self):
        url = "Job/getCategoryJobList.json"
        resp = self.auth.send_request(url)
        
        jobs = self.parser.parseAllCategories(resp)
        jobs.sort(key=lambda x: x.projects_count, reverse=True)
        self.foa.writeJobsToFile(jobs, file_name="jobs_in_all_categories.csv", type="csv")
        
        
        jobs = self.parser.parseMainCategories(resp)
        jobs.sort(key=lambda x: x.projects_count, reverse=True)
        self.foa.writeJobsToFile(jobs, file_name="jobs_in_main_categories.csv", type="csv")
        
        top_jobs = jobs[:100]
        self.foa.writeJobsToFile(top_jobs, file_name="jobs_TOP100_in_main_categories.csv", type="csv")
        
    def write_projects_for_main_categories(self):
        url = "Job/getCategoryJobList.json"
        resp = self.auth.send_request(url)
        jobs = self.parser.parseMainCategories(resp)
        jobs.sort(key=lambda x: x.projects_count, reverse=True)
        top_jobs = jobs[:1]
        #self.foa.writeJobsToFile(top_jobs, file_name="jobs_TOP100_in_main_categories.json")
        
       # print "finished getting top jobs..."
        top_job_names = [job.name for job in top_jobs]
     #   print top_job_names
        escaped_top_job_names = [urllib2.quote(job_name) for job_name in top_job_names]
        joined = ",".join(escaped_top_job_names)
        
        #print "Joined job names" + joined + "\n\n\n\n\n"
        
        all_projects_in_season = {}
        for base in range(0,2000000,-200):
            for i in range(0, 200, -1):
                url = "Project/searchProjects.json?searchjobtypecsv="+joined+"&status=Closed&count=200&page=%d"%(i + base)
                resp = self.auth.send_request(url)
                #print "\n"
                # print resp
                projects = self.parser.parseProjects(resp)
                print "\tpage %d of %d"%(i + base, 2000000)
                   
                self.foa.appendProjectsToCSVFile(projects, file_name="spring_2012.csv")
            dest = "spring_2012_%d.csv"%(i + base)
            print "COPYING FILE spring_2012.csv to "+dest
            copy_file("spring_2012.csv", dest)
        #print projects
        

manager = Manager()
#manager.write_jobs_to_csv()
manager.write_projects_for_main_categories()


