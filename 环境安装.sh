# 01 ubuntu 16.04 编译安装 python 2.7.15
# 创建目录 安装python在此目录下
sudo mkdir -p /usr/local/ll
# 新建后他的权限默认只有root可以写入,要修改权限,所有人都可以写
sudo chmod 777 /usr/local/ll

# 安装zlib库, 因为setuptools依赖这个库
sudo apt-get install zlib1g-dev
# 安装 ssl
sudo apt-get install libssl-dev
# 修改python源文件包中的文件Modules/Setup.dist：(Java代码)
  
# Socket module helper for SSL support; you must comment out the other  
# socket line above, and possibly edit the SSL variable:  
SSL=/usr 
_ssl _ssl.c \
        -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
       -L$(SSL)/lib -lssl -lcrypto 
# 修改后编译安装python就支持ssl了

# 下载源代码安装包
# 进入目录
cd /usr/local/ll
wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz
# 解压
tar zxvf Python-2.7.15.tgz
mkdir python
cd Python-2.7.15
# 编译安装
./configure --prefix=/usr/local/ll/python --with-zlib=/usr/include && \
make && \  # 编译
make install  # 安装

# 安装完成后python在/usr/local/ll/python/bin/ 这个目录里
# 执行他的命令如下:
/usr/local/ll/python/bin/python
# 添加别名
vim ~/.bashrc # 添加下面的行
alias py2=/usr/local/ll/python/bin/python
# 可以使用py2 执行安装的python了

# 02 安装setuptools
# 进入目录
cd /usr/local/ll
wget https://files.pythonhosted.org/packages/1a/04/d6f1159feaccdfc508517dba1929eb93a2854de729fa68da9d5c6b48fa00/setuptools-39.2.0.zip
unzip setuptools-39.2.0.zip
cd setuptools-39.2.0
# 用安装好的指定的Python 运行setup.py安装, 会安装到指定的Python版本中
py2 setup.py build && py2 setup.py install

# 03 安装pip
cd /usr/local/ll && \
wget https://files.pythonhosted.org/packages/ae/e8/2340d46ecadb1692a1e455f13f75e596d4eab3d11a57446f08259dee8f02/pip-10.0.1.tar.gz && \
tar zxvf pip-10.0.1.tar.gz && \
cd pip-10.0.1 && \
py2 setup.py build && \
py2 setup.py install

# 04 安装虚拟环境
pip install virtualenv && \
pip install virtualenvwrapper

# 05 安装git
sudo apt-get install git
# 生成公钥
ssh-keygen -t rsa
# 添加公钥到git
# github 账号: diligentDay 密码: diligent666
cat ~/.ssh/id_ras.pub  # 复制添加到github的ssh设置中
mkdir ~/study
cd ~/study
git clone git@github.com:diligentDay/project_study.git
#  ok



 











