# RUC-Registrant

 Automatic registration of epidemic prevention and control.

selenium 实现的 RUC 疫情防控通电脑端自动登记脚本

### 所用库

1. selenium
2. win10toast (main_plus.py)

### 基本使用指南

0. 科学上网，Firefox 的定位服务都要科学上网才能正确访问，所以这个脚本必须科学上网运行，理论上你也可以用某些方法直接给它位置，但这违背了脚本的初衷
1. 配置好 selenium 火狐浏览器驱动（[配置方法](https://blog.csdn.net/hy_696/article/details/80114065)）
2. 在 setting.json 中输入账号密码信息用于登录
3. 运行 main.py (main_plus.py)

目前代码毫无鲁棒性，必须前一天登记过所以主要信息都保留，本代码只完成点一下"获取位置"和前后的自动化

登记失败会报错提醒，可能的原因有：账号密码错误，昨天忘记登记，导致部分信息缺失；网速太慢；网站改版

#### setting.json 说明

thresh_time : 通知停留在屏幕上的时间，单位：秒

log : 只对 main_plus.py 生效，0 表示低通知，即只在失败时通知；1 表示高通知，即登记失败，今日已登记，本次登记成功都通知，默认值为 1

### 进阶使用指南

main_plus.py 将尽量尝试静默执行，并改用 win10toast 库调用 win10 系统通知栏来显示通知

所以把 log 改成 0，把 main_plus.py 和科学上网设成开机自启，其中前者用创建快捷方式+最小化启动就能无感使用了

### 注意

脚本没有模拟定位的功能，对于他人对本代码修改导致的问题本人概不负责
