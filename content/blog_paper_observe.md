Title: Paper总结 - Observed versus latent features for knowledge base and text inference
Date: 2019-11-30
Modified: 2019-11-30
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

作者是Kristina Toutanova, 和Danqi Chen

本文提出了一个很简单的observed model，就可以在FB15k, WN18上的link prediction的性能超过已有的模型。文中认为原因就是这两个数据集中存在很多冗余的关系，比如语义相似的关系和inverse的关系。

例子：$r_1$和$r_2$是两个相似的关系，它们经常共同存在，$r_1$, $r_3$是inverse的关系，也会经常共同出现，即($e_1$, $r_1$, $e_2$)的三元组如果存在，则($e_1$, $r_2$, $e_2$)和($e_2$, $r_3$, $e_1$)也会存在。那么$r_1$与$r_2$就是相似关系，$r_1$与$r_3$就是inverse关系。那么在测试集中要测试($e_1$, $r_2$, $e_2$)或者($e_2$, $r_3$, $e_1$)时，如果($e_1$, $r_1$, $e_2$)在训练集中存在，那么这两个三元组则非常可能被判断为正确。

因此，为了解决FB15K和WN18这两个数据集中存在的问题，本文重新构造了一个数据集FB15k-237。这个数据集中删除了语义相似的关系或者inverse的关系，比如$r_1$,$r_2$,$r_3$，删除了$r_2$和$r_3$，保留了$r_1$，这样最后就只有237个关系。同时，对于测试集与验证集中的每个三元组，其实体之间在训练集中不能相连。也就是说验证集和测试集中要测试的entity pair在训练集中不能相连。