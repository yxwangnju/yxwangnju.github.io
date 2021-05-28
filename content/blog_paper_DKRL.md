Title: Paper总结 - DKRL:Description-Embodied Knowledge Representation Learning
Date: 2019-12-4
Modified: 2019-12-4
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

> 这篇文章Accepted in AAAI2016

摘要：已有的KRL模型都是基于structure information来建模的，即只基于三元组关系。事实上，许多知识库中也包含对实体的描述信息，如果在embedding中能考虑到这些文本描述信息，则会提升KRL的效果。在对描述文本进行embedding时，本文考虑了两种方式，一种是bag_of_words，另一种是CNN。Bog_od_words模型把文本内容看成无序的组合，但CNN考虑到了文本内容的位置(因为有窗口)。同时，这篇文章也可用于zero-shot场景的学习，即要测试的实体是全新的、在训练集中未出现过的。

### 特点(不足)：

1. zero-shot的场景只考虑了新增实体，没有考虑新增关系。
2. 因为考虑了实体的描述信息，因此需要的原始数据就要求比较高。在许多real-KG上不太work。
3. 也只考虑了FB15K，在上面加新增实体构成了FB20K