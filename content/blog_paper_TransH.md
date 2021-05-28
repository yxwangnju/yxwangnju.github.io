Title: Paper总结 - TransH: Knowledge graph embedding by translating on hyperplanes
Date: 2019-10-17
Modified: 2019-10-17
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

为了解决TransE无法很好地表达reflexive/one-to-many/many-to-one/many-to-many关系的问题，TransH会将实体的每个embedding投影到一个平面上，再在这些平面上做translation。

对每一个关系，除了关系自身的embedding外，还定义了每个关系的投影平面的法向量$W_r$。

![.]({static}/pictures/7.jpg){: .image-process-large-photo}

TransH的实验结果：

![.]({static}/pictures/8.jpg){: .image-process-large-photo}

同时，本论文也做了triple classification和text fact extraction的实验。