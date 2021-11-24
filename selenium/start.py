from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

class start:
    def __init__(self,keyword,limit):
        self.keyWords = keyword         #키워드 입력
        self.limit = limit                  #사진 개수 제한

    def active(self):
        driver = webdriver.Chrome(executable_path="selenium\chromedriver.exe")
        driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
        elem = driver.find_element_by_name("q")
        elem.send_keys(self.keyWords)
        elem.send_keys(Keys.RETURN)

        # SCROLL_PAUSE_TIME = 1
        # # Get scroll height
        # last_height = driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     # Scroll down to bottom
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME)
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         try:
        #             driver.find_element_by_css_selector(".mye4qd").click()
        #         except:
        #             break
        #     last_height = new_height

        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        count = 0
        for image in images:
            if count == self.limit:
                break
            try:
                image.click()
                time.sleep(2)
                imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(imgUrl,self.keyWords + str(count+1) + ".jpg")
                count = count + 1
            except:
                pass

        driver.close()