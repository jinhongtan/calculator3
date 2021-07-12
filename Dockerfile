# 基于python镜像
FROM python:3.7

# 作者信息
MAINTAINER jinhongTan <https://github.com/jinhongtan/xxx.git>

# 工作目录
WORKDIR /code

# 拷贝py文件和requirements.txt文件
ADD . /code
# 也可使用以下两句实现
#COPY test.py /code/
#COPY requirements.txt /code/

# 更新pip
RUN pip install --upgrade pip

# pip安装依赖包
RUN pip install -r requirements.txt

# 执行python文件
CMD ["python","/code/src/test.py"]
