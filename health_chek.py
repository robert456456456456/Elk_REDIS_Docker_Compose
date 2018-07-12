import urllib2
import os
response=''
try:
    request = urllib2.Request('localhost:9200')
    response = urllib2.urlopen(request)
    print response.getcode()
except:
    print 'faild '

if response.getcode():
    print 'ok'

else:
    print 'inside else'
    os.system("docker-compose stop;docker rm $(docker ps -a -q);docker rmi $(docker images -q);docker-compose up -d;")
