"""Get connections"""
import json 
import logging  
from airflow import DAG 
from airflow.models import Variable 
from airflow.hooks.base_hook import BaseHook 
from airflow.operators.python_operator import PythonOperator


def test(**kwargs):
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
    'test_vault_log',    
    start_date=datetime(2020, 1, 1),    
    schedule_interval=None
) as dag:      
    test_task = PythonOperator(         
        task_id='test-task',         
        python_callable=test,         
        op_kwargs={
            'my_conn_id': 'connection_to_test'
        },     
    )
