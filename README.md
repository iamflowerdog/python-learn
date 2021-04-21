# python-learn
python


## ubuntu 安装 python


```
apt-get remove python-pip python3-pip


wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
python3 get-pip.py

```
* 1. 先安装python
* 2. 获取 get-pip.py 文件 `wget https://bootstrap.pypa.io/get-pip.py`
* 3. 下载文件后，通过 python 执行 `python get-pip.py`
     `如果执行失败，会提示你需要 Please use https://bootstrap.pypa.io/pip/2.7/get-pip.py instead `
     `这个报错的意思，就是告诉我们 根据本地机器的版本，去下载正确的 get-pip.py 文件, 然后重复执行步骤2 `
* 4. 