Title: Paper总结 - NTN: Reasoning with neural tensor networks for knowledge base completion
Date: 2019-10-24
Modified: 2019-10-24
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章发表于NeurIPS2013，在TransE发表之前。

主要内容： NTN - Neural Tensor Network

score function: 

\begin{equation}
g\left(e_{1}, R, e_{2}\right)=u_{R}^{T} f\left(e_{1}^{T} W_{R}^{[1: k]} e_{2}+V_{R}\left[\begin{array}{l}
e_{1} \\
e_{2}
\end{array}\right]+b_{R}\right)
\end{equation}

其中，$e_1, e_2 \in R^d$， 是头尾实体的向量表示。 $W_R^{[1:k]} \in R^{d \times d \times k}$，有 k 个 slide，每个 slide 都是 $d \times d$ 维。$e_1^{T}W_R^{[1:k]} \in R^{d \times d \times k}$ 的结果是一个 k 维向量，即：$h[i] = e_1^{T}W_R^{[i]}e_2$; $W_R^{[i]} \in R^{d \times d}$

Loss function: 

\begin{equation}
J(\boldsymbol{\Omega})=\sum_{i=1}^{N} \sum_{c=1}^{C} \max \left(0,1-g\left(T^{(i)}\right)+g\left(T_{c}^{(i)}\right)\right)+\lambda\|\boldsymbol{\Omega}\|_{2}^{2}
\end{equation}