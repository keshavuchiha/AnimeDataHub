
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



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
        # details=self.names.text.split('\n')
        # print(details[0].split(':'))
        # info=getInfo(details)

        # print(info)
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
