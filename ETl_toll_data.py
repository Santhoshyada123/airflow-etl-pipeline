from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Default arguments for the DAG
default_args = {
    'owner': 'Santhosh',
    'start_date': days_ago(0),
    'email': ['san@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# Task to unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment/staging',
    dag=dag,
)

# Task to extract data from CSV
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command="cut -d ',' -f 1,2,3,4 /home/project/airflow/dags/finalassignment/staging/vehicle-data.csv > \
    /home/project/airflow/dags/finalassignment/staging/csv_data.csv",
    dag=dag,
)

# Task to extract data from TSV
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -f 5,6,7 /home/project/airflow/dags/finalassignment/staging/tollplaza-data.tsv | tr '\t' ',' > \
    /home/project/airflow/dags/finalassignment/staging/tsv_data.csv",
    dag=dag,
)

# Task to extract data from fixed-width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="cut -c 11,12 /home/project/airflow/dags/finalassignment/staging/payment-data.txt | tr -s ' ' ',' > \
    /home/project/airflow/dags/finalassignment/staging/fixed_width_data.csv",
    dag=dag,
)

# Task to consolidate extracted data
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d ',' /home/project/airflow/dags/finalassignment/staging/csv_data.csv \
    /home/project/airflow/dags/finalassignment/staging/fixed_width_data.csv \
    /home/project/airflow/dags/finalassignment/staging/tsv_data.csv > \
    /home/project/airflow/dags/finalassignment/staging/extracted_data.csv",
    dag=dag,
)

# Task to transform data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="awk 'BEGIN {FS=OFS=\",\"} { $4 = toupper($4) }1' \
    /home/project/airflow/dags/finalassignment/staging/extracted_data.csv > \
    /home/project/airflow/dags/finalassignment/staging/transformed_data.csv",
    dag=dag,
)

# Task dependencies
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
