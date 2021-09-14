#!/usr/bin/env python3


import http.client
import json
import requests
import urllib.request, urllib.error, urllib.parse
import sys
import os
import re
import collections
import csv


conn = http.client.HTTPSConnection('petition.parliament.uk')


## Step 1 - download and store the category listings
# categories = ['20915','27','43','47456','12','7','47460','8','15741','11','26','42','13','17501','47692']
# for cat in categories:
#     url = "https://my.supplychain.nhs.uk/Catalogue/browse?sectionID={}&sortColumn=NCP&sortDescending=False&page=0&coreListRequest=BrowseAll&contractID=&pageSize=100".format(cat)
#     print(url)
#     outfile = "./cats1/{}.htm".format(cat)
#     response = urllib.request.urlopen(url)
#     with open(outfile, 'w') as output:
#         output.write(str(response.read()))


## Step2 - parse PLPs to get PDP URLs
# directory = os.getcwd() + '/cats1/'
# all = []
# for filename in os.listdir(directory):
#     #if filename == "20915.htm":
#     if os.path.isfile(os.path.join(directory, filename)):
#         with open(os.path.join(directory, filename), 'r') as f: 
#             links = re.findall("href=[\"\']\/Catalogue\/product\/([^comparison].*?)[\"\']", f.read())
#             all = all + links



headers = {'Content-type': 'pplication/x-www-form-urlencoded'}
signupId = 576886
auth_key = "fGkDeVfPra0y9Am1GJNp_MZIRkTQuaIQVApUMzJ4tNSdXVpMo2nZiqltz-1oOAiEtbcAxy0OpaLvDpaNoZPV_w"

data = {    
    "authenticity_token": auth_key,
    "signature[autocorrect_domain]": ???,
    "signature[uk_citizenship]": 1,
    "signature[name]": ????,
    "signature[email]": ????,
    "signature[location_code]": ????,
    "signature[postcode]": ????,
    "signature[notify_by_email]": 1
}

post_action = '/petitions/' + signupId + '/signatures/new'
conn.request('POST', post_action, data, headers)
response = conn.getresponse()
print(response.read().decode())

# url = "http://mock.kite.com/submitform"
# data = {"a": 1, "b": 2}
# print requests.post(url, data).text
#  Step 1 - get auth token (action="/petitions/576886/signatures/new")
#  Step 2 - inject token into form elements
#  Step 3 - post form 
# Form  - action="/petitions/576886/signatures/new"  method="post"
# Input - name="authenticity_token" value="fGkDeVfPra0y9Am1GJNp_MZIRkTQuaIQVApUMzJ4tNSdXVpMo2nZiqltz-1oOAiEtbcAxy0OpaLvDpaNoZPV_w"
# Input - name="signature[autocorrect_domain]" value="1" 
# Input - name="signature[uk_citizenship]" value="1"  
# Input - name="signature[name]" 
# Input - name="signature[email]"
# Input - name="signature[location_code]" value="GB"
# Input - name="signature[postcode]"
# Input - name="signature[notify_by_email]" value="1"
    