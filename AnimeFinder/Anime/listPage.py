
from time import sleep
import time
from slugify import slugify
import numpy as np
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
from Anime.getLinks import Links
from Anime.VideoPage import VideoPage
from Anime.MoreInfo import MoreInfo
class ListPage():
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def startChar(self,char:str):
        res=[]
        char=char[0].upper()
        # self.driver.find_element(By.XPATH,f'//button[text()="{char}"]')
        # sleep(2)
        
        print(f'//button[text()="{char}"]')
        xpath=f'//button[text()="{char}"]'
        WebDriverWait(self.driver,timeout= 20).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="listplace"]/div')))
        print('waited')
        link=self.driver.find_element(By.XPATH,xpath)
        link.click()

        anime=self.driver.find_elements(By.XPATH,'//div[@id="listplace"]/div')
        print(anime[2].text)
        # //div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub"))]
        subAnime=self.driver.find_elements(By.XPATH,'//div[@id="listplace"]/div[text()="GOGO"]/a[not(contains(@title,"Dub"))]')
        animeLinkList=[]
        
        for anime in subAnime:
            # print(anime.get_attribute('innerHTML'))
            # btn
            animeLinkList.append(anime.get_attribute('href')) 
            # if(anime.get_attribute('innerHTML')=='Kimetsu no Yaiba'):
                
                
            #     print(anime.get_attribute('href'))

            #     btn=anime
        # print(animeLinkList)    
        # self.driver.execute_script('arguments[0].scrollIntoView(true);',btn)
        # self.driver.execute_script('arguments[0].click();',btn)
        
        for link in animeLinkList:
            self.driver.get(link)
            temp=link.split('/')
            videoPage=VideoPage(self.driver)
            # sleep(2)
            epCount=int(videoPage.getEpisodeCount())
            # sleep(2)
            comments=[]
            for i in range(epCount):
                videoPage.selectEpisode(i+1,link)
                sleep(2)
                comment=videoPage.getComments()
                comments.append(comment)
            print(comments)
            res.append([comments,link])
        
        # np.save('temp.npy',res)
        resjson=json.dumps(res)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)
        print(res)
        # self.driver.get(animeLinkList[105])
        
        # # sleep(5)
        # videoPage=VideoPage(self.driver)
        # # videoPage.selectEpisode(3)
        # # videoPage.getComments()
        # videoPage.getEpisodeCount()
        # videoPage.selectEpisode(3)


        # iterate in episode
        # get its comments store in database
        # more info


            # moreInfo=MoreInfo(self.driver)
            # # moreInfo.synopsis()
            # moreInfo.details()


        


        
