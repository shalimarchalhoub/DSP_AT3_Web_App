def get_min_date_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_min_date_query (method): Function that returns the query used for 
    computing the earliest date of a datetime column from a Postgres table

    --------------------
    Parameters
    --------------------
    => schema_name = the schema name of the column we would like to take information from
    => table_name = the table name whose column we want to know more of
    => col_name (date) = the column name from database we want to know more of (which contains dates)

    --------------------
    Pseudo-Code
    --------------------
    => A function that is used to calculate the smallest date in the datetime column and returns that date

    --------------------
    Returns
    --------------------
    => query that contains the smallest date in the datetime column

    """
    query = "SELECT MIN(" + col_name + ") FROM " + schema_name + "." + table_name
    return query

def get_weekend_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_weekend_count_query (method): Function that returns the query used for computing the number of times a date of a datetime column falls during weekends

    --------------------
    Parameters
    --------------------
    => schema_name = the schema name of the column we would like to take information from
    => table_name = the table name whose column we want to know more of
    => col_name (date) = the column name from database we want to know more of (which contains dates)

    --------------------
    Pseudo-Code
    --------------------
    => A function that is used to calculate how many number of days in the dates are weekend

    --------------------
    Returns
    --------------------
    => query that contains the count of days in the dates falling on weekends

    """
    query = "SELECT count(*) FROM " + schema_name + "." + table_name + \
        " WHERE EXTRACT(dow FROM " + col_name + ") = 6 or EXTRACT(dow FROM " + col_name + ") = 0"

    return query

def get_1900_count_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    => get_1900_count_query (method): Function that returns the query used for computing the number of times a datetime column has the value '1900-01-01'

    --------------------
    Parameters
    --------------------
    => schema_name = the schema name of the column we would like to take information from
    => table_name = the table name whose column we want to know more of
    => col_name (date) = the column name from database we want to know more of (which contains dates)

    --------------------
    Pseudo-Code
    --------------------
    => The function that will return the query which will output the count of date equal to 01-01-1900 from a datetime column from a Postgres table

    --------------------
    Returns
    --------------------
    => the count of value in a datetime column which has the value equal to 01-01-1990

    """
    query = "SELECT COUNT(*) FROM " + schema_name + "." + table_name + \
            " WHERE " + col_name + "= '1900-01-01'"
    return query
