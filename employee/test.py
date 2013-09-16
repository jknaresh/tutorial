'''
Created on May 21, 2012

@author: bfiegel
'''
import httplib2
import json
import sys
import requests

def post_thum(object_id,image_file):
    url = "http://127.0.0.1:8000/emp-thum/%s/" % (obj_id)
    files = {'thum': open(image_file, 'rb')}
    r = requests.post(url, files=files)
    print r.raw, r.text
    
if __name__=="__main__":
    if (len(sys.argv) < 2):
        print "Usage %s [object id] [image]"
        exit
    obj_id=sys.argv[1]
    image=sys.argv[2]
    post_thum(obj_id,image)