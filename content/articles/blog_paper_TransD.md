Title: Paper总结 - TransD: Knowledge graph embedding via dynamic mapping matrix
Date: 2019-10-22
Modified: 2019-10-22
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

我感觉这篇文章没有什么太吸引人的地方。

文章的目的是：认为CTransR考虑了关系的种类，但没有考虑实体的种类。

方法：对实体和关系都用了2个vector来embedding。比如对(h, r, t)，用 $h$, $h_p$, $r$, $r_p$, $t$, $t_p$ 来embedding。其中: $h, h_{p} \in R^{m}, t, t_{p} \in R^{n}$

接着定义了两个映射矩阵：

$\mathbf{M}_{r h}=\mathbf{r}_{p} \mathbf{h}_{p}^{\top}+\mathbf{I}^{m \times n}$
$\mathbf{M}_{r t}=\mathbf{r}_{p} \mathbf{t}_{p}^{\top}+\mathbf{I}^{m \times n}$

得到映射后的两个向量：

$\mathbf{h}_{\perp}=\mathbf{M}_{r h} \mathbf{h}, \quad \mathbf{t}_{\perp}=\mathbf{M}_{r t} \mathbf{t}$

score function还是translation-based：

$f_{r}(\mathbf{h}, \mathbf{t})=-\left\|\mathbf{h}_{\perp}+\mathbf{r}-\mathbf{t}_{\perp}\right\|_{2}^{2}$

Loss function:

$L=\sum_{\xi \in \Delta} \sum_{\xi^{\prime} \in \Delta^{\prime}}\left[\gamma+f_{r}\left(\xi^{\prime}\right)-f_{r}(\xi)\right]_{+}$