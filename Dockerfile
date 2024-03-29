#this is my operating system
FROM ubuntu:22.04 
#this is copying all the files from the current directory to the container
# in a directory called app
COPY . /app

#this is the command to run when the container starts
#RUN python3 manage.py runserver

CMD echo "I am running a container!"