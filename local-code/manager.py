import FreelanceOAuthClient
import Job

class Parser:
    def parseProjects(self, raw_data):
        print "TODO"
    def parseUsers(self, raw_data):
        print "TODO"
    def parseJobs(self, raw_data):
        print "TODO"
   
auth = FreelanceOAuthClient()  
parser = Parser()
resp = auth.send_request(url)
jobs = parser.parseJobs(resp)

