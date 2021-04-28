# Create db directory 
mkdir db  
docker-compose  up -d
# Mongo express on http://localhost:8081
# Mongo DB at  http://localhost:27017
# Minimal Jupyter LAB at http://localhost:8888

# To execute commands within mongo-db contanaier
docker exec -it mongo-db bash

# Access mongo-db contanaier logs
docker logs mongo-db

