# Elk_REDIS_Docker_Compose
## Prerequisite For Ubuntu 16.04
## Insall Docker && Docker Compose
###### sudo -i
###### wget -qO- https://get.docker.com/ | sh
###### sudo usermod -aG docker $(whoami)
###### apt-get -y install python-pip
###### pip install docker-compose
## Insall GIT
###### apt-get update
###### apt-get install git-core
###### git --version
## Now Clone  the Project
###### git clone https://github.com/robert456456456456/Elk_REDIS_Docker_Compose.git
###### cd Elk_REDIS_Docker_Compose
###### docker-compose build
##### run (daemon)
###### docker-compose up -d
##### show logs
###### docker-compose logs
## Now
#### Then navigate on http://localhost:9200
### How would you monitor the health of the services?


