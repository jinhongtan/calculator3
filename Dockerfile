# ����python����
FROM python:3.7

# ������Ϣ
MAINTAINER jinhongTan <https://github.com/jinhongtan/xxx.git>

# ����Ŀ¼
WORKDIR /code

# ����py�ļ���requirements.txt�ļ�
ADD . /code
# Ҳ��ʹ����������ʵ��
#COPY test.py /code/
#COPY requirements.txt /code/

# ����pip
RUN pip install --upgrade pip

# pip��װ������
RUN pip install -r requirements.txt

# ִ��python�ļ�
CMD ["python","/code/src/test.py"]
