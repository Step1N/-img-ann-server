#!/bin/bash

# Build docker image
docker build -f Dockerfile -t img_ann_server:latest .

#Run docker 
docker run -d -p 5000:5000 img_ann_server:latest

#Check Default API
curl --request GET --url http://localhost:5000/monitor/health
