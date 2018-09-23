# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 01:56:28 2018

@author: sanooj
"""

"""
import http.client

conn = http.client.HTTPConnection("indigo.thoughtripples.com")

payload = \
"------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n"  + \
"Content-Disposition: form-data; name=\"description\"\r\n\r\n" + \
"\"description\"\r\n" + \
"------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
"Content-Disposition: form-data; name=\"heading\"\r\n\r\n" + \
"\"heading\"\r\n" + \
"------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
"Content-Disposition: form-data; name=\"file\"; filename=\"Far_Cry_5_boxshot.jpg\"\r\n" + \
"Content-Type: image/jpeg\r\n\r\n" + \
open ("Far_Cry_5_boxshot.jpg", 'rb').read () + \
"\r\n" + \
"------WebKitFormBoundary7MA4YWxkTrZu0gW--"

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "35c41afb-06a9-ccad-b8bc-57ed307468a7"
    }

conn.request("POST", "/api.php?api=send_message_ios&appid=51&phone1=9710522014", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8")) 

"""

import urllib3
import certifi

#pool Manager With Cetificate validationm
#https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl
http = urllib3.PoolManager(
        cert_reqs = 'CERT_REQUIRED',
        ca_certs=certifi.where()
        )

#GET request
def makeAGETRequest(http):
    
    get_request = http.request("GET", "http://httpbin.org/robots.txt")
    #print(get_request.data)
    print("status: %s" %(get_request.status))
    print("headers: %s" %(get_request.headers))


#POST w    
def makeAPOSTRequest(http):
   
    from urllib.parse import urlencode
    
    encoded_args = urlencode(
        {
                "name": "morpheus",
                "job": "leader"
         }
        )
    url = 'https://reqres.in//api/users?' + encoded_args
    post_request = http.request("POST", url)
    print("status: %s" %(post_request.status))
    print("headers: %s" %(post_request.headers))
    #print("data: %s" %(post_request.data))
    
#makeAPOSTRequest(http)

def makeAPOSTRequestForMultiPartFileUpload(http):
   
    encoded_body_args = urllib3.filepost.encode_multipart_formdata(
        {
                "description" : "description",
                "heading" : "heading",
                "file" : (
                        "Far_Cry_5_boxshot.jpg",
                        open("Far_Cry_5_boxshot.jpg", 'r').read()
                        )
         }
        )
    
    url = \
    "http://indigo.thoughtripples.com/api.php?" + \
    "api=send_message_ios" + \
    "&" + \
    "appid=51" + \
    "&" + \
    "phone1=9710522014"
    
    post_request = http.request(
            "POST", 
            url,
            body=encoded_body_args,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
    
    print("status: %s" %(post_request.status))
    print("headers: %s" %(post_request.headers))
    #print("data: %s" %(post_request.data))

#makeAPOSTRequestForMultiPartFileUpload(http)

 