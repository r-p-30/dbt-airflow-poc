FROM apache/airflow:3.1.0

COPY requirements.txt /requirements.txt
USER airflow

# Uninstall all existing Python packages except pip, setuptools, and wheel
RUN pip freeze | grep -v "pip==" | grep -v "setuptools==" | grep -v "wheel==" | xargs pip uninstall -y && \
    pip install --no-cache-dir --use-deprecated=legacy-resolver -r /requirements.txt
