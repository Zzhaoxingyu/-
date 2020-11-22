#!/usr/bin/env python
# encoding: utf-8
# @Author   : Xingyu Zhao
# @Software : Pycharm
# @File     : pafd.py
# @Time     : 2020/11/22 16:26
# @Desc     : Fudan University Pinganfudan Automatic check-in script

import time
from selenium import webdriver


def main(num_id: str, num_password: str):
    browser = webdriver.Edge()

    browser.get('https://zlapp.fudan.edu.cn/site/ncovfudan/daily')

    time.sleep(5)

    element = browser.find_element_by_id('username')
    # 输入用户名
    element.send_keys(num_id)

    element = browser.find_element_by_id('password')
    # 输入密码
    element.send_keys(num_password)

    element = browser.find_element_by_id('idcheckloginbtn')
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
    dic = {'Your student number': 'Your passwords'}
    for j in range(0, 2):
        for i in dic:
            try:
                main(i, dic[i])
            except:
                pass
