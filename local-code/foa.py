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
            self.jobs[raw['id']] =  Job(job['id'], job['name'], job['projects_count'], job['seo_url'])
        return jobs
                     
    def writeJobsToFile(self, jobs, file_name = "jobs.json", type="json"):
        
        self.jobs = jobs
        file = open(file_name, "w")
        if(type == "json"):
            file.write(json.dumps([x.to_dict() for x in jobs], indent = 4))
        else:
            for job in self.jobs:
                file.write("%s, %s, %d, %s\n"%(job.id, job.name, job.projects_count, job.seo_url))
        file.close()
        
    def loadProjectsFromFile(self, file_name = "projects.json"):
        file = open(file_name, "r")
        #id nume nr_proiecte
        raw_projects = json.load(file)
        projects = {}
        for project in raw_projects:
            projects[project['id']] =  Job(project['id'], project['name'], project['start_date'], project['jobs'], project['bid_count'], project['avg_bid'])
        return projects
    
    def appendProjectsToCSVFile(self, projects, file_name = "projects.csv"):
        file = open(file_name, "a")
        for project in projects.values():
            file.write("%s, %s, %s, %s, %s, %s\n"%(project.id, project.name, project.start_date, project.jobs, project.bid_count, project.avg_bid))
        file.close();    
    
    def writeProjectsToFile(self, projects, file_name = "projects.json", type="json"):
        file = open(file_name, "w")
        if type == "json":
            file.write(json.dumps([x.to_dict() for x in projects.values()], indent = 4))
        else:
            for project in projects.values():
                file.write("%s, %s, %s, %s, %s, %s\n"%(project.id, project.name, project.start_date, project.jobs, project.bid_count, project.avg_bid))

        file.close()
        
    def loadUsersFromFile(self, file_name = "users.json"):
        print "TODO: "
    
    def writeUsersToFile(self, users, file_name = "users.json"):
        self.users = users
        file = open(file_name, "w")
        file.write(json.dumps([x.to_dict() for x in users], indent = 4))
        file.close()