Title: Paper总结 - TransE
Date: 2019-10-6
Modified: 2019-10-6
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章可以说是非常经典的了，KG embedding领域内的方法基石。

### 总结

距离公式：

$dis=\|h+r-t\|_{L_{1} / L_{2}}$

学习的参数个数：$n \times d + m \times d = (n+m) \times d$

实体之间的关系可分为四种：1-1, 1-n, n-1, n-n:

![.]({static}/pictures/6.jpg){: .image-process-large-photo}

TransE在处理irreflexive和one-to-one的关系时表现更好。