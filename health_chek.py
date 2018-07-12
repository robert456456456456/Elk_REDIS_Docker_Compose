import urllib2
import os
try:
    response = urllib2.urlopen('http://localhost:9200/')

    if response.code == 200:
        print 'ok'
    else:
        print 'inside else'
        os.system("docker-compose stop;docker rm $(docker ps -a -q);docker rmi $(docker images -q);docker-compose up -d;")
except:
    os.system("docker-compose stop;docker rm $(docker ps -a -q);docker rmi $(docker images -q);docker-compose up -d;")

