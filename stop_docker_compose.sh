#!/usr/bin/env bash
docker-compose stop;docker rm $(docker ps -a -q);docker rmi $(docker images -q);