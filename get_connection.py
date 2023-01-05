"""Get connections"""
import json 
import logging  
from airflow.hooks.base_hook import BaseHook   
conn = BaseHook.get_connection('secret_name') 
logging.info(     
    f'Login: {conn.login}'     
    f'Password: {conn.password}'     
    f'URI: {conn.get_uri()}'     
    f'Host: {conn.host}'     
    f'Extra: " {json.loads(conn.get_extra())}'   
    # ... 
)
