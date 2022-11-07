
def get_tables_list_query():


    query=("""SELECT table_name
                 as table_name
                 FROM   information_schema.tables
                 WHERE table_schema != 'information_schema' AND
                 table_schema != 'pg_catalog'""")

    return query



def get_table_data_query(schema_name, table_name):

    query=("""select * from {0}.{1}""".format(schema_name,table_name))
    return query



def get_table_schema_query(schema_name, table_name):

    query=("""select c.table_name,c.column_name
          ,c.data_type,(case when k.COLUMN_NAME=c.column_name then c.column_name else '' end)  as primary_key
          , is_nullable,c.character_maximum_length,c.numeric_precision
            FROM
	        information_schema.columns as c inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as k  
	        on c.table_name=k.table_name
	        where c.table_name = '{1}' and c.table_schema='{0}'""".format(schema_name, table_name))
    return query
