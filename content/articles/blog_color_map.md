Title: 如何用Power BI给地图上色
Date: 2020-9-7
Modified: 2020-9-7
Category: TechNote
Tags: others
Authors: Audrey Wang

每次看到网上给地图着色的图，就觉得这真的是一种很直观展现数据信息的方式，一直想学。正好之前有使用过 Power BI 的经历，就琢磨着如何用 Power BI 来实现这一想法。接下来将我怎么实现的。

<br />

全文只需要准备到的两样工具:

- Power BI 软件
- 要着色的 svg 矢量图

<br />

## 1. 准备数据

第一步当然是要准备好数据。这篇文章中我以展示内蒙古的人口民族信息为例，准备的数据表格如下：

![.]({static}/pictures/color_map/4.png){: .image-process-large-photo}

注意，如果给地图着色，要展现各个区域的不同信息时，数据表中的列名就要以各个区域为名。

<br />

## 2. 下载需着色的矢量地图

其实免费下载的网站零零散散有很多(比如[datav](http://datav.aliyun.com/tools/atlas))。我自己整理了一个中国各省份的 svg 矢量地图集，点击[**此处**]({attach}/downloads/svg_maps.zip)可下载。

接下来我以给内蒙古的地图着色为例。这里就有一张内蒙古的 svg 矢量地图：

![inner mongolia]({static}/pictures/color_map/1.png){: .image-process-large-photo}

<br />

## 3. 用 synoptic panel 应用给 svg 地图标注信息

很多时候下载下来的 svg 地图的格式是乱七八糟的，因此需要调整格式。打开网址 [https://synoptic.design/](https://synoptic.design/)，导入要着色的 svg 图并进行编辑。

![.]({static}/pictures/color_map/2.png){: .image-process-large-photo}

以该内蒙古的原始 svg 图为例，图右边显示的是图的层级结构，G1 代表整个内蒙，下面的 path 代表各个地级市。因为步骤 1 的内蒙各地级市统计表直接就显示的是各个地级市信息，因此 G1 这个层次不需要，需要被删除（可使用软件inkscape进行删除）。

删除后，地图就没有层次关系了，之后便可直接在 name to bind 上编辑地级市名称，如下图所示：

![.]({static}/pictures/color_map/3.png){: .image-process-large-photo}

**注意，svg 图的地级市列的名称需要与之前数据表中的地级市名称一致**。

<br />

## 4. 将数据导入 Power BI

打开 Power BI，导入原始数据。然后，在可视化视图那，点击“获取更多视觉对象”，搜索 synoptic panel 并加载。

![.]({static}/pictures/color_map/5.png){: .image-process-large-photo}

synoptic panel 加载完毕后，将数据表的相关属性拖入到 category 和 measure 中。一般category 就是地级市，measure 就是我们要展示的信息。比如下图，要展现各市性别比：

![.]({static}/pictures/color_map/6.png){: .image-process-large-photo}

<br />

## 5. 大功告成

上面操作完成后，就ok了。可显示各种信息图：

![.]({static}/pictures/color_map/7.png){: .image-process-large-photo}

![.]({static}/pictures/color_map/8.png){: .image-process-large-photo}