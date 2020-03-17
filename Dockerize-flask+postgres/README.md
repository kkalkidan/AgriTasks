# Dockerizing Flask and Postgres
## A How to run guide

### requirments 

- docker needs to be installed on the host machine

```
cd Dockerize-flask+postgres

# run docker-compose 
docker-compose up --build

```
- The docker compose create the services, in this case the `db` and `api`. It exposes ports for each service. Please read the `docker-compose.yml` the port number exposed by each container.
- Go to https:0.0.0.0:5000 to check if the api and db are correctly working
- Go to https:0.0.0.0:5000/accounts?{id} to create an account with the specified id number
- Go to https:0.0.0.0:5000/list_account to see the list of accounts in the database 
