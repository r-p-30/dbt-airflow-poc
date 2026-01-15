FROM quay.io/astronomer/astro-runtime:12.6.0

# Install dbt-snowflake in a virtual environment to avoid dependency conflicts
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake==1.8.0 && deactivate