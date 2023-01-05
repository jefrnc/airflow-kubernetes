"""Get Variable"""
import json 
import logging 
from datetime import datetime 
from airflow import DAG 
from airflow.models import Variable 
from airflow.hooks.base_hook import BaseHook 
from airflow.operators.python_operator import PythonOperator

def get_variable(**kwargs):
    my_var = Variable.get(kwargs['var_name']) 
    logging.info(f'var_name value: {my_var}')

with DAG(   
    'test_get_variable',    
    start_date=datetime(2020, 1, 1),    
    schedule_interval=None
) as dag:      
    test_task = PythonOperator(         
        task_id='test-get_variable',         
        python_callable=get_variable,         
        op_kwargs={
            'var_name': 'my_var',
        },     
    )
