import urllib2
import os
response=''
try:
    request = urllib2.Request('localhost:9200')
    response = urllib2.urlopen(request)
except:
    print 'faild '

if "200" in str(response.getcode()):
    print 'ok'

else:
    os.system("docker-compose stop;docker rm $(docker ps -a -q);docker rmi $(docker images -q);docker-compose up -d;")
