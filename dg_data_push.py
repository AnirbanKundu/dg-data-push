import json
import os
import time
from random import randint
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

FILENAME = 'rasp1'
TAG = 'rasp1'
ingest_url = 'https://dg-ingest-service.run.aws-usw02-pr.ice.predix.io/ingest'
output = ''

cmd_out = os.popen('curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: Basic ZGlnaXRhbC1nYXJkZW46Y2hhbmdlbWU=" -H "Cache-Control: no-cache" -d "grant_type=client_credentials" "https://e97517f4-43d1-4263-9fd3-a16d67076d17.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token"').read()
response = json.loads(str(cmd_out))
access_token = response["access_token"]
print access_token

register_openers()


def push_file():
    with open(FILENAME, 'r') as ingest_file:
        datagen, headers = multipart_encode({"Authorization": "bearer" + access_token, "file": ingest_file, "routing-key": "data.ingestion.dg"})
        request = urllib2.Request(ingest_url, datagen, headers)
        res = urllib2.urlopen(request)
        print res


def write_to_file(data):
    with open(FILENAME, 'w') as fout:
        fout.write(data)


count = 1
while True:
    ts = time.time()
    m = randint(0, 100)
    h = randint(0, 100)
    l = randint(0, 100)
    output += str(ts) + ',' + TAG + ',' + str(m) + ',' + str(h) + ',' + str(l) + os.linesep
    if count >= 5:
        write_to_file(output)
        output = ''
        push_file()
        break
    count += 1
    time.sleep(1)


