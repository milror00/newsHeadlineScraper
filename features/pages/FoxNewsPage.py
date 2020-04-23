
import lxml
import requests
import urllib
import hashlib
from io import BytesIO
from lxml import etree
from lxml import html

from features.configuration.configuration import Configuration
from features.pages.Page import Page

class FoxNewsPage(Page):

    def __init__(self, context):
        self.browser = context.browser

    def clickAccept(self):
        pass

    def getHeadline(self, context):
        details = {}
        config = Configuration()
        self.__getURL__(context)
        dom = lxml.html.parse(BytesIO(context.response.data))
        xpatheval = etree.XPathDocumentEvaluator(dom)
        xpath = './/*[@class="article story-1"]/div[2]/header/h2/a'
        headline =  xpatheval(xpath)
        headlineStr = headline[0].text
        hashedHeadline = hashlib.md5(headlineStr.encode()).hexdigest()
        self.getImage(context,config.getFoxNewsPath(),
                      hashedHeadline , xpath,
                      config.getFoxNewsImageReference(),
                      config.getFoxNewsImageRegion)

        headlines = {}
        headlines['newspaper'] = 'FOXNEWS'
        headlines['headline'] = headline[1].text
        headlines['imageurl'] = hashedHeadline
        context.headlines.append(headlines)
        return True

    def asText(self, context):
        print("Latest FOXNEWS headline scrape: \n" + context.headlines[0]['headline'])