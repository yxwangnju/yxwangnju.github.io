Title: How to use SSH keys to connect remote servers
Date: 2020-02-04
Modified: 2020-02-04
Category: TechNote
Tags: command, ssh
Authors: Audrey Wang

## How SSH Keys Work?

Firstly, users should have a `‘public key/private key’` pair to connect to a remote server. Briefly, **user's local client stores the private key, while the remote sever stores the public key**.

When client wants to connect server, the client will send a request to the server. After server recerives the request and passed the authentication, it returns a string to client. Then client will encrypt this string using its private key and send the encrypted string to server to get authenticated.

<br />

## Steps

### 1. Create Key Pair 

```text
ssh-keygen -t rsa -C "name"
```

`-t` denotes the encryption algorithm, and `-C` denotes the name for the ssh keys (usually client name).

This command will generate two files (id_rsa and id_rsa.pub) in folder `~/.ssh`. id_rsa is the private key and id_rsa.pub is the public key.

### 2. Copy the Public Key to Server

```text
scp ~/.ssh/id_rsa.pub yxwang@<server_ip>:~/.ssh
```

### 3. Put the Public Key to Authorized Keys
Continuely in server, enter the following command:

```text
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
and 
```text
chmod 600 ~/.ssh/authorized_keys
```

### 4. Connect to Server in Client and Done!

```text
ssh yxwang@<server_ip>
```

<br />

## Note

Sometime after the configuration above, we still need password to login. In such situation, we can follow this [blog](https://blog.csdn.net/silentwolfyh/article/details/83656101) to find solution.