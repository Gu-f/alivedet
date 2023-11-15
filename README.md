# alivedet
一个python实现的主机存活探测工具

## 支持的协议探测类型
| 探测类型 | 是否支持 |
| ------------ |---|
| ICMP-PING | ✔️  |
| ARP-PING | ❌ |
| TCP-ACK-PING | ❌ |
| TCP-SYN-PING | ❌ |
| UDP-PING | ❌ |


## 安装
模块  
```shell
pip install -r requirements.txt
```
依赖  
```shell
安装详情请往下看依赖

windows: npcap or winpcap  
linux: libpcap
```


## 用法
```shell
python .\alivedet.py --hosts=192.168.124.17-192.168.124.27 --multi=2 --log-level=ERROR 
```

## 依赖
### Windows
[Npcap](https://npcap.com/) or [Winpcap](https://www.winpcap.org/)  
[Npcap和Winpcap对比](https://npcap.com/vs-winpcap.html)  


### Linux
[libpcap](https://www.tcpdump.org/#latest-release)  
```shell
# Debian/Ubuntu系统
sudo apt-get install libpcap-dev   

# CentOS/RHEL系统
sudo yum install libpcap-devel  

# Fedora系统
sudo dnf install libpcap-devel   

# Arch Linux系统
sudo pacman -S libpcap  
```