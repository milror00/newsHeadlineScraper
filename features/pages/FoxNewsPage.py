
import lxml
import requests
import urllib
import hashlib
from io import BytesIO
from lxml import etree
from lxml import html
from features.pages.Page import Page

class FoxNewsPage(Page):

    def getHeadline(self, context):
        details = {}
        self.__getURL__(context)
        dom = lxml.html.parse(BytesIO(context.response.data))
        xpatheval = etree.XPathDocumentEvaluator(dom)
        headline =  xpatheval('.//*[@class="article story-1"]/div[2]/header/h2/a')
        image = xpatheval('.//*[@class="article story-1"]//img/@src')[1]
        headlines = {}
        headlines['headline'] = headline[1].text
        headlines['image'] = image
        headlines['hash'] = hashlib.md5(headline[1].text.encode('utf-8'))
        context.headlines.append(headlines)
        return True