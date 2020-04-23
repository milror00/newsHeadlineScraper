import time

import pyautogui
import urllib3
from PIL import ImageGrab

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from features.configuration.configuration import Configuration


class Page():

    def __openBrowserURL__(self, uri):
        self.browser.get(uri)

    def __getURL__(self, context):
        http = urllib3.PoolManager()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        context.response = http.request('GET', context.currentURL,headers)

    def waitForPageLoaded(self, xpath):
        try:
            timeout = Configuration.getTimeOut(self)
            driver = self.browser
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except:
            raise

    def findElement(self, by, text):
        return self.browser.find_element(by, text)

    def click(self, by, text):
        element = self.findElement(by, text)
        element.click()

    def getImage(self, context,imagePath,imageName ,xpath,imageRef, imageRegion):
        config = Configuration()
        self.__openBrowserURL__(context.currentURL)
        self.waitForPageLoaded(xpath)
        time.sleep(3)
        self.clickAccept()
        image_save = imagePath + imageName + '.jpg'
        ref = imagePath+imageRef
        box = pyautogui.locateOnScreen(ref, grayscale=True)
        region = imageRegion
        x = imageRegion['x']
        y = imageRegion['y']+box[1]/2+100
        w = imageRegion['w']
        h = imageRegion['h']
        im = ImageGrab.grab(bbox=(x, y, x + w, y + h))
        im.save(image_save)