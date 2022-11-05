def get_missing_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_missing_query (method): Function that returns the query used for computing the number of missing values of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    schema_name (str): Name of the dataset schema 
    table_name (str): Name of the dataset table 
    col_name (str): Name of the column 

    --------------------
    Pseudo-Code
    --------------------
    Gets the total number of columns where the values are null from the specific table in the schema

    --------------------
    Returns
    --------------------
    (SQL Query): SQL Query for total number of columns with missing data

    """
    return ("SELECT COUNT("+col_name+") FROM " + schema_name + "." + table_name + "WHERE" + col_name + "IS NULL;")

def get_mode_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_mode_query (method): Function that returns the query used for computing the mode value of a column from a Postgres table

    --------------------
    Parameters
    --------------------
    schema_name (str): Name of the dataset schema 
    table_name (str): Name of the dataset table 
    col_name (str): Name of the column 

    --------------------
    Pseudo-Code
    --------------------
    Group data by columns and order them then get the mode of each from the table within the schema

    --------------------
    Returns
    --------------------
    (SQL Query): SQL Query that computes the mode of a column


    """
    return ("SELECT MODE() WITHIN GROUP (ORDER BY " +col_name + ") AS mode FROM " + schema_name + "." + table_name + ";")

def get_alpha_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_alpha_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has only alphabetical characters

    --------------------
    Parameters
    --------------------
    schema_name (str): Name of the dataset schema 
    table_name (str): Name of the dataset table 
    col_name (str): Name of the column

    --------------------
    Pseudo-Code
    --------------------
    Get the total amount of columns from the table within the schema where the column entried only have alphabetical letters

    --------------------
    Returns
    --------------------
    (SQL Query): SQL Query for computing total amount of time a column has only alphabetical entries


    """
    return("SELECT COUNT(" + col_name + ") FROM " + schema_name+ "."+table_name + " WHERE" + col_name + " LIKE '%[a-zA-Z]%'")
