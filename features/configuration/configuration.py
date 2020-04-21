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

    def getDBName(self):
        return 'test'

    def getTestTableName(self):
        return 'test'

    def getHost(self):
        return '127.0.0.1'

    def getTestTableName(self):
        return 'test'

    def getUsername(self):
        return ''

    def getPassword(self):
        return ''
