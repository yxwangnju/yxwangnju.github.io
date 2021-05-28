Title: Paper总结 - TransD: Knowledge graph embedding via dynamic mapping matrix
Date: 2019-10-22
Modified: 2019-10-22
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

我感觉这篇文章没有什么太吸引人的地方。

文章的目的是：认为CTransR考虑了关系的种类，但没有考虑实体的种类。

方法：对实体和关系都用了2个vector来embedding。比如对(h, r, t)，用$h$, $h_p$, $r$, $r_p$, $t$, $t_p$来embedding。其中: $h, h_{p} \in R^{m}, t, t_{p} \in R^{n}$

接着定义了两个映射矩阵：

![.]({static}/pictures/10.png){: .image-process-large-photo}

得到映射后的两个向量：

![.]({static}/pictures/11.png){: .image-process-large-photo}

score function还是translation-based：

![.]({static}/pictures/12.png){: .image-process-large-photo}

Loss function:

![.]({static}/pictures/13.png){: .image-process-large-photo}