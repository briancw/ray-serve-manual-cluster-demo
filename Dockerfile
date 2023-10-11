###
# Dockerfile for a Ray Head server
###

FROM ubuntu:22.04

# Baseline Update and tools
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl git build-essential

# Install Python
RUN apt-get install -y python3 python3-pip python3-venv

# Python Deps
RUN pip3 install -U pip setuptools --no-cache-dir

# Install Ray
RUN pip3 install ray[default] --no-cache-dir --index-url http://10.0.1.71:5000/index  --trusted-host 10.0.1.71
