# README

## Introduction
This program automates ssh login to remote host with passwords. This program works with open-ssh and python, and its configuration is described as YAML format. This program can be used in case that the target host is accessed via multiple bastions.

## Environment
This program needs to install the following package and libraries:
* python3.x
* pexpect
* PyYAML
* curses

## Configuration
Prepare an ssh config file describing parameters to access the target host. An example is below:

> Host example1  
>    &emsp;Hostname 192.168.64.2  
>    &emsp;Port 22  
>    &emsp;identityFile ~/.ssh/example01  
>    &emsp;User ubuntu
>
> Host example2  
>    &emsp;Hostname 172.16.10.2  
>    &emsp;Port 22  
>    &emsp;User ubuntu  
>    &emsp;UpdateHostKeys ask  
>    &emsp;IdentitiesOnly yes  
>    &emsp;IdentityFile ~/.ssh/example02  
>    &emsp;ProxyJump example1  
>    &emsp;DynamicForward 1080


Describe configurations of this program in "ssh_autologin_config.yml" file. In this config file, you can set multiple target hosts. For each target host, you need to decide its ID and set a hostname, which should be the same with one of hosts described in ssh config file, and password list (if the target host is accessed via some bastions and some of them need password, you need to describe those passwords in order) in the nest on the ID. An example is below:

> host1:  
>   &emsp;host: example1  
>   &emsp;pass: [pass1]
>
> host2:  
>   &emsp;host: example2  
>   &emsp;pass: [pass1, pass2]  

"ssh_autologin.py" and "ssh_autologin_configuration.yml" should be in the same directry. Or you need modify the name of the configuration file to the PATH.

## How to use
In your terminal or command prompt, run "ssh_autologin.py" with a host ID as its argument. Host ID must be one of IDs in "ssh_autologin_configuration.yml".

> $ python3 ssh_autologin.py example1







