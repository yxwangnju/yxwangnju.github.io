Title: Paper总结 - TransR: Modeling relation paths for representation learning of knowledge bases
Date: 2019-10-17
Modified: 2019-10-17
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

2015年发表在AAAI上。

TransR其实和TransH很相似，针对不同的关系将实体映射到不同的空间中。文中认为TransE和TransH的缺点是将entity和relation放在同一维度空间中。于是提出了可将entity和relation映射在不同空间。

![.]({static}/pictures/TransR/1.png){: .image-process-large-photo}

对于每一个关系 $r$，都有一个映射矩阵 $M_r$，将实体映射到关系空间中。

![.]({static}/pictures/TransR/2.png){: .image-process-large-photo}

这里实体的维数和关系的维数不必相等。

![.]({static}/pictures/TransR/3.png){: .image-process-large-photo}

Score function:

![.]({static}/pictures/TransR/4.png){: .image-process-large-photo}

----

同时，还提出了CTransR (Cluster-based TransR)

按照不同的关系将pair(h, t)划分到不同的cluster中，比如：

![.]({static}/pictures/TransR/1.jpg){: .image-process-large-photo}

对每一个簇学习一个关系表示。

score function定义为：

![.]({static}/pictures/TransR/5.png){: .image-process-large-photo}

实验部分也是在三个任务上进行了比较：

1. link prediction
2. triple classification
3. text relation extraction