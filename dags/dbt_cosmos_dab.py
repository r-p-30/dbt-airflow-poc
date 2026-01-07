from airflow import DAG
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig
from datetime import datetime

with DAG(
    dag_id="dbt_cosmos_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    dbt_tg = DbtTaskGroup(
        group_id="dbt_models",
        project_config=ProjectConfig("/opt/airflow/dbt"),
        profile_config=ProfileConfig(
            profile_name="default",
            profiles_yml_filepath="/opt/airflow/dbt/profiles.yml"
        ),
    )

    dbt_tg

