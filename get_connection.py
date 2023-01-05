"""Get connections"""
import json 
import logging 
from datetime import datetime 
from airflow import DAG 
from airflow.models import Variable 
from airflow.hooks.base_hook import BaseHook 
from airflow.operators.python_operator import PythonOperator


def get_test_connection(**kwargs):
    # Test connections   
    conn = BaseHook.get_connection(kwargs['my_conn_id'])
    logging.info(     
        f'Login: {conn.login}'     
        f'Password: {conn.password}'     
        f'URI: {conn.get_uri()}'     
        f'Host: {conn.host}'     
        f'Extra: " {json.loads(conn.get_extra())}'   
        # ... 
    )

with DAG(   
    'test_connection',    
    start_date=datetime(2020, 1, 1),    
    schedule_interval=None
) as dag:      
    test_task = PythonOperator(         
        task_id='test_connection',         
        python_callable=get_test_connection,         
        op_kwargs={
            'my_conn_id': 'connection_to_test'
        },     
    )
