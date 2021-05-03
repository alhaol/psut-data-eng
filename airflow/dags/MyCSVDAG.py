
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd
 
def CSVToJson():
    df=pd.read_csv('/opt/airflow/dags/data/data.csv')
    for i,r in df.iterrows():
        print(r['name'])
 
    df.to_json('/opt/airflow/dags/data/fromAirflow.json',orient='records')
 
 
default_args = {
 
    'owner': 'ibrahim1',
 
    'start_date': dt.datetime(2020, 3, 18),
 
    'retries': 1,
 
    'retry_delay': dt.timedelta(minutes=1),
}
 
with DAG('MyCSVDAG',
 
         default_args=default_args,
         schedule_interval=timedelta(minutes=1),  
        catchup=False,     
         ) as dag:
 
    print_starting = BashOperator(task_id='starting',
 
                     bash_command='echo "I am reading the       CSV now....."')
 
 
 
    CSVJson = PythonOperator(task_id='convertCSVtoJson',
 
                             python_callable=CSVToJson)
 
 
print_starting.set_downstream(CSVJson)
# or 
# CSVJson.set_upstream(print_starting)
 

print_starting >>  CSVJson
 
# or 
#CSVJson << print_starting
