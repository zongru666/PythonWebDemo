'''
https://zhuanlan.zhihu.com/p/113372249
https://www.cnblogs.com/mafu/p/14158337.html

通过python+selenium+ChromeDriver实现自动登录网页和循环定时轮流切换标签展示
'''

# -*- coding:utf-8 -*-

# @Time : 2020/01/11 10:30

'''
update time ：2022/05/17 15：00 增加内外网地址注释，以备用
update time ：2021/06/29 19：00 配置到监控中心电脑
update time ：2021/06/25 08：30 新增可设置单个页面不同的停留时间
update time ：2021/01/22 14：20 初始化去掉保存密码弹窗，窗口最大化
update time ：2021/01/22 08：30 添加全屏模式和去掉顶部“受控”信息提示
update time ：2021/01/21 15：00 添加系统
'''

# @Author : zongru666

# @File : WebDemo.py




from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.support.ui import WebDriverWait

#from selenium.webdriver.common.action_chains import ActionChains

#导入时间参数
from parameters import time_of_all # 统一设置时间
from parameters import t1 # 系统1时间
from parameters import t2 # 系统2时间
from parameters import t3 # 系统3时间
from parameters import t4 # 系统4时间


def ChromeDemo():
    option = webdriver.ChromeOptions() #加载浏览器配置
    # option.add_argument('--kiosk') #启动时自动全屏（相当于在浏览器界面按F11按键，不与窗口最大化同时使用）
    # option.add_argument('disable-infobars') #浏览器不显示受自动测试软件控制 
    option.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
    driver=webdriver.Chrome(options=option) # 声明浏览器对象
    # driver=webdriver.Chrome() # 声明浏览器对象
    driver.maximize_window() # 最大化窗口（不与全屏模式同时使用）
    # 标签页0 系统1
    driver.get("http://你的网址") #输入外网地址，并发送请求到web服务器得到响应
    #driver.get("http://你的内网地址") #输入内网地址，并发送请求到web服务器得到响应

    driver.find_element_by_id("通过id找到账户框对应位置id").send_keys("你的账户名称") #系统1（通过手动在对应网页按F12，Elements，点击左上角箭头，再在页面点击需要找到的元素）通过id找到用户名输入框，输入用户名

    driver.find_element_by_id("通过id找到密码框对应位置id").send_keys("你的密码") #找到密码输入框，输入密码

    driver.find_element_by_name("通过id找到登录按钮位置id").click() #通过name找到登录按钮并点击登录
    
    #driver.execute_script("document.body.style.zoom='0.5'")
    driver.refresh()


    
    #新建标签页1 系统2
    newTab1 = 'window.open("http://你的网址");' #就当成js语句吧 数字化系统内网地址
    #newTab1 = 'window.open("http://你的网址");' #就当成js语句吧 数字化系统外网地址
    driver.execute_script(newTab1) #输出js语句
    driver.switch_to.window(driver.window_handles[1]) #切换到第二个标签页，第一个标签页为0

    driver.find_element_by_id("通过id找到账户框对应位置id").send_keys("你的账户名称") #找到用户名输入框，输入用户名

    driver.find_element_by_id("通过id找到密码框对应位置id").send_keys("你的密码") #找到用户名输入框，输入用户名

    driver.find_element_by_id("通过id找到登录按钮位置id").click() #通过id找到登录按钮并点击
    
    # driver.execute_script("document.body.style.zoom='0.8'")
    

    
    #新建标签页2 系统3
    #newTab2 = 'window.open("http://你的网址");' #就当成js语句吧 建管养系统内网
    newTab2 = 'window.open("http://你的网址");' #就当成js语句吧 建管养系统外网
    driver.execute_script(newTab2) #输出js语句
    driver.switch_to.window(driver.window_handles[2]) #切换到第三个标签页，第一个标签页为0

    driver.find_element_by_id("通过id找到账户框对应位置id").send_keys("你的账户名称") #找到用户名输入框，输入用户名

    driver.find_element_by_id("通过id找到密码框对应位置id").send_keys("你的密码") #找到用户名输入框，输入用户名

    driver.find_element_by_name("通过id找到登录按钮位置id").click() #通过id找到登录按钮并点击

    driver.execute_script("document.body.style.zoom='0.8'")
    

    
    #新建标签页3 系统4
    newTab3 = 'window.open("http://你的网址");' #就当成js语句吧 系统4 内网
    #newTab3 = 'window.open("http://你的网址");' #就当成js语句吧 系统4 外网
    driver.execute_script(newTab3) #输出js语句
    driver.switch_to.window(driver.window_handles[3]) #切换到第四个标签页，第一个标签页为0
    driver.find_element_by_id("通过id找到账户框对应位置id").send_keys("你们账户名称") #找到用户名输入框，输入用户名
    driver.find_element_by_id("通过id找到密码框对应位置id").send_keys("你的密码") #找到用户名输入框，输入用户名
    driver.find_element_by_xpath("通过xpath找到登录按钮位置完整xpath").click() #通过xpath（通过选择copy full Xpath）找到登录按钮并点击
    # driver.execute_script("document.body.style.zoom='0.8'")
    
    
    # 初始化（遍历每个标签，以去掉“保存密码弹窗”）,2021/01/25更改
    for k in driver.window_handles:
        driver.switch_to.window(k) # 循环切换标签
        time.sleep(1) # 等待（停留）时间


    if time_of_all==0: #当统一设定的时间为0，按单个系统的停留时间执行
        while 1:
            driver.switch_to.window(driver.window_handles[0]) #切换到第一个标签页，系统1
            time.sleep(t1)
            driver.switch_to.window(driver.window_handles[1]) #切换到第二个标签页，系统2
            time.sleep(t2)
            driver.switch_to.window(driver.window_handles[2]) #切换到第三个标签页，系统3
            time.sleep(t3)
            driver.switch_to.window(driver.window_handles[3]) #切换到第四个标签页，系统4
            time.sleep(t4)

    else: # 当统一设定的时间非0，按统一设定的时间执行
        while 1:
            for k in driver.window_handles:
                driver.switch_to.window(k) # 循环切换标签
                #driver.refresh()
                time.sleep(time_of_all) # 等待（停留）时间

    #driver.close() #关闭标签
    #driver.quit() #关闭浏览器


if __name__ == "__main__":
    ChromeDemo()
