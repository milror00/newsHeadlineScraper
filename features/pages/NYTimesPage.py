import lxml
import pyautogui
import requests
import urllib
import hashlib
import pyscreenshot
from io import BytesIO
import time

from PIL import ImageGrab
from lxml import etree
from lxml import html
from selenium.webdriver.common.by import By

from features.configuration.configuration import Configuration
from features.pages.Page import Page



class NYTimesPage(Page):

    def __init__(self, context):
        self.browser = context.browser

    def getHeadline(self, context):
        details = {}
        config = Configuration()
        self.__getURL__(context)
        dom = lxml.html.parse(BytesIO(context.response.data))
        xpatheval = etree.XPathDocumentEvaluator(dom)
        xpath = './/*/h2/span'
        headline = xpatheval(xpath)
        headlineStr = headline[0].text  # or new.split()[index]
        hashedHeadline = hashlib.md5(headlineStr.encode()).hexdigest()
        self.getImage(context,config.getNYImagePath(),
                      hashedHeadline  , xpath,
                      config.getNYTimesImageReference(),
                      config.getNYImageRegion)
        headlines = {}
        headlines['newspaper'] = 'NYTIMES'
        headlines['headline'] = headline[0].text
        headlines['imageurl'] = hashedHeadline
        context.headlines.append(headlines)
        return True
        print("Latest NYTIMES headline scrape: \n" + context.headlines[0]['headline'])

    def clickAccept(self):
            self.click(By.XPATH, './/*[@data-testid="GDPR-accept"]' )
