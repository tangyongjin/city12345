# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg wget git gcc libasound2-dev portaudio19-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get upgrade -y && apt-get install gcc libc6-dev -y --no-install-recommends --fix-missing

# Copy the requirements file first to take advantage of Docker layer caching
COPY requirements.txt ./
# COPY requirements2.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt
# RUN pip install --no-cache-dir -r requirements2.txt

# RUN pip install -r requirements2.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install torch

# Copy the current directory contents into the container at /app
# COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP server.py
ENV FLASK_RUN_HOST 0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run"]
