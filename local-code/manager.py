import web.FreelanceOAuthClient as freelance_auth
import job
import json
import foa as FileOA

class Parser:
    def parseProjects(self, raw_data):
        print "TODO"
    def parseUsers(self, raw_data):
        print "TODO"
    def parseJobs(self, raw_data):
       
        raw_json = json.loads(raw_data)
        raw_jobs = raw_json['json-result']['items']
        jobs = []
        for raw_job in raw_jobs:
           
            id = raw_job['id']
            name = raw_job['name']
            count = raw_job['project_count']
            jobs.append(job.Job(id, name, count))
        return jobs
   
auth = freelance_auth.FreelanceOAuthClient()  
parser = Parser()

url = "Job/getJobList.json"
resp = auth.send_request(url)
jobs = parser.parseJobs(resp)
sorted_jobs = sorted(jobs, key=lambda x: x.projects_count, reverse=True)

foa = FileOA.Foa()
foa.writeJobsToFile(jobs)