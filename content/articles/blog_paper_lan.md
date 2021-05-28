Title: Paper总结 - LAN: Logic Attention Based Neighborhood Aggregation for Inductive Knowledge Graph Embedding
Date: 2019-12-4
Modified: 2019-12-4
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

Accepted in AAAI2019

### 阅读时发现的特性(不足)：
1. 仍然学习的是 neiboirhood aggregator，那么这种通用的 aggregator，每来一个新实体不需经过训练就直接得到 embedding，是否造成这个 embedding 的质量并不好。
2. 只考虑到新实体的加入。
3. 新实体必须是只出现在head位置或只出现在 tail 位置的实体。对于既出现在 head 又出现在 tail 的实体无法执行。
4. 只在一个数据集 (FB15K) 上做实验。

<br />

### 文章的创新点：

1. 获取周围邻居的 neighbors 后，在 pooling 层求新实体的 embedding 时，引入了 attention mechanism。这个 attention mechanism 引用了 logic rule (概率)，这是关键的地方。
2. 做了充足的小实验，比如 pooling 层用 mean、LSTM 以及各种 attention 变种。因为用了 attention，还加了一个 case study。