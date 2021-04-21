# python-learn
python


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
3. 然后输入 glances 会显示GUI界面