Title: Paper总结 - SimplE: Simple embedding for link prediction in knowledge graphs
Date: 2019-10-23
Modified: 2019-10-23
Category: Paper Reading
Tags: Research, Paper
Authors: Audrey Wang

这篇文章发表于NeurIPS 2018。

感觉文章作者还是有很强的数学功底的，论文中CP分解部分不太容易理解。

### 总结

这篇文章是基于CP分解。文中认为CP分解中，对实体e分别用两个vector来表示，即$h_e$与$t_e$。其中$h_e$表示 e 处于头实体时的embedding, $t_e$是尾实体的embedding。关系$r$只有一种表示。

作者认为这种方式有不足的地方，比如说：

![.]({static}/pictures/simple/1.jpg){: .image-process-large-photo}

假如($e_1$, $r_1$, $e_2$)是$e_1$爱看某个电影，($e_2$, $r_2$, $e_3$)是$e_2$中有$e_3$参演。但它们彼此之间没有联系，但直观上感觉$e_3$是否参演对$e_1$是否爱看这部电影应该是有影响的。

于是SimplE为这个边构造了一个反向边(绿色所示)，这样$e_2$与$e_3$的更新就会影响到($e_1$, $e_2$)

$\langle h_e, r, t_e\rangle \doteq \sum_{j=1}^{k} h_{e}[j] * r[j] * t_{e}[j]$

$\langle t_e, r^{-1}, h_e\rangle \doteq \sum_{j=1}^{k} h_{e}[j] * r^{-1}[j] * t_{e}[j]$

目标是使所有 $\langle h_e, r, t_e\rangle$ 与 $\langle t_e, r^{-1}, h_e\rangle$ 最小（或者最大化）。测试时只会使用 $r$，而不会使用 $r^{-1}$。

文忠认为SimplE的表达能力是全面的，能够处理 Symmetric / anti-symmetric / inverse / transitive 所有类型的关系。