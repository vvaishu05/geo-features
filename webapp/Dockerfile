# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
	binutils \
	libproj-dev \
	gdal-bin \
	&& rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /code/

# Expose the port that the app runs on
EXPOSE 8000

WORKDIR /code/geofeatures

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "geofeatures.wsgi:application"]
