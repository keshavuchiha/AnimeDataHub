
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Anime.getLinks import Links
class VideoPage():
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def getEpisodeCount(self)->int:
        self.epCount=self.driver.find_element(By.XPATH,'//span[@id="epsavailable"]').get_attribute('innerHTML')
        print(self.epCount)
        return self.epCount
        pass
    def selectEpisode(self,epNum:int,link:str):
        # sleep(5)
        try:
            self.driver.get(f'{link}/ep{epNum}')
        except:
            print('not woring '+str(epNum))
            pass
        pass
    def getComments(self):
        # //button[@id="showcommentbtn"]
        # //div[@class="load-more"]/a
        try:
            self.driver.implicitly_wait(2)
            WebDriverWait(self.driver,timeout= 5).until(EC.visibility_of_element_located((By.XPATH,'//button[@id="showcommentbtn"]')))
            commentBtn=self.driver.find_element(By.XPATH,'//button[@id="showcommentbtn"]')
            self.driver.execute_script('arguments[0].scrollIntoView(true);',commentBtn)
            cmtCnt=self.driver.execute_script('return arguments[0].innerHTML',commentBtn);
            # cmtCnt=cmtCnt[4:]
            # cmtCnt=int(cmtCnt)
            print('no of comments '+cmtCnt)
            cmtCnt=int(cmtCnt[4:-8].strip())
            if(cmtCnt==0):
                return []
            self.driver.execute_script('arguments[0].click();',commentBtn)

            # sleep(2)
            WebDriverWait(self.driver,timeout= 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="Disqus" and @src]')))
            # print(self.driver.page_source)
            WebDriverWait(self.driver,timeout= 5).until(EC.presence_of_element_located((By.XPATH,'//div[@class="load-more"]/a')))
            # print(self.driver.find_elements(By.XPATH,'//div[@class="post-message "]')[2].text)
            loadCommentBtn= self.driver.find_element(By.XPATH,'//div[@class="load-more"]/a')
            
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while(True):
                # sleep(1)
                # try:
                #     # WebDriverWait(self.driver,timeout= 3).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="load-more" and @style]/a')))
                #     if(self.driver.find_element(By.XPATH,'//div[@class="load-more" and @style]/a')):
                #         print('no element found')
                #         break
                # except NoSuchElementException:
                #     continue
                
                # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # sleep(1)
                try:

                    WebDriverWait(self.driver,timeout= 3).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="load-more"]/a')))
                    
                    # print(self.driver.find_elements(By.XPATH,'//div[@class="post-message "]')[2].text)
                    loadCommentBtn= self.driver.find_element(By.XPATH,'//div[@class="load-more"]/a')
                    # self.driver.execute_script('arguments[0].scrollIntoView(true);',loadCommentBtn)
                    self.driver.execute_script('arguments[0].click();',loadCommentBtn)
                    sleep(1)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    
                    
                    print(new_height)
                    if(new_height==last_height):
                        break
                    last_height=new_height
                except:
                    break
                
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(self.driver,timeout= 15).until(EC.visibility_of_all_elements_located((By.XPATH,'//li[@class="post"]/ancestor-or-self::li')))
            # sleep(5)
            parents=self.driver.find_elements(By.XPATH,'//li[@class="post"]/ancestor-or-self::li')
            children=self.driver.find_elements(By.XPATH,'//li[@class="post"]')

            # //li[@class="post" and @id="post-5932989784"]//div[@class="post-message "]//div//p
            # messgae
            # //li[@class="post" and @id="post-5932989784"]//header[@class="comment__header"]//span[contains(@class,"author")]//a
            # author name
            # //li[@class="post" and @id="post-5932989784"]//img[@data-role="user-avatar"]
            # avatar
            # //li[@class="post" and @id="post-5932989784"]//header[@class="comment__header"]//span[@class="post-meta"]//a
            # time
            commentList=[]
            for i in range(len(children)):
                id=children[i].get_attribute('id')
                info={}
                info['id']=id
                info['parentId']=parents[i].get_attribute('id')
                info['message']=self.driver.find_element(By.XPATH,f'//li[@class="post" and @id="{id}"]//div[@class="post-message "]//div//p').text
                info['authorName']=self.driver.find_element(By.XPATH,f'//li[@class="post" and @id="{id}"]//header[@class="comment__header"]//span[contains(@class,"author")]//a').text
                info['authorId']=self.driver.find_element(By.XPATH,f'//li[@class="post" and @id="{id}"]//header[@class="comment__header"]//span[contains(@class,"author")]//a').get_attribute('data-username')
                info['authorAvatar']=self.driver.find_element(By.XPATH,f'//li[@class="post" and @id="{id}"]//img[@data-role="user-avatar"]').get_attribute('src')
                info['timeCreation']=self.driver.find_element(By.XPATH,f'//li[@class="post" and @id="{id}"]//header[@class="comment__header"]//span[@class="post-meta"]//a').get_attribute('title')
                print(info)
                commentList.append(info)
            return commentList
        except:
            return []
        
        pass
    def moreInfo(self):
        moreInfoBtn=self.driver.find_element(By.XPATH,'//*[text()="More info"]')
        self.driver.execute_script('arguments[0].scrollIntoView(true);',moreInfoBtn)
        self.driver.execute_script('arguments[0].click();',moreInfoBtn)
        


        
