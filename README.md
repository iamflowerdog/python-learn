# python-learn
python

## Django 最简单 Demo

这是一个最简单的 Django demo，只用一个文件实现。

### 运行方法

```bash
# 激活虚拟环境（如果还没激活）
source .venv/bin/activate

# 运行 Django demo
python django_demo.py
```

然后在浏览器打开 `http://127.0.0.1:8000/` 即可看到 "Hello, Django!" 信息。

按 `Ctrl+C` 停止服务器。


## ubuntu 安装 pip `https://stackoverflow.com/questions/37495375/python-pip-install-throws-typeerror-unsupported-operand-types-for-retry`


```
apt-get remove python-pip python3-pip
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
python3 get-pip.py

```
1. 获取 get-pip.py 文件 `wget https://bootstrap.pypa.io/get-pip.py`
2. 下载文件后，通过 python 执行 `python get-pip.py`
3. 先安装python
     `如果执行失败，会提示你需要 Please use https://bootstrap.pypa.io/pip/2.7/get-pip.py instead `
     `这个报错的意思，就是告诉我们 根据本地机器的版本，去下载正确的 get-pip.py 文件, 然后重复执行步骤2 `

安装成功会提示 

```
Installing collected packages: pip
Successfully installed pip-20.3.4

```
测试是否安装成功 `pip --version`

## pip安装glances

1. `pip install glances` 
   此处可能会报error `ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.`
   解决办法: `使用国内的镜像源安装。在原来安装时在命令里加一个参数 -i，然后在i后面加国内镜像地址。` url: https://blog.csdn.net/zhangvalue/article/details/104271094
   有可能还会提示 timeout, 这个时候需要把timeout修改 `sudo pip install --default-timeout=100 future`
2. 成功后会提示 

  ```
  Installing collected packages: psutil, glances
  Successfully installed glances-3.1.6.2 psutil-5.8.0
  ```
3. 然后输入 glances 会显示GUI界面 (linux 下面需要切换成 root 权限)


## glances 安装folder plugin 用来监控 folder 遇到的问题

1. glances 的配置文件放到 `~/.config/glances/glances.conf`
2. 如果通过python运行的话，可能会看不到 folder 配置信息，需要我们通过 debug 来查看log
3. 通过 glances -V 查看 log输出的目录 `Log file: /home/pvc/.local/share/glances/glances.log`  
    然后 `sudo vim ~/.local/share/glances/glances.log ` 会看到 `Scandir not found. Please use Python 3.5+ or install the scandir lib`
4. 然后通过 pip 安装 scandir 插件 `pip install scandir`
5. 然后 输入 glances 可以看到 folder

## glances 查看 restful API 
1. glances -w 启动 client 模式 
2. 去 github 查看 restful api `https://github.com/nicolargo/glances/wiki/The-Glances-RESTFULL-JSON-API`
3. 在 Mac 电脑 输入 `curl XGET http://192.168.1.34:61208/api/3/pluginslist`