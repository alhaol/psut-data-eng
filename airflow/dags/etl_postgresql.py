
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from random import randint
from datetime import datetime
import subprocess


from sqlalchemy import create_engine
import psycopg2
import pandas as pd


host="172.26.0.2" # use, 172.26.0.2, "localhost" if you access from outside the localnet decompose env 
database="testDB"
user="me"
password="1234"
port='5432'
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
def _check_db_tables():
    print(engine.table_names())
   

def _read_table_as_DF():
    DF2=pd.read_sql("SELECT * FROM users2020 LIMIT 100;" , engine)
    print(DF2.head(10))

    
def _install_tools():
    try:
        from faker import Faker
    except:
        subprocess.check_call(['pip' ,'install', 'faker' ])
        from faker import Faker
    try:
        import psycopg2 
    except:
        subprocess.check_call(['pip' ,'install', 'psycopg2-binary' ])
        import psycopg2
        
    try:
        from sqlalchemy import create_engine
    except:
        subprocess.check_call(['pip' ,'install', 'sqlalchemy' ])
        from sqlalchemy import create_engine
        
        
    try:
        import pandas as pd 
    except:
        subprocess.check_call(['pip' ,'install', 'pandas' ])
        import pandas as pd 
        

with DAG("etl_postgresql", start_date=datetime(2021, 1, 1),
    schedule_interval="*/5 * * * *", catchup=False) as dag:

        install_tools = PythonOperator(
            task_id="install_tools",
            python_callable=_install_tools
        )

        check_db_tables = PythonOperator(
            task_id="check_db_tables",
            python_callable=_check_db_tables
        )

        read_table_as_DF = PythonOperator(
            task_id="read_table_as_DF",
            python_callable=_read_table_as_DF
        )

    

        install_tools >> check_db_tables >> read_table_as_DF
