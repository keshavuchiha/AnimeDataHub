import imp
import types
import typing
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import AnimeProject.Constants as const
class Anime(webdriver.Chrome):
    def __init__(self,teardown=False):
        super(Anime,self).__init__(ChromeDriverManager().install())
        self.teardown=teardown
        self.implicitly_wait(10)
        self.maximize_window()
    
    def __exit__(self, exc_type: typing.Optional[typing.Type[BaseException]], exc: typing.Optional[BaseException], traceback: typing.Optional[types.TracebackType]):
        if(self.teardown):
            self.quit()

    def landingPage(self):
        self.get(const.BASE_URL)

