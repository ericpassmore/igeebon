#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

# following in JS
# new init empty state
# branch1 if URL has code=xxxxx then state=getting_token
# ###### NO CODE #######
# if no code then state=retreiving_token
# fetch teamsnap oauth token in memory
# if no oauth token then state=not_authorized
# if oauth token and not expired then state=authorized
# if oauth token and expired then state=not_authorized
# else state=undefined

# if state=not_authorized
# browser request auth.teamsnap/oauth/authorize
# redirect browser to user action login challenge and authorize link
# redirect back to page with code
# ###### HAS CODE ########
# python3 assemble URL POST with code
# return JSON and parse
# back to JS returned token, and fireoff webworker to store
# return webworker state=autorized
cgitb.enable()
print('Content-Type: text/html;charset=utf-8')

client_id="YjrnUX3JuquW6hWmBLRLYFipWlYuiWg6qDZayXr27xo"
redirect_uri="https%3A%2F%2Figeebon.com" # https://igeebon.com URL-encoded
response_type="code"
authorization_url="https://auth.teamsnap.com/oauth/authorize"
do_oauth_login_url="{AUTHORIZATION_URL}?client_id={CLIENT_ID}\
&redirect_uri={REDIRECT_URI}&response_type={RESPONSE_TYPE}".format(
    AUTHORIZATION_URL=authorization_url, CLIENT_ID=client_id,
    REDIRECT_URI=redirect_uri, RESPONSE_TYPE=response_type)

print()
print(do_oauth_login_url)


# POST ?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&redirect_uri=REDIRECT_URI&code=AUTHORIZATION_CODE&grant_type=authorization_code
token_url="https://auth.teamsnap.com/oauth/token"
client_secret="HwwQ1I690weAN_16pOmWCOleSLfbm2qZgL2Y3abauOo"
code=""
options="grant_type=authorization_code"


# response for OAUTH ACCESS token expires_in seconds
#{
#  "access_token": "e226c729934316851bcf568288c5573f60f190f5ee3900c1cc52e013ee313281",
#  "expires_in": 7200,
#  "scope": "read",
#  "token_type": "bearer"
#}
