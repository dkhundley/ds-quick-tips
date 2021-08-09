# Starting with base image
FROM python:3.9-slim-buster

# Installing required packages from requirements.txt file
COPY dependencies/requirements.txt /
RUN pip install -r /requirements.txt

# Copying the FastAPI inference script and model
COPY container/ /container
COPY models/ /models

# Setting the working directory appropriately
WORKDIR /container

# Exposing the appropriate port on the container
EXPOSE 5001

# Setting the entrypoint for the container
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "5001", "api:api"]
