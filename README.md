# Collaborative Development of Database Explorer Web App

## :man_teacher: Authors
* Kai To MOK  
* Mahjabeen Mohiuddin  
* Phoebe Jacinda Santoso  
* Shalimar Chalhoub 

## :bookmark_tabs: Description
Our Group has been tasked to develop a containerised web application in Python that will explore the content of a database and analyse single tables. The application will be containarised with Docker and will run on Python 3.8.2.  
  
### Challenges Faced
 * Difficulties in finding comaptible packages
 * Trouble working remotely and collaborating
 * Discrepancy in coding style and parameter naming

 #### Solutions
The first problem was solved by constantly updating the requirements.txt file. As for the rest of the problems, constant communication and updates on the GitHub repository assisted in avoiding these conflicts.

### Future implementations
  
Future implementations of the project would include adding some prediction model that would be able to do prediction on given datasets

## :computer: How to Setup
The First step is to download Python and run version 3.8.2  as well as <code>streamlit
</code> via Pip


The Requirements for this project as listed below  
* Pandas 1.3.3
* Numpy 1.17.3
* Streamlit 0.89.0
* Altair 4.1.0

## :hammer_and_wrench: How to Run the Program

In order to run the code is to open the command Prompt and write the below command
```
docker run -p 8501:8051 -e PYTHONPATH="${PYTHONPATH}:/app" -it python_streamlit_app:latest
```
Next, open 
```
http://localhost:8501
```
And you will be able to see the app there and start using the various functions



### 📁 File Structure & Description

```
./
|
├── app/
│   └── streamlit_app.py            <- Python Code used to display the final application in the Docker Container
├── src/
│   ├── __init__.py                 <- turns src folder into a package for importing in main script
│   ├── config.py                   <- python script containing the code to configure the app
│   ├── Database/                 
│      ├── dsipaly.py               <- python script for displaying the menu to connect to a database
│      ├── logics.py                <- python script that manages the connection to a Postgres Databse
│      └── queries.py               <- python script for SQL queries related to the Database             
│   ├── Dataframe/               
│      ├── dsipaly.py               <- python script for displaying the overall information for a selected table
│      ├── logics.py                <- python script that manages the dataset loaded from Postgres
│      └── queries.py               <- python script for SQL queries related to the dataframe
│   ├── serie_date/
│      ├── dsipaly.py               <- python script for displaying information on all date/time columns
│      ├── logics.py                <- python script that manages date/time columns loaded from Postgres
│      └── queries.py               <- python script for SQL queries related to date columns
│   ├── serie_numeric/               
│      ├── dsipaly.py               <- python script for displaying information on all of the numeric columns
│      ├── logics.py                < -python script that manages numeric columns loaded from Postgres
│      └── queries.py               <- python script for SQL queries related to numeric columns
│   ├── serie_text/                
│      ├── dsipaly.py               <- python script for displaying information on all of the text columns
│      ├── logics.py                <- python script that manages text columns loaded from Postgres
│      └── queries.py               <- python script for SQL queries related to to text columns
|   ├──test
│      ├── test_database_logics.py      <- python script for testing code from Database/logics.py
│      ├── test_database_queries.py     <- python script for testing code from Database/queries.py
│      ├── test_dataframe_logics.py     <- python script for testing code from Dataframe/logics.py
│      ├── test_dataframe_queries.py    <- python script for testing code from Dataframe/queries.py
│      ├── test_serie_date_logics.py    <- python script for testing code from serie_date/logics.py
│      ├── test_serie_date_queries.py   <- python script for testing code from serie_date/queries.py
│      ├── test_serie_numeric_logics.py <- python script for testing code from serie_numeric/logics.py 
│      ├── test_serie_numeric_logics.py <- python script for testing code from serie_numeric/queries.py
│      ├── test_serie_text_queries.py   <- python script for testing code from serie_text/logics.py
│      └── test_serie_text_logics.py    <- python script for testing code from serie_text/queries.py          
│   
├── .gitignore                   <- avoids unecessary files pushed to the repository
├── Dockerfile                   <- file used to build a Docker image
├── README.md                    <- a markdown file containing student details, a description of this project and instructions for running the application
├── docker-compose.yml           <- a YAML file to configure the application's services
└── requirements.txt             <- a text file containing information on packages required to run the project
```


## Citations
* Student A: Kai To MOK -- 24586683  
* Student B: Mahjabeen Mohiuddin -- 24610507  
* Student C: Phoebe Jacinda Santoso -- 24600088  
* Student D: Shalimar Chalhoub -- 14071892
