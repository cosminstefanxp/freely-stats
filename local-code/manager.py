import web.FreelanceOAuthClient as freelance_auth
import job
import json
import foa as FileOA
import cgi
import urllib2
import project
import project_details
import bids
from distutils.file_util import copy_file
import freelancer_parser
from freelancer_parser import *


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
        top_jobs = jobs[:100]
        #self.foa.writeJobsToFile(top_jobs, file_name="jobs_TOP100_in_main_categories.json")
        
       # print "finished getting top jobs..."
        top_job_names = [job.name for job in top_jobs]
     #   print top_job_names
        escaped_top_job_names = [urllib2.quote(job_name) for job_name in top_job_names]
        result = ",".join(escaped_top_job_names)
        
        #print "Joined job names" + result + "\n\n\n\n\n"
        
        all_projects_in_season = {}
        for base in range(0,2000000,200):
            for i in range(200):
                url = "Project/searchProjects.json?searchjobtypecsv="+result+"&status=Closed&count=200&page=%d"%(i + base)
                resp = self.auth.send_request(url)
                #print "\n"
                
                projects = self.parser.parseProjects(resp)
                print "\tpage %d of %d"%(i + base, 2000000)
                   
                self.foa.appendProjectsToCSVFile(projects, file_name="spring_2012.csv")
            dest = "spring_2012_%d.csv"%(i + base)
            print "COPYING FILE spring_2012.csv to "+dest
            copy_file("spring_2012.csv", dest)
        #print projects
        
    def write_projects_details(self, ids):
        print "project details"
        count = 0
        projects ={}
        for id in ids:
            if count < 0:
                count +=1
                continue
            url = "Project/getProjectDetails.json?projectid="+id
            resp = self.auth.send_request(url)
            print resp
            project = self.parser.parseProjectDetails(resp);
            if project:
                projects[project.id] = project
            count += 1
            if count % 10 == 0:
                self.foa.appendProjectsDetailsToCSVFile(projects, file_name = "full_projects_details.csv")
                projects = {}
            if count % 10 == 0:
                dest = "full_projects_details_%d.csv"%(count)
                copy_file("full_projects_details.csv", dest)
            print "%d of %d\n"%(count, len(ids))
        return projects

    
    
    def write_bids(self, ids):
        count = 0
        projects_bids ={}
        for id in ids:
            if count < 28830:
                count +=1
                continue
            url = "Project/getBidsDetails.json?projectid="+id
            resp = self.auth.send_request(url)
           # print resp
           
            bids = self.parser.parseBids(resp);
            if bids:
                projects_bids[id] = bids
            count += 1
            if count % 10 == 0:
                self.foa.appendBidsToCSVFile(projects_bids)
                projects_bids = {}
            if count % 1000 == 0:
                dest = "projects_bids_%d.csv"%(count)
                copy_file("projects_bids.csv", dest)
            print "%d of %d\n"%(count, len(ids))
        return projects_bids
    
    def write_user(self, ids):
        count = 0
        users ={}
        for id in ids:
            if count < 41380:
                count +=1
                continue
            val = int(id)
            url = "User/getUserDetails.json?userid=%d"%(val)
            resp = self.auth.send_request(url)
            #print resp
            
            user = self.parser.parseUsers(resp);
            if user:
                users[val] = user
            count += 1
            if count % 10 == 0:
                self.foa.appendUsersToCSVFile(users)
                users = {}
            if count % 1000 == 0:
                dest = "users_%d.csv"%(count)
                copy_file("users.csv", dest)
            print "%d of %d\n"%(count, len(ids))       
        return users
    
    
    def write_sellers(self, ids):
        count = 0
        sellers ={}
        for id in ids:
            if count < 29900:
                count +=1
                continue
            val = int(id)
            url = "User/getUserDetails.json?userid=%d"%(val)
            resp = self.auth.send_request(url)
           # print resp
            seller = self.parser.parseUsers(resp);
            if seller:
                sellers[val] = seller
            count += 1
            if count % 100 == 0:
                self.foa.appendUsersToCSVFile(sellers, file_name="sellers.csv")
                sellers = {}
            if count % 1000 == 0:
                dest = "sellers_%d.csv"%(count)
                copy_file("sellers.csv", dest)
            print "%d of %d\n"%(count, len(ids))
        self.foa.appendUsersToCSVFile(sellers, file_name="sellers.csv")
    
    def write_currency(self):
        url = "Common/getCurrencies.json"
        resp = self.auth.send_request(url)
        currencies = self.parser.parseCurrencies(resp)
        #print currencies
    
manager = Manager()
#manager.write_currency()


#details = manager.foa.loadProjectDetailsFromCSV("projects_details_uniq.csv")
#ids = [proj.buyer_id for proj in details.values()]
#manager.write_sellers(ids)




#manager.write_jobs_to_csv()
#manager.write_projects_for_main_categories()


#prj = manager.foa.loadProjectsFromCSVFile(file_name="spring_2012_599.csv")
#ids = []
#for elem in prj:
#    ids.append(prj[elem].id)
fin = open("project_ids", "r")
lines = fin.readlines()
lines = [line[:-1] for line in lines]
print lines
manager.write_projects_details(lines)
#manager.write_bids(ids)


'''
file = open("users.txt", "r")
ids = file.readlines();
file.close()
manager.write_user(ids)
'''

#manager = Manager()
##manager.write_jobs_to_csv()
##manager.write_projects_for_main_categories()
#prj = manager.foa.loadProjectsFromCSVFile(file_name="spring_2012_599.csv")
#ids = []
#for elem in prj:
#    ids.append(prj[elem].id)
#print ids[:3]
#manager.write_projects_details(ids)



