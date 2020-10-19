FROM python:3.8-alpine
WORKDIR /project

# loading envars in docker-compose.yml


####################### BOILERPLATE - pip installs whatever is in  requirements.txt ###############################
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo "pip-install requirements.txt done"
run echo "copying project files..."
######################## </> BOILERPLATE ############################################################

COPY . /project
CMD ["python", "main.py"]