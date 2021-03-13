# imports needed
import pandas as pd
import numpy as np

from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
def get_zillow_data():
    '''
    This function uses the SQL query from below and specifies the database to use
    '''
    # SQL query that joins all of the tables together from the 'telco_churn' database     
    sql_query = """
                SELECT * 
                FROM properties_2017
                JOIN predictions_2017 USING(parcelid)
                WHERE transactiondate BETWEEN "2017-05-01" AND "2017-06-30";
                """
    return pd.read_sql(sql_query,get_connection('zillow'))