# pull base image. When Docker runs, it runs Linux in the background. The application will run on Linux
FROM python:3.10-slim

# update the apt-get package manager.
RUN apt-get update

# install python3-dev and build-essential packages. These packages include developer kits. They are needed to install some of the Python packages.
RUN apt-get install python3-dev build-essential -y

# pip requirements
RUN pip install --upgrade pip # upgrade pip
# install virtualenv and create a virtual environment. /Opt is the directory where the virtual environment will be created. Venv is the name of the virtual environment.
RUN pip install virtualenv && python -m virtualenv /opt/venv

# set the PATH environment variable to include the virtual environment. This ensures that the Python packages installed in the virtual environment are used when the application is run. Actually, we defined a new path. This path is the path of the virtual environment we created. In this way, when we run the python command, it will search for python in the virtual environment.
ENV PATH="/opt/venv/bin:$PATH"

# copy the requirements.txt file to the /tmp directory in container. This file contains the Python packages that are needed to run the application. ./requirements.txt is the path to the requirements.txt file in the local directory. /tmp/requirements.txt is the path to the requirements.txt file in the container.
ADD ./requirements.txt /tmp/requirements.txt
# install the Python packages in the requirements.txt file.
RUN pip install -r /tmp/requirements.txt

# copy the application files to the /app directory in the container. All the application files are in the local directory(.), /srv/app is the path to the /srv/app directory in the container.
COPY . /srv/app

# set the working directory to /srv/app. This is the directory where the application files are located. All the commands that are run in the container will be run in this directory.
WORKDIR /srv/app


