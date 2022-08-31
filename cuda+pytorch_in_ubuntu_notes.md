#cuda
##ubuntu系统禁用自带NVIDIA Nouveau驱动
1. 打开黑名单
sudo gedit /etc/modprobe.d/blacklist-nouveau.conf
2. 添加两行语句
blacklist nouveau  
options nouveau modeset=0
3. 更新initramfs
sudo update-initramfs -u
4. 重启
reboot
5. 验证，终端输入语句
lsmod | grep nouveau
没有显示结果表示禁用成功

##安装驱动：
1. 直接使用系统推荐安装
sudo ubuntu-drivers autoinstall
2. 重启系统
reboot
3. 查看驱动信息
nvidia-smi
4. 测试
nvidia-settings

##安装cuda
* 下载cuda
根据电脑系统配置信息下载相应版本(尽量打开vps)[cuda-download](https://developer.nvidia.com/cuda-toolkit-archive)
* example
wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda_11.7.1_515.65.01_linux.run
sudo sh cuda_11.7.1_515.65.01_linux.run  
 
本次下载的cuda版本为11.7.1，当运行安装程序后会进入安装界面，因为前面已经安装过驱动，因此安装驱动选项可以不选

* 安装完成后需要配置相关环境变量
vim ~/.bashrc
添加cuda安装地址（该地址会在cuda安装成功后给出）
export LD\_LIBRARY\_PATH=\$LD\_LIBRARY\_PATH:/usr/local/cuda-11.7/lib64
export PATH=\$PATH:/usr/local/cuda-11.7/bin
export CUDA\_HOME=\$CUDA\_HOME:/usr/local/cuda-11.7
* 验证是否安装成功
nvcc -V
出现相应版本信息表示安装成功

####cuda安装遇到的坑

在完成安装之后打开NVIDIA visual profile程序如果出现Java jre包不存在问题进行如下解决：
* sudo apt-get install libcanberra-gtk*
* sudo apt install openjdk-8-jdk

##安装pytorch

* 下载pytorch
根据电脑系统配置信息下载相应版本(尽量打开vps)[pytorch-download](https://pytorch.org/get-started/locally/)
* example
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116





