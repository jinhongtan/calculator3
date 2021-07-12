## 运行

#### 构建镜像
首先cd到Dockerfile所在目录

```shell
# 切换到Dockerfile所在目录
cd <Dockerfile_dir>
```

执行docker bulid命令

```shell
docker build -t mycalucator_py:v1
```

#### 执行镜像

```shell
docker run -it mycalucator_py:v1
```

