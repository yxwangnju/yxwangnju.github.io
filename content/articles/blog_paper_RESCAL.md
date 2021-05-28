Title: Paper总结 - RESCAL: A three-way model for collective learning on multi-relational data
Date: 2019-10-16
Modified: 2019-10-16
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章是2011年发表在ICML上的。

A: matrix of entity embedding

Rk: matrix of k-th relation embedding

![.]({static}/pictures/RESCAL/1.png){: .image-process-large-photo}是一个矩阵，即关于关系k的实体间的邻接矩阵

优化目标：![.]({static}/pictures/RESCAL/2.png){: .image-process-large-photo}

其中：![.]({static}/pictures/RESCAL/3.png){: .image-process-large-photo} 并且 ![.]({static}/pictures/RESCAL/4.png){: .image-process-large-photo}

总之，RESCAL就是对每一个关系建立了一个关系矩阵，有多个关系就有多少个关系矩阵。因此，RESCAL一个很大的缺点就是训练参数太多了。

