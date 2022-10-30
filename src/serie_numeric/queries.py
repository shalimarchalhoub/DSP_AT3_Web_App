def get_negative_number_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_negative_number_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has negative values 

    --------------------
    Parameters
    --------------------
    pass
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    pass
    -> pseudo-code

    --------------------
    Returns
    --------------------
    pass
    -> (type): description

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
    pass
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    pass
    -> pseudo-code

    --------------------
    Returns
    --------------------
    pass
    -> (type): description

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
    pass
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    pass
    -> pseudo-code

    --------------------
    Returns
    --------------------
    pass
    -> (type): description

    """
    return f'select distinct {col_name} from {schema_name}.{table_name}'
