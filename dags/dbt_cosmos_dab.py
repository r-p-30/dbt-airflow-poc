from airflow import DAG
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime

with DAG(
    dag_id="dbt_cosmos_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    dbt_tg = DbtTaskGroup(
        group_id="dbt_models",
        project_config=ProjectConfig("/usr/local/airflow/dbt/etl_demo"),
        profile_config=ProfileConfig(
            profile_name="default",
            profiles_yml_filepath="/usr/local/airflow/dbt/etl_demo/profiles.yml"
        ),
        execution_config=ExecutionConfig(
            dbt_executable_path="/usr/local/airflow/dbt_venv/bin/dbt",
        ),
    )

    dbt_tg

