from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('D:\VSCODE\PythonoweLove\chromedriver.exe')
browser.maximize_window()
browser.delete_all_cookies()
browser.get("https://www.youtube.com")

song_name='Rick Astley - Never Gonna Give You Up (Official Music Video)'

sleep(2)

acc_butt = browser.find_element(By.PARTIAL_LINK_TEXT, 'ZAAKCEPTUJ')
acc_butt.click()

sleep(2)

search_input = browser.find_element(By.NAME, 'search_query')
search_input.send_keys(song_name)

sleep(2)

search_butt = browser.find_element(By.ID, 'search-icon-legacy')
search_butt.click()

sleep(3)

play_ricky = browser.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
play_ricky.click()

sleep(3)

action = ActionChains(browser)
action.send_keys('f').perform()