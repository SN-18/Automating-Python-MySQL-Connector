# CLI Package for Automating SQL Connction Using Python

## Connecting with MySql Server using Python 3.11
This package is meant to be used to connect connect with a MySQL server, start-up a default Schema for the user and to create a Table to work start-off with the server as a boiler-plate package.

## Installation MySQL
<ol>
  <li>
  To install MySQL, visit <a href="https://dev.mysql.com/downloads/installer/"> Official MySQL Documentation </a>:<br>
    <img width="1360" alt="Screenshot 2023-07-07 at 10 32 04 AM" src="https://github.com/SN-18/SQL_Python_Connector_Package/assets/83748468/9ef92dfb-a017-4ed0-a859-31e1db3cc6a2">
  </li>
  
  <li>
After installation is complete, go to the terminal to check if the installation was successfull:

Use the command: <br>

``` mysql --version ```

A successful output looks like the output below:

<img width="568" alt="Screenshot 2023-07-07 at 10 42 29 AM" src="https://github.com/SN-18/SQL_Python_Connector_Package/assets/83748468/365613d9-df94-4cab-a755-a3becec0df87">
    
  </li>
</ol>


## Running a Server

<ol>
  <li>
    In a terminal, use the command:

    ```mysql.server start```
    
  </li>

  <li>
    A successful Screen looks like the following output:
<br> <img width="567" alt="Screenshot 2023-07-07 at 10 51 30 AM" src="https://github.com/SN-18/SQL_Python_Connector_Package/assets/83748468/ac5c50e2-550c-4f45-96f4-e2f17d2575f3">
  </li>
  
  <li>
    To create a connection using the GUI, on mac for example, one can use System Preferences. Search for MySQL and use:
<br>
<img width="567" alt="Screenshot 2023-07-07 at 10 51 30 AM" src="https://github.com/SN-18/SQL_Python_Connector_Package/assets/83748468/4735e854-7051-48f5-ba87-566d02e21237">
    
  </li>

  
</ol>

## Checking if connection is active
<br>
Check the status of the connection via:
    ```
    
    mysql -u root -p
    
    ```

    When asked the password, enter the root password. This is the password that was used while setting up mySQL while installation in step 1. A succesful connection with it looks like:
    <br>
    <img width="567" alt="Screenshot 2023-07-07 at 10 51 30 AM" src="https://github.com/SN-18/SQL_Python_Connector_Package/assets/83748468/4735e854-7051-48f5-ba87-566d02e21237">
    

## Creating a Schema
This Python package creates a database, chooses a default schema, creates a table and establishes a connection for the user. It can be customised for a custom schema, but the hassle of creating and checking for the connection has been automated away.

Instead of creating the database, checking for the connection, and verify using GUI, simply run the python package by importing it as:

``` import python-starter ```

Run the python script as:

```python script_name arg1 arg2 arg3 ...```

The script creates a DB in absense of one, arguments are added to the schema, and then the user can enter the table enteries after being prompted to. This automates the hassle of doing this all from scratch.

##Dependencies
Use the following command in order to resolve any dependencies:

```pip install -r requirements.txt```

This will install all the dependencies on your virtual environment and would resolve any errors due to missing packages while setup.


