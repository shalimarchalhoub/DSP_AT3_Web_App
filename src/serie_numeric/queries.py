def get_negative_number_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_negative_number_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has negative values 

    --------------------
    Parameters
    --------------------
    column from a Postgres table

    --------------------
    Pseudo-Code
    --------------------
    count the number of negative number from the table 

    --------------------
    Returns
    --------------------
    the number of negaive number(int)

    """
    return f'select count({col_name}) from {schema_name}.{table_name} where {col_name} < 0'

def get_std_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_std_query (method): Function that returns the query used for computing the standard deviation value of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    column from a Postgres table

    --------------------
    Pseudo-Code
    --------------------
    calculate the standard deviation from the table 

    --------------------
    Returns
    --------------------
    query that calulate the standard deviation(float)

    """
    return f'select std({col_name}) from {schema_name}.{table_name}'

def get_unique_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_unique_query (method): Function that returns the query used for computing the number of unique values of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    column from a Postgres table

    --------------------
    Pseudo-Code
    --------------------
    select all the distinct from the table 

    --------------------
    Returns
    --------------------
    query used for computing the number of unique values of a column from a Postgres table


    """
    return f'select distinct {col_name} from {schema_name}.{table_name}'
