Title: Tensorflow的安装与卸载
Date: 2019-6-25
Modified: 2020-1-4
Category: TechNote
Tags: command, tensorflow
Authors: Audrey Wang

---
## 前言

最近开始学习深度学习的相关知识，看了一些关于tensorflow安装的博客，绕了一些弯，因此来填一下坑(多余安装的或者非windows)，主要围绕使用pycharm时需要用到tensorflow的安装过程。

环境：windows10专业版。只是想简单跑一下tensorflow的话，安装过程真的很简单。
如果你有“安装IDE并关联编译器"的经验，不想看复杂的安装说明，可以尝试看这个目录凭自己的理解装完，有问题细看。
1. 安装python，建议3.5以上版本
2. 安装pycharm，在pycham中关联python解释器，即给出Python.exe所在的路径。
3. Pycharm中File->settings->Project xxx:->Project interpreter，右侧列表任意双击一项就可以打开“Available Package(可安装的包的列表)”，找到你要的tensorflow版本点击install Package。gpu版需要显卡支持CUDA，并安装CUDA和cuDNN。

## 安装pip

1. 安装python(如果你已经装有python，可以跳过这步)
指的是python的解释器(interpreter)和一些套件，有点类似于学C的时候的编译器的感觉，找到资源运行一下exe基本就装好了。关于版本，tensorflow1.2以后的版本需要3.5以后的版本。关于2.x与3.x的区别有哦兴趣可以参考
[http://www.runoob.com/python/python-2x-3x.html](http://www.runoob.com/python/python-2x-3x.html)。

2. 选择一个IDE
好的IDE可以提高效率，我使用的pycharm，这个看个人喜好。Anaconda有自带spider。
pycharm资源和安装教程很多，这里略过。
例如：[https://blog.csdn.net/yctjin/article/details/70307933?locationNum=11&fps=1](https://blog.csdn.net/yctjin/article/details/70307933?locationNum=11&fps=1)。
IDE安装的时候会询问是否关联解释器，如果不小心点过去了，也可以打开File->Project:xxx->Project interpreter来关联解释器的路径，这个过程和使用codeblocks关联编译器差不多。至此基本的python已经可以用了。

![]({static}/pictures/6.png){: .image-process-large-photo}

另：File->settings->Color Scheme可以选择主题。

一些教程比较推荐的方法是使用pip，这个很方便。在python目录下的Scripts文件夹里有pip.exe和pip3.exe。通过在命令行输入一些指令就可以完成安装了。详细：[https://blog.csdn.net/u010099080/article/details/53418159](https://blog.csdn.net/u010099080/article/details/53418159)。

Pycharm安装其实更加方便(本质还是pip，只不过不需要自己输指令)。方法来源：[https://jingyan.baidu.com/article/335530dafdbb3619cb41c3a8.html](https://jingyan.baidu.com/article/335530dafdbb3619cb41c3a8.html)。方法：在如图1的界面中，任意双击一个packge，例如pip。接着你就能看到可安装的包的列表了，找到你需要的package后点install package就好了，就这么简单。右边栏是包的介绍，下方可以选择特定的版本（用Python3.6下不到1.2之前的版本）。列表里蓝色的是已经装好的。

装好以后你的列表里就有了，如上图1所示。就算只装了tensorflow也会带着一堆配套的东西，比如numpy，tensorboard；完全不用担心。另外需要pandas之类的话，安装同样的方法安装即可。

![]({static}/pictures/7.png){: .image-process-large-photo}

## conda配置不同的环境
如果装了tensorflow，再安装tensorflow-gpu，默认会运行tensorflow-gpu，如果本机不支持CUDA，就开始报错。而上面的安装方法的那个列表不支持删除。可以打开cmd，输入pip list，这样可以看到所有已经安装的包。pip uninstall tensorflow和pip uninstall tensorflow-gpu就可以删除这两个包。然后重新安装tensorflow。最好使用conda来配置不同的环境。具体conda配置环境可查看这个article[conda配置]({filename}/blog_server_config_conda.md)