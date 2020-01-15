# External libraries
import pandas as pd
import sqlalchemy 
import pyodbc

# Credentials file
import credentials

db_driver = credentials.database_driver
db_server = credentials.database_server
db_port = credentials.database_port
db_username = credentials.username
db_password = credentials.password
db_database = credentials.database
sql_schema = credentials.schema
sql_table = credentials.table

connection_str = 'mssql+pyodbc://'+db_username+':'+db_password+'@'+db_server+','+db_port+'/'+db_database+'?driver='+db_driver
# Notes: 
# 
# 1. If no username and password is provided then defaults to "Trusted_Connection=yes"
# 
# 2. For our specific database, the port is defined by using a comma as a separator. This is more commonly denoted by a colon. 
#   If this is the case this connection string will need to be edited by replacing the comman with a colon.

engine = sqlalchemy.create_engine(connection_str)


dic={'Column 1':[10],'Column 2': [20]}
data = pd.DataFrame.from_dict(dic)

data.to_sql(name=sql_table,con=engine,schema=sql_schema,index=False,if_exists='replace')