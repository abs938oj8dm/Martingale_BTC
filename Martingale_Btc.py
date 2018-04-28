#coding: utf-8

from selenium import webdriver
#import os

#認証情報を環境変数から受け取る。
#USER = os.environ['']
#PASS = os.environ['']
USER = ''
PASS = ''

driver = webdriver.Chrome(executable_path='chromedriver')
driver.implicitly_wait(5)

def Login():
    driver.get('https://freebitco.in/')
    driver.find_element_by_css_selector('body > div.large-12.fixed > div > nav > section > ul > li.login_menu_button > a').send_keys('\n')
    driver.implicitly_wait(5)

    driver.find_element_by_css_selector("input[id='login_form_btc_address']").send_keys(USER)
    driver.find_element_by_css_selector("input[id='login_form_password']").send_keys(PASS)
    driver.find_element_by_css_selector('button#login_button.new_button_style.profile_page_button_style.center').send_keys('\n')
    driver.find_element_by_css_selector('#fp_multiplier_bonuses_main_div > div > p:nth-child(1) > a.bold.double_your_btc_link.double_your_btc_link2').send_keys('\n')

def Martingale():
    driver.find_element_by_css_selector('#double_your_btc_bet_hi_button').send_keys('\n')
    while True:
        if driver.find_element_by_id('double_your_btc_bet_win').text != "" and driver.find_element_by_id('double_your_btc_bet_lose').text == "":
            driver.find_element_by_css_selector('#double_your_btc_min').send_keys('\n')
            driver.find_element_by_css_selector('#double_your_btc_bet_hi_button').send_keys('\n')
        elif driver.find_element_by_id('double_your_btc_bet_win').text == "" and driver.find_element_by_id('double_your_btc_bet_lose').text != "":
            driver.find_element_by_css_selector('#double_your_btc_2x').send_keys('\n')
            driver.find_element_by_css_selector('#double_your_btc_bet_hi_button').send_keys('\n')

if __name__ == "__main__":
    Login()
    Martingale()