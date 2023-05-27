We using the official MongoDB Docker image and exposing port 27017 for communication with the database. 
We're  creating a named volume called mongodb_data to persist the data across container restarts.
```
docker-compose up -d
```

Once the MongoDB container is up and running, you can connect to it from your Jupyter notebook or any other application using the following details:
```
Host: localhost
Port: 27017
Username: admin
Password: secret
```
You can modify these credentials in the docker-compose.yml file if needed.

```
python3 -m venv .venv
. .venv/bin/activate
!pip install pymongo
!pip install psycopg2
pip freeze > requirements.txt
```