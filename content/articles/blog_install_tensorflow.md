Title: Tensorflow的安装与卸载
Date: 2019-6-25
Modified: 2020-1-4
Category: TechNote
Tags: command, tensorflow
Authors: Audrey Wang

## 前言

入组了，开始学深度学习知识。最近安装了tensowflow, cuda，cuDNN什么的，还比较麻烦，因此写一个article记录下。

环境：windows10。安装步骤：
1. 安装python，建议3.5以上版本。我选择了3.7。
2. 安装pycharm，在pycham中关联python解释器，即给出Python.exe所在的路径。
3. Pycharm中File->settings->Project xxx:->Project interpreter，右侧列表任意双击一项就可以打开“Available Package(可安装的包的列表)”，找到你要的tensorflow版本点击install Package。gpu版需要显卡支持CUDA，并安装CUDA和cuDNN。

## 安装pip
pip就是python依赖包安装工具，我觉得pip是最方便的。在python目录下的Scripts文件夹里有pip.exe和pip3.exe。通过在命令行输入一些pip指令就可以完成安装相关依赖包了。详细：[https://blog.csdn.net/u010099080/article/details/53418159](https://blog.csdn.net/u010099080/article/details/53418159)。

![]({static}/pictures/6.png){: .image-process-large-photo}

在Pycharm中也可以安装依赖包。方法来源：[https://jingyan.baidu.com/article/335530dafdbb3619cb41c3a8.html](https://jingyan.baidu.com/article/335530dafdbb3619cb41c3a8.html)。方法：在上图的界面中，任意双击一个packge，例如pip。接着你就能看到可安装的包的列表了，找到你需要的package后点install package就好了，就这么简单。右边栏是包的介绍，下方可以选择特定的版本（用Python3.6下不到1.2之前的版本）。列表里蓝色的是已经装好的。

其实，就算只装了tensorflow也会带着一堆配套的东西，比如numpy，tensorboard，这个不需要管。另外需要pandas之类的话，安装同样的方法安装即可。

![]({static}/pictures/7.png){: .image-process-large-photo}

## conda配置不同的环境
如果装了tensorflow，再安装tensorflow-gpu，默认会运行tensorflow-gpu，如果本机不支持CUDA，就开始报错。而上面的安装方法的那个列表不支持删除。可以打开cmd，输入pip list，这样可以看到所有已经安装的包。pip uninstall tensorflow和pip uninstall tensorflow-gpu就可以删除这两个包。然后重新安装tensorflow。最好使用conda来配置不同的环境。具体conda配置环境可查看这个article[conda配置]({filename}/articles/blog_server_config_conda.md)。