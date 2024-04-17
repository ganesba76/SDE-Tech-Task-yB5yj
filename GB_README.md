This project implements an ETL pipeline to extract data from the JSONPlaceholder API, carry out specified transformations, and load the data into a database for analysis. Additionally, SQL queries are provided to answer analysis questions based on the loaded data.

Introduction:

The ETL pipeline retrieves data from the JSONPlaceholder API, transforms it by parsing embedded JSON structures, adding a computed status field to posts, and combining posts with user details. The transformed data is then loaded 
into a database for further analysis.

Setup:
1. Cloning the shared repository:
2. Setting up & Activated the virtual environment.
3. Requirement.txt file holds the modules/environment required for executing in Vitual space.

Execution:
1) Run the ETL pipeline script to extract, transform, and load the data: "python main.py"
2) Verify that the data has been successfully loaded into the database.
3) Execute the requested SQL queries to perform analysis on the loaded data.

Assumptions:
1) The JSONPlaceholder API endpoints /posts and /users are assumed to be accessible and provide the required data.
2) The database (SQLite) used for loading the data is assumed to be configured and accessible.
3) For performing the sql challenge, have used MSSQL database & scripts are attached for table/index creation & select  statements. Syntax may differ for other database versions. 


Additional Information:
1) Unit tests for the ETL pipeline are available in the tests directory. Run them using a testing framework such as pytest.
2) Documentation for SQL schema creation and additional SQL queries can be found in the sql directory.
3) Ensure that the database schema matches the structure expected by the SQL queries.
4) Any relevant performance tuning tips & furture improvements documented in relevant sql files.

Improvements:

1) SQL improvements have been mentioned in the SQL files like table partitioning/ indexing / avoiding Btree.
2) We can validate the JSON document against a schema before processing & "JSON Schema library" can be used to perform it.

UAT:
1) Due to time constraint indepth & detailed UAT scripts are not created to perform it. UAT validated against simple data.
2) SQL script syntax may vary in different database versions.