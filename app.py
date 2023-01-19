from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Youtube:
    def __init__(self):
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("https://www.youtube.com/")
    
    
    def start(self):
        link = []
        i = 3
        screen_height = self.driver.execute_script("return window.screen.height;")
        while len(link) < 500:
            self.driver.implicitly_wait(5)
            self.driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 3
            sleep(3)
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;") 
            
            content = self.driver.find_element(By.ID, "contents")
            video = content.find_elements(By.ID, "thumbnail")
            
            for each_video in video:
                vid_link = each_video.get_attribute("href")
                link.append(vid_link)
                
        print("Final length is: ", len(link))
        
        return link
    
    
    def open_link(self, links):
        self.driver.implicitly_wait(5)
        for link in links:
            self.driver.get(link)
            


if __name__== '__main__':
    bot = Youtube()
    links = bot.start()
    bot.open_link(links)