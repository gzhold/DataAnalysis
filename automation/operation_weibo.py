from selenium import webdriver
from lxml import etree
import requests


import time
browser = webdriver.Chrome()
# 登录微博
def weibo_login(username, password):
     # 打开微博登录页
     browser.get('https://passport.weibo.cn/signin/login')
     browser.implicitly_wait(5)
     time.sleep(1)
     # 填写登录信息：用户名、密码
     browser.find_element_by_id("loginName").send_keys(username)
     browser.find_element_by_id("loginPassword").send_keys(password)
     time.sleep(1)
     # 点击登录
     browser.find_element_by_id("loginAction").click()
     time.sleep(1)
# 设置用户名、密码
username = 'gzhold@126.com'
password = "Goodluck2011#"
weibo_login


# 添加指定的用户
def add_follow(uid):
    url = 'https://m.weibo.com/u/'+str(uid)
    # 请求头和目标网址
    headers = {
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    time.sleep(1)
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    dom = etree.HTML(r.text)

    #browser.find_element_by_id("follow").click()
    #follow_button = etree.find_element_by_xpath("/a[@class='W_btn_c btn_34px']")
    #follow_button.click()

    # 获取所有 li标签
    xpath_items = '/a[@class="W_btn_c btn_34px"]'
    # 获取所有的文章标签
    items = dom.xpath(xpath_items)
    print(items)


# 随机指定一个账户
uid = '1678434491'
add_follow(uid)


# 给指定某条微博添加内容
def add_comment(weibo_url, content):
     browser.get(weibo_url)
     browser.implicitly_wait(5)
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").clear()
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
     time.sleep(2)
     comment_button = browser.find_element_by_css_selector(".W_btn_a").click()
     time.sleep(1)


# 发文字微博
def post_weibo(content):
     # 跳转到用户的首页
     browser.get('https://weibo.com')
     browser.implicitly_wait(5)
     # 点击右上角的发布按钮
     post_button = browser.find_element_by_css_selector("[node-type='publish']").click()
     # 在弹出的文本框中输入内容
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
     time.sleep(2)
     # 点击发布按钮
     post_button = browser.find_element_by_css_selector("[node-type='submit']").click()
     time.sleep(1)


# 给指定的微博写评论
weibo_url = 'https://www.weibo.com/u/3465629360/home?topnav=1&wvr=6#1557321808536'
content = 'Gook Luck! 好运已上路！'
#add_comment(weibo_url, content);
# 自动发微博
content = '每天学点心理学'
#post_weibo(content)




