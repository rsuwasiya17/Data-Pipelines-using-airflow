# **Data Pipelines with Apache Airflow**

## Table of contents

* [Project Summary](#Project-Summary)
* [Project Description](#Project-Description)
* [Project Datasets](#Project-Datasets)
* [Files](#Dag-and-Operator-Files)
* [Pipeline](#Pipeline)

# Project Summary
Sparkify is a music streaming startup which has decided that it is time to introduce more automation and monitoring to their data warehouse ETL pipelines and come to the conclusion that the best tool to achieve this is Apache Airflow.

# **Project Description**
In these project we will create high grade data pipelines that are dynamic and built from reusable tasks, can be monitored, and allow easy backfills. The data quality plays a big part when analyses are executed on top the data warehouse and we have to run tests against their datasets after the ETL steps have been executed to catch any discrepancies in the datasets.
The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.

# **Project Datasets**
The data for this project is available on Amazon S3.
- Song data: s3://udacity-dend/song_data
- Log data: s3://udacity-dend/log_data

# **Dag and Operator Files**
- `udac_example_dag.py`

  Contains the tasks and dependencies of the DAG.

- `create_tables.sql`

  Contains the SQL queries used to create all the required tables in Redshift.

- `sql_queries.py`

  Contains the SQL queries used in the ETL process.

- `stage_redshift.py`

  Contains StageToRedshiftOperator, which copies JSON data from S3 to staging tables in the Redshift data warehouse.

- `load_dimension.py`

  Contains LoadDimensionOperator, which loads a dimension table from data in the staging tables.

- `load_fact.py`

  Contains LoadFactOperator, which loads a fact table from data in the staging tables.

- `data_quality.py`

  Contains DataQualityOperator, which runs a data quality check by passing an SQL query and expected result as arguments, failing if the results don't match.

# **Pipeline**
![ERD](images/dag.png)
