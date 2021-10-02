from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 

keyward = "検索する名前 or メールアドレスor etc（検索結果は１人のみ）"
message = "自動送信するメッセージ"

# make a driver by already opened chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

wait = WebDriverWait(driver, 15)

# get target URL
driver.get('https://teams.microsoft.com')

WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located)

# input keyward
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="searchInputField"]')))
EleSearch = driver.find_element_by_xpath('//*[@id="searchInputField"]')
EleSearch.clear()
EleSearch.send_keys(keyward)
EleSearch.send_keys(Keys.RETURN)

# click area of user
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-result-tabs"]/li[2]/a')))
driver.find_element_by_xpath('//*[@id="search-result-tabs"]/li[2]/a').click()

# click first user
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="peopleSearchContent-0"]/div/div[2]')))
driver.find_element_by_xpath('//*[@id="peopleSearchContent-0"]/div/div[2]').click()

# send message for user
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders')))
EleMsgBox = driver.find_element_by_css_selector('.cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders')
EleMsgBox.clear()
EleMsgBox.send_keys(message)
