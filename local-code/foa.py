import job
import json

class Foa:
    def __init__(self):
        self.jobs = {}
        self.projects = {}
        self.users = {}
        self.bids = {}
    
    def loadJobsFromFile(self, file_name = "jobs.json"):
        file = open(file_name, "r")
        #id nume nr_proiecte
        jobs = json.load(file)
        for job in jobs:
            self.jobs[raw['id']] =  Job(job['id'], job['name'], job['projects_count'])
                     
    def writeJobsToFile(self, jobs, file_name = "jobs.json"):
        file = open(file_name, "w")
        file.write(json.dumps([x.to_dict() for x in jobs], indent = 4))
        file.close()
        
    def loadProjectsFromFile(self, file_name = "projects.json"):
        print "TODO: "
    
    def writeProjectsToFile(self, projects, file_name = "projects.json"):
        print "TODO: "
        
    def loadUsersFromFile(self, file_name = "users.json"):
        print "TODO: "
    
    def writeUsersToFile(self, users, file_name = "users.json"):
        print "TODO: "