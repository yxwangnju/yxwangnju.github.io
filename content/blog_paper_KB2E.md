Title: Paper总结 - KB2E: Learning to represent knowledge graphs with Gaussian embedding
Date: 2019-10-22
Modified: 2019-10-22
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章发表于2015年，用了高斯分布来描述试题表述的不确性。对每个实体和关系用高斯分布来表示，即

$\mathcal{P}_{h} \sim \mathcal{N}\left(\boldsymbol{\mu}_{h}, \boldsymbol{\Sigma}_{h}\right)$

$\mathcal{P}_{r} \sim \mathcal{N}\left(\boldsymbol{\mu}_{r}, \boldsymbol{\Sigma}_{r}\right)$

$\mathcal{P}_{t} \sim \mathcal{N}\left(\boldsymbol{\mu}_{t}, \boldsymbol{\Sigma}_{t}\right)$

然后，还是使用translation 那一套思想，想要 (h-t) 与 r 尽可能吻合。

$P_{e} \sim N\left(u_{n}-u_{t}, \Sigma_{n}+\Sigma_{r}\right) \quad P_{r} \sim N\left(u_{r}, \Sigma_{r}\right)$

Then, they use two method to model the similarity of $P_e$ and $P_r$.

Loss function：

$\mathcal{L}=\sum_{(h, r, t) \in \Gamma} \sum_{\left(h^{\prime}, r^{\prime}, t^{\prime}\right) \in \Gamma_{(h, r, t)}^{\prime}}\left[\mathcal{E}(h, r, t)+\gamma-\mathcal{E}\left(h^{\prime}, r^{\prime}, t^{\prime}\right)\right]_{+}$

Experiments on two Tasks:

1. Link Prediction
2. Triple classification

**Motivation: They think TransE/TransH/TransR all don't consider the uncertainty of embeddings.**
