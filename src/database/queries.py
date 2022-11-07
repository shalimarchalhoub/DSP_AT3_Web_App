
def get_tables_list_query():
    """
        --------------------
        Description
        --------------------
        -> get_tables_list_query (method): Function that returns the query used for extracting the list of
        tables from a Postgres table

        --------------------
        Parameters
        --------------------
        ->query: type is str, it holds the query to be returned

        --------------------
        Pseudo-Code
        --------------------
        -> This code helps the function to return the query

        --------------------
        Returns
        --------------------
        ->type is str. query is returned

        """


    query=("""select table_name as table_name
                 from   information_schema.tables
                 where table_schema != 'information_schema' and
                 table_schema != 'pg_catalog'""")

    return query



def get_table_data_query(schema_name, table_name):
    """
        --------------------
        Description
        --------------------
        -> get_table_data_query (method): Function that returns the query used for extracting the content 
        of a Postgres table

        --------------------
        Parameters
        Parameters
        --------------------
        ->query: type is str, it holds the query to be returned

        --------------------
        Pseudo-Code
        --------------------
        -> This code helps the function to return the query

        --------------------
        Returns
        --------------------
        ->type is str. query is returned

        """

    query=("""select * from {0}.{1}""".format(schema_name,table_name))
    return query



def get_table_schema_query(schema_name, table_name):
    """
        --------------------
        Description
        --------------------
        -> get_table_schema_query (method): Function that returns the query used for extracting the list of
        columns from a Postgres table and their information

        --------------------
        Parameters
        --------------------
        ->query: type is str, it holds the query to be returned

        --------------------
        Pseudo-Code
        --------------------
        -> This code helps the function to return the query

        --------------------
        Returns
        --------------------
        ->type is str. query is returned

        """

    query=("""select c.table_name,c.column_name
          ,c.data_type,(case when k.COLUMN_NAME=c.column_name then c.column_name else '' end)  as primary_key
          , is_nullable,c.character_maximum_length,c.numeric_precision
            FROM
	        information_schema.columns as c inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as k  
	        on c.table_name=k.table_name
	        where c.table_name = '{1}' and c.table_schema='{0}'""".format(schema_name, table_name))
    return query
