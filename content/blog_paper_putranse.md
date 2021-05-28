Title: Paper总结 - PuTransE: Non-parametric estimation of multiple embeddings for link prediction on dynamic knowledge graphs
Date: 2019-10-30
Modified: 2019-10-30
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

### 主要思想：将TransE的训练集划分到不同的空间中分开训练。

### 主要过程如下：

1. 从关系集合尺中选取1个关系 $r$, 并形成关于此关系 $r$ 的 space。 
2. 找出 KG 中所有与关系相连的实体形成集合 $E_r$。
3. 对于 $E_r$ 中的每一个实体以其作为起始点, 开始进双向 Random Walk, 获取一些三元组。
4. 对获取的三元组进行训练、得实体关系的 Embedding。

<br />

### PuTransE的用途：

1. 进行传统的link prediction
2. 可以做增量式的训练 （还可以做triple减少的训练）
3. 大大削减训练时间。

<br />

### 我的感觉
总体而言，这篇文章还有很大漏洞，主要的不足在于：

1. link prediction的实体候选集范围是有限的，对于有些test triple (h, r, t) 可能还无法计算出一个score。、
2. 缺乏理论支持。