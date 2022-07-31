import os
import typing
import types
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from slugify import slugify
import Anime.constants as const
from Anime.listPage import ListPage 
class Anime(webdriver.Chrome):
    def __init__(self):
        super(Anime,self).__init__(ChromeDriverManager().install())
        self.implicitly_wait(10)
        self.maximize_window()
    def __exit__(self, exc_type: typing.Optional[typing.Type[BaseException]], exc: typing.Optional[BaseException], traceback: typing.Optional[types.TracebackType]):
        self.quit()
    def AZList(self):
        link=self.find_element(By.XPATH,'//a[@title="A-Z List"]')
        link.click()
        page=ListPage(driver=self)
        # page.startChar('K')
        azlist=['#']
        for i in range(ord('A'),ord('Z')+1):
            azlist.append(chr(i))
        # print(azlist)       
        for i in azlist:
            if not os.path.exists(os.path.join(const.BASE_FOLDER,'data',i.upper())):
                os.makedirs(os.path.join(const.BASE_FOLDER,'data',i.upper()))
            if os.path.exists(os.path.join(const.BASE_FOLDER,'data',i.upper(),'completed.txt')):
                continue
            page.startChar(i) 
            with open(os.path.join(const.BASE_FOLDER,'data',i.upper(),'completed.txt'),'w+') as f:
                f.write(f'{i} completed')
            self.get('https://animixplay.to/list')
    def landingPage(self):
        self.get(const.BASE_URL)
        