Title: 如何用Power BI给地图上色
Date: 2020-9-7
Modified: 2020-9-7
Category: TechNote
Tags: others
Authors: Audrey Wang

每次看到网上给地图着色的图，就觉得这真的是一种很直观展现数据信息的方式，一直想学。正好之前有使用过 Power BI 的经历，就琢磨着如何用 Power BI 来实现这一想法。接下来将我怎么实现的。

全文只需要准备到的两样工具:

- Power BI 软件
- 要着色的 svg 矢量图

<br />

## 1. 下载需着色的矢量地图

其实免费下载的网站零零散散有很多，比如这个[网站](http://datav.aliyun.com/tools/atlas)。我自己整理后了一个中国各省份的 svg 矢量地图集，点击[此处]({attach}/downloads/svg_maps.zip)可下载。

比如，这里就有一张内蒙古的 svg 地图：

![inner mongolia]({static}/pictures/color_map/1.png){: .image-process-large-photo}

## 2. 用synoptic panel应用给svg地图标注信息

打开网址 [https://synoptic.design/](https://synoptic.design/)，导入要着色的 svg 图并进行编辑。

![.]({static}/pictures/color_map/2.png){: .image-process-large-photo}

注意：以该图为例，图右边显示的是 svg 图的层级结构，G1 代表整个内蒙，下面的 path 代表各个地级市。因为一般的内蒙各地级市统计表直接就显示的是各个地级市信息，因此 G1 这个层次不需要，需要被删除（可使用软件inkscape进行删除）。

删除后，地图就没有层次关系了，之后便可直接在 name to bind 上编辑地级市名称，如下图所示：

![.]({static}/pictures/color_map/3.png){: .image-process-large-photo}

## 3. 准备原始数据

地图准备好后，还需要准备数据信息。比如这是一份内蒙古的各个地级市的人口和民族信息：

![.]({static}/pictures/color_map/4.png){: .image-process-large-photo}

**注意，统计表的地级市列的名称需要与上一步 svg 图编辑时填入的名称一致**。(比如在这个例子中，此处的地级市名称应该没有“市”字)。

## 4. 导入 Power BI

首先，打开 Power BI，导入原始数据。然后，在可视化视图那，点击“获取更多视觉对象”，搜索 synoptic panel 并加载。

![.]({static}/pictures/color_map/5.png){: .image-process-large-photo}

synoptic panel 加载完毕后，将数据表的相关属性拖入到 category 和 measure 中。一般category 就是地级市，比如下图：

![.]({static}/pictures/color_map/6.png){: .image-process-large-photo}

## 5. 大功告成

最后一切就ok了，可显示各种信息图：

![.]({static}/pictures/color_map/7.png){: .image-process-large-photo}

![.]({static}/pictures/color_map/8.png){: .image-process-large-photo}