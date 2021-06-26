Title: Paper总结 - RESCAL: A three-way model for collective learning on multi-relational data
Date: 2019-10-16
Modified: 2019-10-16
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章是2011年发表在ICML上的。

以下是符号表示是：

$A$: matrix of entity embedding

$R_k$: matrix of k-th relation embedding

$\mathcal{X}_{k} \approx A R_{k} A^{T}$, for $k=1, \ldots, m$ 是一个矩阵，即关于关系k的实体间的邻接矩阵

优化目标：$\min _{A, R_{k}} f\left(A, R_{k}\right)+g\left(A, R_{k}\right)$

其中：$f\left(A, R_{k}\right)=\frac{1}{2}\left(\sum_{k}\left\|\mathcal{X}_{k}-A R_{k} A^{T}\right\|_{F}^{2}\right)$ 并且 $g\left(A, R_{k}\right)=\frac{1}{2} \lambda\left(\|A\|_{F}^{2}+\sum_{k}\left\|R_{k}\right\|_{F}^{2}\right)$

总之，RESCAL就是对每一个关系建立了一个关系矩阵，有多个关系就有多少个关系矩阵。因此，RESCAL一个很大的缺点就是训练参数太多了。

