

# <center>欢迎使用JamYidoSystem 发卡系统 #
![Docker Image Version (latest by date)](https://img.shields.io/docker/v/huyihe/jamyidosystem-faka?label=docker%20version&style=for-the-badge) 
![Docker Automated build](https://img.shields.io/docker/automated/huyihe/jamyidosystem-faka?style=for-the-badge&color=brightgreen) 
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/huyihe/jamyidosystem-faka?style=for-the-badge) 
![GitHub release (latest by date)](https://img.shields.io/github/downloads/HuYihe2008/JamYidoSystem-faka/latest/total?style=for-the-badge) 
![GitHub](https://img.shields.io/github/license/HuYihe2008/JamYidoSystem-faka?style=for-the-badge) 
![GitHub followers](https://img.shields.io/github/followers/HuYihe2008?style=for-the-badge) 
![GitHub forks](https://img.shields.io/github/forks/Huyihe2008/jamyidosystem-faka?style=for-the-badge) 
![GitHub Repo stars](https://img.shields.io/github/stars/Huyihe2008/jamyidosystem-faka?style=for-the-badge) 
![GitHub watchers](https://img.shields.io/github/watchers/Huyihe2008/jamyidosystem-faka?style=for-the-badge) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Huyihe2008/jamyidosystem-faka?style=for-the-badge)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Huyihe2008/jamyidosystem-faka?style=for-the-badge)
![作者](https://img.shields.io/badge/%E4%BD%9C%E8%80%85-%E4%BA%91%E5%A0%87%EF%BC%88JamYido%EF%BC%89-red?style=for-the-badge)

---

### [反馈](https://github.com/HuYihe2008/JamYidoSystem-Faka/discussions) 

---

## 适用场景：
适用于各种邀请码、充值卡、激活码、注册码、腾讯爱奇艺积分CDK等，支持手工和全自动发货。

## 功能特色：

- Stisla UI：web界面很漂亮
- 前端使用VUE3.0,毫秒级响应
- 已集成支付宝当面付、微信官方、Payjs、虎皮椒、YunGouOS、易支付、Mugglepay、码支付等十几种支付接口
- 普通用户支持邮箱、短信接收消息
- 管理员支持邮箱、短信、微信通知
- 支持2~4层批发模式
- 长卡密可导出为txt文本
- 多种主题模式【列表、卡片、宫格】
- 支持自定义背景、标题、关键词等
- 支持热备份，可一键云端备份、一键导出备份文件到本地
- 数据库可分离，兼容Mysql、PostgreSQL和Sqlite(比较麻烦)
- 支持移动端唤醒支付宝
- JWT保证后台接口安全
- Limter保障服务器访问频率和次数

## 部署方法：

### 一、正式上线部署

### 1.使用宝塔docker镜像管理器 

    1.进入宝塔，打开软件商店，搜索docker

    2.安装完毕后进入dockers管理器，点击镜像管理，点击镜像搜索，输入“huyihe/jamyidosystem-faka”即可拉取镜像

    3.部署镜像

    4.记得开通端口8000至主机任意端口

### 2.快速命令
```bash
    #安装命令
    docker run -d \
    -p 8000:8000 \
    --restart=always \
    --name=loacltest \
    -e DB_TYPE=Mysql \
    -e DB_HOST=43.154.43.164 \
    -e DB_PORT=3306 \
    -e DB_USER=key_jamyido \
    -e DB_PASSWORD=Hyh386855867 \
    -e DB_DATABASE=key_jamyido \
    huyihe/jamyidosystem-faka
    
    #然后你可一使用http://服务器IP:8000/  访问面板
```

## Github社区讨论

项目已开通专属社区,主要集中开发者计划、BUG反馈、新功能建议等，欢迎积极参与讨论，[点此进入](https://github.com/HuYihe2008/JamYidoSystem-faka/discussions) 

### 项目依赖
- 前端UI：Stisla --> https://github.com/stisla/stisla
- 前端交互程序：vue3.0 --> https://github.com/vuejs/vue-next
- 后端：Flask --> https://github.com/pallets/flask
- 管理员接口：Flask-JWT --> https://flask-jwt-extended.readthedocs.io/en/stable/

## License

本程序使用MIT协议，您可以免费使用，复制或修改软件，但是请保留底部作者信息和License许可声明。
