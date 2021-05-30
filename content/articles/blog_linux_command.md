Title: Linux下常用命令整理
Date: 2021-5-25
Modified: 2021-5-25
Category: TechNote
Tags: linux, command
Authors: Audrey Wang

# 这篇note记录linux下常用command
显示当前目录下文件大小:
```text
ls -l
```

显示特定文件的大小:
```text
ls -l | grep 'name'
```

更改文件名:
```text
mv file file'
```

查看当前系统的所有进程：
```text
top
```

## GPU相关命令

显示显卡状况:
```text
watch -n 1 nvidia-smi
```

查看使用GPU的所有进程：
```text
fuser -v /dev/nvidia*
```

杀掉GPU的某个进程（把PID替换为对应进程ID）：
```text
kill -9 PID
```


## ... 持续更新中!