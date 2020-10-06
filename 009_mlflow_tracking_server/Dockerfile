# Defining base image
FROM python:3.8.2-slim

# Installing required Python libraries
RUN pip install PyMySQL==0.9.3 && \
    pip install psycopg2-binary==2.8.5 && \
    pip install mlflow[extras]==1.9.1

# Defining start up command
EXPOSE 5000
ENTRYPOINT ["mlflow", "server"]
