Title: Paper总结 - SimplE: Simple embedding for link prediction in knowledge graphs
Date: 2019-10-23
Modified: 2019-10-23
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章发表于NeurIPS 2018。

感觉文章作者还是有很强的数学功底的，论文中CP分解部分不太容易理解。

### 总结

这篇文章是基于CP分解。文中认为CP分解中，对实体e分别用两个vector来表示，即$h_e$与$t_e$。其中he表示e处于头实体时的embedding, $t_e$是尾实体的embedding。