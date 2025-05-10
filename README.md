Linux16 (Install Oracle VirtualBox on Window), Ubuntu 16.04LTS (Xenial Xerus 64-bit)
Base Memory : 5538MB, Processors : 6, Video Memory : 16MB, Graphics Controller: VBoxVGA, Storage Controller : IDE;IDE Secondary Device 0: [OPtical Drive] Empty, Storage Controller : SATA; SATA Port 0: linux16.vdi (Normal, 31.93GB)
Network : Intel PRO/1000 MT Desktop (Bridged Adapter, Intel(R) Wi-Fi 6E AX211 160MHz)



Python3 version : Python 3.11.8
Python2 version : Python 2.7.12
pynaoqi-python2.7-2.5.7.1-linux64

Terminal 1 :
cd /home/yujin/Desktop/Web/screenHTML/Scenario; python3 -m http.server 8000

Terminal 2 :
export PYTHONPATH=${PYTHONPATH}:/home/yujin/Desktop/robot/pepperchat/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages ; export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:/home/yujin/Desktop/robot/pepperchat/pynaoqi-python2.7-2.5.7.1-linux64/lib ; export QI_SDK_PREFIX=/home/yujin/Desktop/robot/pepperchat/pynaoqi-python2.7-2.5.7.1-linux64

python3 Ex_main_app.py

Pepper : Ex_main_app.py로 연 로컬 웹페이지에서 스크린 이미지 띄울 수 있음
Double : http://10.134.71.207:8080/ (더블 ip주소) 에서 Accessary web view 부분에 http://리눅스 ip주소:8000/원하는 html 이름 하고 open 누르면 이미지 띄울 수 있음

