"""Get Variable"""
import logging  
from airflow.models import Variable   
my_var = Variable.get('var_name') 
logging.info(f'var_name value: {my_var}')
