## python学习笔记

### 安装python 虚拟环境

1. 安装python虚拟环境

```shell
sudo pip3 install virtualenv
```

2. 创建 venv环境

> --no-site-packages 表示不复制python环境中的第三方包， venv 新创建的环境

```shell
virtualenv --no-site-packages venv
```

3. 进入虚拟环境

```shell
source venv/bin/activate
```
这时候看到命令行前面 带有 虚拟环境的名字；如``(venv) Dale:Django long$`;

4. 在虚拟环境中安装Django

```shell
pip3 install Django
```
安装完成后，进入python3中，命令行直接 `python3`，进入后在python中引入django， 'import django';

5. 创建应用

```shell
python3 manage.py stsrtapp admin
```
这时候就可以在文件家中看到创建了一个 为admin的文件目录；

6. 退出当前虚拟环境

```shell
deactivate
```


## 数据库

1. 创建用户
```shell
python manage.py createsuperuser
```

## json数据

1. [django数据转换成json的三种方法](https://blog.csdn.net/weixin_34234721/article/details/93078899)

2. [Python http请求方法](https://www.jianshu.com/p/9a9dd097d282)
