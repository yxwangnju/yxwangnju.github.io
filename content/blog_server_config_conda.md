Title: 远程服务器连网配置+conda使用 
Date: 2021-5-25
Modified: 2021-5-25
Category: TechNote
Tags: conda, command
Authors: Audrey Wang

---

<br />

# 一、远程服务器连网配置

实验室的服务器一般都是没联网的，因此需要让服务器使用其他已连网设备进行代理。一般就使用本地机器。首先下载推荐软件[CCProxy](https://www.youngzsoft.net/ccproxy/), 开启后确认好本地连接地址以及端口，比如111.222.33.44:808。如果本机使用了VPN进行代理，则需要开启二级代理（点击“高级”），并查询VPN的使用端口。

![]({static}/pictures/ccproxy.jpg){: .image-process-large-photo}

然后，在服务器上设置代理，输入以下命令：
```text
export http_proxy=http://111.222.33.44:808
export https_proxy=https://111.222.33.44:808
```
然后验证是否生效：
```text
echo $http_proxy
```
如果显示正确，则ok！

接下来检查是否能上网，输入以下命令：
```text
wget www.baidu.com
```
如果返回网页数据，则联网成功！


<br />

# 二、Conda配置与使用

## 1. 配置conda连网
进入服务器的.condarc文件（一般就在自己用户名的目录下），修改文件内容如下：
```text
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: true
 
proxy_servers:
  http: http://xxx.xx.xx:808
  https: https://xxx.xx.xx:808
ssl_verify: false
```
channel一般换成国内的镜像，proxy_server换成上面ccproxy配置的地址。

<br />

## 2. conda创建env
创建有特定版本python的conda环境：
```text
conda create -n envname python=3.7
```
`proceed ([y]/n)?` 就输入 `y`

之后，可用conda或者pip安装其他的依赖包，假设所有依赖包都在requriment.txt文件中：
```text
pip install -r requriment.txt
```
或者
```text
conda install -r requriment.txt
```

<br />

## 3. 其他conda命令
查看目前所有conda环境：
```text
conda info -e
```
查看目前环境下有哪些包：
```text
conda list 或者 pip list
```
进入某个conda环境：
```text
conda activate envname 或者 source activate envname
```
