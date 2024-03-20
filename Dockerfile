# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR app

# Copy the current directory contents into the container at /app
COPY . .
RUN apt-get update
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir flask joblib scikit-learn numpy

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Run app.py when the container launches
ENTRYPOINT ["python3", "02-app.py"]

