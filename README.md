# 通过python，利用selenium和Chromedriver在chrome浏览器实现多个网站自动登录，并轮巡展示功能。

# 环境部署
## ①直接安装python
下载executable版安装

## ②使用便携版
下载python embeddable版本（最好解压放到英文路径下）

配置环境变量（右击“我的计算机”，选择“属性”“高级系统设置”“环境变量”，双击系统变量的“path”，新建并将python路径复制到此，确定）

（安装pip）下载get-pip.py文件至python解压后的目录，get-pip.py文件下载方式参考如下：
https://pip.pypa.io/en/stable/installing/ ，链接另存为即可

在当前目录下打开cmd，输入命令“python get-pip.py”并敲击回车运行命令，安装完成后，文件夹中会增加Lib和Scripts两个文件夹，将script路径添加到环境变量
![image](https://github.com/zongru666/test/assets/166798572/39bfa7ac-9ee3-45bf-898b-b581e7ab4adb)

记事本打开python37._pth，去除import site的注释，最终修改如下：
>    python37.zip  
>    “# Uncomment to run site.main() automatically”  
>    import site  #其实就是去掉前面的“#”  

执行命令
> pip install selenium  
下载chromedriver（版本与chrome要对应，将chromedriver.exe放到script文件夹下）  
https://www.cnblogs.com/hester/p/11321884.html#_label2_0
-------------------------------------------------------------------------------------
# 将WebDemo.bat和PythonWebDemo.py文件放到D盘
> ~1.需要配置环境变量（双击 配置环境.bat ）可能会有告警~  
> 2.如果pip list不成功，需要运行get-pip.py文件  
> 3.还要看chrome版本是不是87.0.4280.x  
（有些高于这个版本也行，如果不行就要更改driver，搜索chromedriver并下载对应win32版本，解压并将exe文件添加到webdemo20220517\done\python-3.7.8-embed-amd64\Scripts路径下）  
安装python①（或者使用便携版②）（以python3.7.8为例）
-------------------------------------------------------------------------------------
## 鼓励一下
[返回目录](#contents)  
如果这个项目有帮到你，希望你能动用你的发财小手支持一下  
_你的鼓励是这个项目继续更新的最大动力_  

![mm_reward_qrcode_1724116372006(1)](https://github.com/user-attachments/assets/ae10606c-2a42-4486-8e6d-7b7d056ca8f4)
![支付宝](https://github.com/user-attachments/assets/3c686079-ddee-498b-9188-2639d0b7bbac)

## Star History  

[![Star History Chart](https://api.star-history.com/svg?repos=zongru666/PythonWebDemo&type=Timeline)](https://star-history.com/#zongru666/PythonWebDemo&Timeline)





