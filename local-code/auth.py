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
#import oauth2 as oauth
import urllib2
from urllib import urlopen

oauth_token        = 'f5b86bb1ab1390951ae016568af1afd7356dc044'
oauth_token_secret = 'c308401c010c8db91a4a3c05d57de17df8dcac30'

# key and secret granted by the service provider for this consumer application - same as the MockOAuthDataStore
consumer_key = 'a7b9bb9df9b80aff52f25507a27f64358ca9959c'
consumer_secret = 'a54ecf41c7627385dff3d68c8b80e973b7ae0fb4'



request_token_url = 'http://api.sandbox.freelancer.com/RequestRequestToken/requestRequestToken.json'
access_token_url = 'http://api.sandbox.freelancer.com/RequestAccessToken/requestAccessToken.json'
authorize_url = 'http://www.sandbox.freelancer.com/users/api-token/auth.php'

def init():    
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    client = oauth.Client(consumer)
    
    # Step 1: Get a request token. This is a temporary token that is used for 
    # having the user authorize an access token and to sign the request to obtain 
    # said access token.
    
    resp, content = client.request(request_token_url, "GET")
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
    print resp, content
    
    print "Access Token:"
    print "    - oauth_token        = %s" % access_token['oauth_token']
    print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
    print
    print "You may now access protected resources using the access tokens above." 
    print

def send_request(url):
    print "Will be implemented"
    #dummy method which gets a json or xml from the affiliate api, without oauth
    fis = urllib2.urlopen(url)
    data = fis.read()
    fis.close()
    print data
    out = file('fisier', 'w')
    out.write(data)
    out.close()
    return data

#send_request("http://api.freelancer.com/Project/Search.xml?jobs[]=PHP&jobs[]=XML&featured=1")