import web.FreelanceOAuthClient as freelance_auth
import job

class Parser:
    def parseProjects(self, raw_data):
        print "TODO"
    def parseUsers(self, raw_data):
        print "TODO"
    def parseJobs(self, raw_data):
        print "TODO" + raw_data
   
auth = freelance_auth.FreelanceOAuthClient()  
parser = Parser()

url = "Job/getJobList.json"
resp = auth.send_request(url)
jobs = parser.parseJobs(resp)

