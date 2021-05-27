Title: Using bert-as-service
Date: 2020-11-5
Modified: 2020-11-5
Category: TechNote
Tags: command, BERT
Authors: Audrey Wang


### Using BERT model as a sentence encoding service
Recently I have to use BERT as the pre-trained language model for my task. There is a package called `bert-as-service` to provide services that encodes sentences.

<br />

### Installation

Install the server and client via pip. They can be installed separately or even on different machines:

```text
pip install bert-serving-server  # server
pip install bert-serving-client  # client, independent of `bert-serving-server`
```

Note that the server MUST be running on Python >= 3.5 with Tensorflow >= 1.10 (one-point-ten). Again, the server does not support Python 2!

<br />

### Getting Started!

#### 1. Download a Pre-trained BERT Model

Head to [BERT DOWNLOAD](https://github.com/google-research/bert) to download certain version of BERT.

![]({static}/pictures/3.jpg){: .image-process-large-photo}

H stands for dimension, and L stands for layer number.

I use the 12/768 (BERT-Base) version.

<br />

#### 2. Start the BERT service

After installing the server, then to use bert-serving-start CLI as follows:

```text
bert-serving-start -model_dir /tmp/english_L-12_H-768_A-12/ -num_worker=4 
```

The '/tmp/english_L-12_H-768_A-12/' is the location of the BERT category that you just downloaded. 

**Don't set the num_worker too big! No more than 4. Usually 1 or 2.** 

![]({static}/pictures/4.jpg){: .image-process-large-photo}

If showing like the above picture, it means successfully started.

We can enter `ctrl+z` in terminal to end the service. If entering in terminal doesn't work, we can go to the Task Manager to manually end it.

![]({static}/pictures/5.jpg){: .image-process-large-photo}

<br />

#### 3. Use Client to Get Sentence Encodes

Now we can encode sentences simply as follows:

```text
from bert_serving.client import BertClient
bc = BertClient()
bc.encode(['First do it', 'then do it right', 'then do it better'])
```

It will return a `ndarray` (or `List[List[float]]` if you wish), in which each row is a fixed-length vector representing a sentence.

As a feature of BERT, you may get encodes of a pair of sentences by concatenating them with `|||` (with whitespace before and after), e.g.

```text
bc.encode(['First do it ||| then do it right'])
```

<br />

### Use BERT Service Remotely

One may also start the service on one (GPU) machine and call it from another (CPU) machine as follows:

```text
# on another CPU machine
from bert_serving.client import BertClient
bc = BertClient(ip='xx.xx.xx.xx')  # ip address of the GPU machine
bc.encode(['First do it', 'then do it right', 'then do it better'])
```

In this case, we only need 
```text
pip install -U bert-serving-client
```

in local machine. The service in server usually is on.
