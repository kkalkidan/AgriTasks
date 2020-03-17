# Dockerizing Flask

## A How to run guide 

### requirements:
- Docker needs to be installed

### Steps 

```
# builds the docker image, also removes intermediate containers 
docker build --name flask-app --rm . 

# run the docker image
docker run -p 5000:5000 flask-image:latest

# to view the list of running containers
docker ps 

# to stop the container
docker stop <container name>

```

Go to http://0.0.0.0:5000/ to check if the app is correctly running. 

> author: Kalkidan Fekadu