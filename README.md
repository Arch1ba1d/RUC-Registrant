# Registrant

 Automatic registration of epidemic prevention and control.

selenium 实现的 RUC 疫情防控通电脑端自动登记脚本

### 所用库

1. selenium
2. win10toast (main.pyz)

### 基本使用指南

(有个很BUG的问题，Chrome 和 Firefox 的定位服务都要科学上网才能正确访问，所以这个脚本必须科学上网运行，理论上你也可以用其他方法直接给它定位信息，就不用调服务了，但这违背了这个脚本的初衷)

在 setting.json 中输入账号密码信息用于登录，运行 main.py

目前鲁棒性很低，必须前一天登记过所以主要信息都保留，本代码只完成点一下''获取位置"和前后的自动化

登记失败会报错提醒，可能的原因有：账号密码错误，昨天忘记登记，导致部分信息缺失；网速太慢；网站改版

### 进阶使用指南

main.pyz 不显示 console，并改用 win10toast 库调用 win10 系统通知栏来显示通知

所以把 log 改成0，把 main.pyz 设成开机自启就能无感登记了

#### setting.json 说明

thresh_time : 通知停留在屏幕上的时间，单位秒

log : 只对 main.pyz 生效，0 表示低通知，即只在失败时通知；1 表示高通知，即登记失败，今日已登记，本次登记成功都通知

### 注意

1. 浏览器驱动是火狐浏览器
2. 不带模拟定位的功能，对于修改代码导致的问题本人不负责
