import time
from selenium import webdriver


def main(num_id: str, num_password: str):
    # browser = webdriver.Edge()

    # Webdriver地址
    chrome_driver = r"E:\Anaconda\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

    browser = webdriver.Chrome(executable_path=chrome_driver)

    browser.get('https://zlapp.fudan.edu.cn/site/ncovfudan/daily')

    element = browser.find_element_by_id('username')
    # 输入用户名
    element.send_keys(num_id)

    element = browser.find_element_by_id('password')
    # 输入密码
    element.send_keys(num_password)

    element = browser.find_element_by_xpath("//div[@class='IDCheckLoginFoot']/input[@id='idcheckloginbtn']")

    element.click()

    try:

        time.sleep(5)

        element = browser.find_element_by_xpath(
            '//div[@id="wapat"]//div[@class="wapat-btn-box"]//div[text()="已知晓(I understand)"]')
        element.click()

        time.sleep(5)
        element = browser.find_element_by_xpath('//input[@placeholder="点击获取地理位置"]')
        element.click()

        # time.sleep(5)
        # element = browser.find_element_by_xpath(
        #     '//div[@name="tw"]//span[text()="37.2℃以下（正常体温）"]/preceding-sibling::span[1]')
        # element.click()

        time.sleep(5)
        element = browser.find_element_by_xpath('//div[@class="footers"]//a[text()="提交信息 "]')
        element.click()

        time.sleep(5)
        element = browser.find_element_by_xpath('//div[@id="wapcf"]//div[text()="确认"]')
        element.click()
    finally:
        browser.close()
        return True


if __name__ == '__main__':
    # 输入学号和密码
    dic = {'id':'password'}
    for j in range(0, 2):
        for i in dic:
            try:
                main(i, dic[i])
            except:
                pass
