#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import urllib.parse

cgitb.enable()
print('Content-Type: text/html;charset=utf-8')

# open teamsnap property file
# to-do url encode redirect_uri
teamsnap_props = {}
f = open("teamsnap.prop", "r")
for line in f:
    vars = line.split("=",1)
    # url encode callback url
    if vars[0] == "callback":
        teamsnap_props[vars[0]] = urllib.parse.quote(str.strip(vars[1]), safe="")
    else:
        teamsnap_props[vars[0]] = str.strip(vars[1])
f.close()


response_type="code"
authorization_url="https://auth.teamsnap.com/oauth/authorize"
do_oauth_login_url="{AUTHORIZATION_URL}?client_id={CLIENT_ID}\
&redirect_uri={REDIRECT_URI}&response_type={RESPONSE_TYPE}".format(
    AUTHORIZATION_URL=authorization_url,
    CLIENT_ID=teamsnap_props["client_id"],
    REDIRECT_URI=teamsnap_props["callback"],
    RESPONSE_TYPE=response_type)

print()
print(do_oauth_login_url)


# POST ?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&redirect_uri=REDIRECT_URI&code=AUTHORIZATION_CODE&grant_type=authorization_code
token_url="https://auth.teamsnap.com/oauth/token"
client_secret=teamsnap_props["client_secret"]
code=""
options="grant_type=authorization_code"


# response for OAUTH ACCESS token expires_in seconds
#{
#  "access_token": "e226c729934316851bcf568288c5573f60f190f5ee3900c1cc52e013ee313281",
#  "expires_in": 7200,
#  "scope": "read",
#  "token_type": "bearer"
#}
