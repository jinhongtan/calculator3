# python images
FROM python:3.7

# author
MAINTAINER jinhongTan <https://github.com/jinhongtan/xxx.git>

# list
WORKDIR /code

# copy py file and requirements.txt file
ADD . /code
# Achieve based on below two method
#COPY test.py /code/
#COPY requirements.txt /code/

# update pip
RUN pip install --upgrade pip

# pip installation
RUN pip install -r requirements.txt

# run python
CMD ["python","/code/src/test.py"]