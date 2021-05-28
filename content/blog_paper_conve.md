Title: Paper总结 - ConvE: Convolutional 2D knowledge graph embeddings
Date: 2019-10-24
Modified: 2019-10-24
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

发表于AAAI2018。

该篇文章利用了卷积操作，整个模型如下：

![.]({static}/pictures/conve/1.jpg){: .image-process-large-photo}

score function的定义如下：

\begin{equation}
\psi_{r}\left(\mathbf{e}_{s}, \mathbf{e}_{o}\right)=f\left(\operatorname{vec}\left(f\left(\left[\overline{\mathbf{e}_{s}} ; \overline{\mathbf{r}_{r}}\right] * \omega\right)\right) \mathbf{W}\right) \mathbf{e}_{o}
\end{equation}

其中 $\left[\overline{\mathbf{e}_{s}} ; \overline{\mathbf{r}_{r}}\right] * \omega$ 就是卷积操作，$\mathbf{W}$ 就是映射。

同时本文也用了 1-N scoring，以往的scoring都是1-1的打分，这篇文章提出了可用1-N的方式打分。