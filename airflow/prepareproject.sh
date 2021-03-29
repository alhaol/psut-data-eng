curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'

mkdir dags logs plugins 

echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

docker-compose up airflow-init

docker-compose up

docker exec ID_webserver airflow version 

curl -X GET "http://localhost:8080/api/va/dags"

AIRFLOW_API_AUTH_BACKEND: 'airflow.api.auth.backend.basic_auth'

docker-compose up && docker-compose down 
