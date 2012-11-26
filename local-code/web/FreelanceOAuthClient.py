"""
The MIT License

Copyright (c) 2007 Leah Culver

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Example consumer. This is not recommended for production.
Instead, you'll want to create your own subclass of OAuthClient
or find one that works with your web framework.
"""
import urlparse
import oauth2 as oauth

# key and secret granted by the service provider for this consumer application - same as the MockOAuthDataStore
consumer_key = 'a929cb338bb38be7da3ee9d30c6db0a7705210f7'
consumer_secret = 'b43eba15bb402b6b4ede6cf369145b13a217719d'

# uri for obtaining the access tokens
request_token_url = 'http://api.freelancer.com/RequestRequestToken/requestRequestToken.json'
access_token_url = 'http://api.freelancer.com/RequestAccessToken/requestAccessToken.json'
authorize_url = 'http://www.freelancer.com/users/api-token/auth.php'

#uri for API
freelancer_com_api_url = 'http://api.freelancer.com/'

class FreelanceOAuthClient:
    '''Class that handles the calls to the Freelancer.com API'''

    # Main access tokens (cosminstefanxp)
    #oauth_token =           '7ce03cf8c8e89707b536db92dfa1a0ace75fc47b'
    #oauth_token_secret =    '23c34b616ae57180cb5f1869fc4fc856e943677f'
    
    # Secondary access tokens (uebmasterxp)
    oauth_token        = 'f6d0c73e4d7b628a335573e7bcca574e76b7e1a5'
    oauth_token_secret = 'f1c06993bad0be16558e4a17da67561a44f01c5c'
    
    def __init__(self):
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        token = oauth.Token(FreelanceOAuthClient.oauth_token, FreelanceOAuthClient.oauth_token_secret)
        self.client = oauth.Client(consumer, token)
        
    @staticmethod
    def load_oauth_token():    
        '''Loads a new oauth token'''
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        client = oauth.Client(consumer)
        
        # Step 1: Get a request token. This is a temporary token that is used for 
        # having the user authorize an access token and to sign the request to obtain 
        # said access token.
        
        resp, content = client.request(request_token_url, "GET")
        print resp 
        print content
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        
        request_token = dict(urlparse.parse_qsl(content))
        
        print "Request Token:"
        print "    - oauth_token        = %s" % request_token['oauth_token']
        print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
        print 
        
        # Step 2: Redirect to the provider. Since this is a CLI script we do not 
        # redirect. In a web application you would redirect the user to the URL
        # below.
        
        print "Go to the following link in your browser:"
        print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
        print 
        
        # After the user has granted access to you, the consumer, the provider will
        # redirect you to whatever URL you have told them to redirect to. You can 
        # usually define this in the oauth_callback argument as well.
        accepted = 'n'
        while accepted.lower() == 'n':
            accepted = raw_input('Have you authorized me? (y/n) ')
        oauth_verifier = raw_input('What is the PIN? ')
        
        # Step 3: Once the consumer has redirected the user back to the oauth_callback
        # URL you can request the access token the user has approved. You use the 
        # request token to sign this request. After this is done you throw away the
        # request token and use the access token returned. You should store this 
        # access token somewhere safe, like a database, for future use.
        token = oauth.Token(request_token['oauth_token'],
            request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)
        client = oauth.Client(consumer, token)
        
        resp, content = client.request(access_token_url, "POST")
        access_token = dict(urlparse.parse_qsl(content))
        FreelanceOAuthClient.oauth_token = access_token['oauth_token']
        FreelanceOAuthClient.oauth_token_secret = access_token['oauth_token_secret']

        
        print "Access Token:"
        print "    - oauth_token        = %s" % access_token['oauth_token']
        print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
        print
        print "You may now access protected resources using the access tokens above." 
        print
    
    
    def send_request(self, relative_url, method="GET"):    
        '''
        Makes a request to Freelancer.API to the given relative url. Handles the oAuth. 
        
        @return: the response received from server
        '''
        resp, content = self.client.request(freelancer_com_api_url + relative_url, method)
        print "[DEBUG] Fetch response for %s: %s" % (relative_url, resp['status'])
        return content
            
#FreelanceOAuthClient.load_oauth_token()   
#client = FreelanceOAuthClient()
#print client.send_request("Project/getBidsDetails.json?projectid=2792530")
#print client.send_request("Project/Properties.json?projectid=2792530")