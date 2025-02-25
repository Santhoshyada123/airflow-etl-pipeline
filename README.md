# airflow-etl-pipeline
An Apache Airflow-based ETL pipeline for processing toll data. This project involves extracting, transforming, and loading data from various file formats (CSV, TSV, Fixed Width) into a consolidated dataset for further analysis

# Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Airflow. The pipeline processes toll data, performing a series of data extraction and transformation tasks on various file formats (CSV, TSV, and Fixed Width). The final output is a consolidated CSV file containing all necessary data, followed by a transformation to clean up and standardize the data. The entire pipeline is orchestrated with Apache Airflow, which ensures smooth automation and execution of tasks.
# Key Tasks in the Pipeline
1)Unzipping Data: Unzips the raw data files from a compressed archive.

2)Extracting Data from CSV: Extracts specific fields from the vehicle-data.csv file and stores them in a new CSV file.

3)Extracting Data from TSV: Extracts specific fields from the tollplaza-data.tsv file and saves them as tsv_data.csv.

4)Extracting Data from Fixed Width: Extracts specific fields from the payment-data.txt file and stores them in a new CSV file.

5)Consolidating Data: Combines all extracted data (from CSV, TSV, and Fixed Width files) into one consolidated CSV file.

6)Transforming Data: Transforms the data (converts the vehicle type to capital letters) and stores it in a new file called transformed_data.csv.
The pipeline is built using BashOperator for each task, which runs bash commands to handle file manipulations such as unzipping, extracting, merging, and transforming data.

# Installation & Setup
**Prerequisites**

Before running this pipeline, ensure the following:

1)Apache Airflow is installed and configured.

2)Python 3.x is installed on your system.

3)You have access to the necessary datasets (vehicle-data.csv, tollplaza-data.tsv, payment-data.txt).
URL: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz

# Setting Up Apache Airflow
1)Install Apache Airflow using pip:

  bash command :pip install apache-airflow
2) Set up the Airflow database:

bash command :airflow db init
3)Create a folder structure for your DAG:Create a folder structure for storing your data and DAGs (Directed Acyclic Graphs). Example: ~/airflow/dags/finalassignment/staging with any directory path based on your environment.

4)Place the raw data files in the directory: After setting up your directory, you will need to place your raw data files (such as CSVs, TSVs, etc.) into the folder you just created, like ~/airflow/dags/finalassignment/staging/.

# Task Overview

1)The tasks in the DAG are designed as per the steps described in the assignment:

2)Unzip Data: The unzip_data task unzips the downloaded data using tar.

3)Extract Data from CSV: The extract_data_from_csv task extracts the necessary fields from vehicle-data.csv.

4)Extract Data from TSV: The extract_data_from_tsv task extracts data from tollplaza-data.tsv.

5)Extract Data from Fixed Width: The extract_data_from_fixed_width task extracts data from payment-data.txt.

6)Consolidate Data: The consolidate_data task merges the fields from the extracted CSV, TSV, and fixed-width files.

7)Transform Data: The transform_data task converts the vehicle_type column to uppercase.


  








