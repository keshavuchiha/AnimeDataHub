
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Anime.getLinks import Links
class VideoPage():
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def getEpisodeCount(self):
        self.epCount=self.driver.find_element(By.XPATH,'//span[@id="epsavailable"]').get_attribute('innerHTML')
        print(self.epCount)
        pass
    def getComments(self):
        commentBtn=self.driver.find_element(By.XPATH,'//button[@id="showcommentbtn"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);',commentBtn)
        self.driver.execute_script('arguments[0].click();',commentBtn)
        pass
    def Video(self):
        pass
    def moreInfo(self):
        moreInfoBtn=self.driver.find_element(By.XPATH,'//*[text()="More info"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);',moreInfoBtn)
        self.driver.execute_script('arguments[0].click();',moreInfoBtn)
        


        
