
import re
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


from Anime.getLinks import Links
from Anime.utils.getInfo import getInfo
class MoreInfo():
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def synopsis(self):
        WebDriverWait(self.driver,timeout= 15).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="panelplace"]')))
        self.synopsis=self.driver.find_element(By.XPATH,'//div[@id="panelplace"]')
        print('synopsis')
        print(self.synopsis.get_attribute('innerHTML'))
        pass
    
    def details(self):
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//span[@id="addInfo"]')))
        # sleep(2)
        self.details=self.driver.find_element(By.XPATH,'//span[@id="addInfo"]')
        print('details')
        print(self.details.text)
        details=self.details.text.split('\n')
        print(details[0].split(':'))
        info=getInfo(details)

        print(info)     
    def names(self):
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//span[@id="addTitle"]')))
        # sleep(2)
        self.names=self.driver.find_element(By.XPATH,'//span[@id="addTitle"]')
        print('names')
        print(self.names.text)
        names=self.names.text.split('\n')
        print(names)
    def relatedTab(self):
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//li[@id="relatebtn"]')))
        # sleep(2)
        related=self.driver.find_element(By.XPATH,'//li[@id="relatebtn"]')
        # print('related')
        # print(related.text)
        related.click()
        # names=self.names.text.split('\n')
        # print(names)

        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//div[@id="panelplace"]')))
        # sleep(2)
        self.related=self.driver.find_element(By.XPATH,'//div[@id="panelplace"]')
        print('related')
        print(self.related.text)
        # self.related.click()
        relatedData=self.related.text.split('\n\n')
        info={}
        for data in relatedData:
            data=data.split(':',1)
            data[0]=data[0].strip()
            data[1]=data[1].split('\n')
            for i in range(len(data[1])):
                data[1][i]=data[1][i][2:]
            data[1]=data[1][1:]
            info[data[0]]=data[1]
        print(info)

        pass
    def similarTab(self):
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//li[@id="recombtn"]')))
        # sleep(2)
        similar=self.driver.find_element(By.XPATH,'//li[@id="recombtn"]')
        # print('related')
        # print(related.text)
        similar.click()
        # names=self.names.text.split('\n')
        # print(names)

        WebDriverWait(self.driver,timeout= 15).until(EC.visibility_of_all_elements_located((By.XPATH,'//p[@class="name"]')))
        # sleep(2)
        self.similar=self.driver.find_elements(By.XPATH,'//p[@class="name"]//a')
        print('similar')
        print(self.similar[0].text)

        l=[]
        for t in self.similar:
            l.append(t.text.strip())
        print(l)
        pass
    def opEndTab(self):
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//li[@id="songbtn"]')))
        # sleep(2)
        opend=self.driver.find_element(By.XPATH,'//li[@id="songbtn"]')
        opend.click()

        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//div[@id="panelplace"]')))
        self.songs=self.driver.find_element(By.XPATH,'//div[@id="panelplace"]')
        print('songs')
        print(self.songs.text)
        # self.related.click()
        songsData=self.songs.text.split('\n\n')
        info={}
        for data in songsData:
            data=data.split(':',1)
            data[0]=data[0].strip()
            data[1]=data[1].split('\n')
            for i in range(len(data[1])):
                data[1][i]=data[1][i][2:].strip()
                data[1][i]=re.sub(r'\(eps[^)]*\)\s*Play$','',data[1][i])
                if(data[1][i][-4:]=='Play'):
                    data[1][i]=data[1][i][:-4]
                data[1][i]=data[1][i].strip()
            data[1]=data[1][1:]
            info[data[0]]=data[1]
        print(info)
    
    def trailerTab(self):

        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//li[@id="traillerbtn"]')))
        # sleep(2)
        trailer=self.driver.find_element(By.XPATH,'//li[@id="traillerbtn"]')
        trailer.click()

        WebDriverWait(self.driver,timeout= 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="iframeanime"]')))
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//iframe')))
        self.trailer=self.driver.find_element(By.XPATH,'//iframe')
        # self.trailer=self.driver.find_element(By.XPATH,'//*[@id="iframeanime"]')
        # print(self.trailer.get_attribute('src'))
        print(self.trailer.get_attribute('src'))

        # self.related.click()
        self.driver.switch_to.default_content()
        pass
    def images(self):

        # //img[@id="maincoverimage"]
        # //div[@id="picViewer"]
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//img[@id="maincoverimage"]')))
        # sleep(2)
        animeImages=self.driver.find_element(By.XPATH,'//img[@id="maincoverimage"]')
        animeImages.click()

        WebDriverWait(self.driver,timeout= 15).until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@id="picViewer"]//img')))
        self.images=self.driver.find_elements(By.XPATH,'//div[@id="picViewer"]//img')
        for image in self.images:
            print(image.get_attribute('src'))
        # self.driver.switch_to.default_content()
        pass
    def comments(self):
        # //button[@id="showcommentbtn"]
        # //div[@class="load-more"]/a
        WebDriverWait(self.driver,timeout= 15).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="showcommentbtn"]')))
        commentBtn=self.driver.find_element(By.XPATH,'//button[@id="showcommentbtn"]')
        commentBtn.click()
        sleep(2)
        WebDriverWait(self.driver,timeout= 15).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//iframe[@title="Disqus" and @src]')))
        # print(self.driver.page_source)
        
       
        WebDriverWait(self.driver,timeout= 15).until(EC.presence_of_element_located((By.XPATH,'//div[@class="load-more"]/a')))
        print(self.driver.find_elements(By.XPATH,'//div[@class="post-message "]')[2].text)
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
            # if(curr==height):
            #     print(curr)
            #     print(height)
            #     break
            # height=curr
            # try:
            #     if(self.driver.find_element(By.XPATH,'//div[@class="load-more" and @style]/a')):
            #         print('no element found')
            #         break
            # except NoSuchElementException:
            #     continue
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver,timeout= 15).until(EC.visibility_of_all_elements_located((By.XPATH,'//li[@class="post"]/ancestor-or-self::li')))
        # sleep(5)
        parents=self.driver.find_elements(By.XPATH,'//li[@class="post"]/ancestor-or-self::li')
        children=self.driver.find_elements(By.XPATH,'//li[@class="post"]')

        # comments_text=self.driver.find_elements(By.XPATH,'//div[@class="post-message "]')
        # for comment in comments_text:
        #     print(comment.text)
        # p=[]
        # c=[]
        # cnt=0
        # for i in range(len(children)):
        #     # print(parents[i].get_attribute('id'),end=':')
        #     # print(children[i].get_attribute('id'))
        #     if(parents[i].get_attribute('id')!=children[i].get_attribute('id')):
        #         print(parents[i].text)
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
        pass