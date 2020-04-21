class Configuration:

    def getEnvironment(self):
        return 'LIVE'

    def getBrowserType(self):
        return 'FIREFOX'


    def getURL(self, newspaper):
        if newspaper == 'fox':
            return 'https://www.foxnews.com/'

    def getTimeOut(self):
        return 10
