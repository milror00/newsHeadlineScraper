class Configuration:

    def getEnvironment(self):
        return 'LIVE'

    def getBrowserType(self):
        return 'FIREFOX'


    def getURL(self, newspaper):
        if newspaper == 'FOXNEWS':
            return 'https://www.foxnews.com/'

    def getNYImagePath(self):
        return "C:\\Users\\oem\\Desktop\\NYTimesImages\\"

    def getNYTimesImageReference(self):
        return('1587647485058.png')

    def getFoxNewsPath(self):
        return "C:\\Users\\oem\\Desktop\\FoxNewsImages\\"

    def getFoxNewsImageReference(self):
        return('1587650858881.png')

    def getTimeOut(self):
        return 10

    def getDBName(self):
        return 'test'

    def getHost(self):
        return '127.0.0.1'

    @property
    def getNYImageRegion(self):
        return {'x':630,'y':300,'h':325,'w':475}

    @property
    def getFoxNewsImageRegion(self):
        return {'x':580,'y':70,'h':320,'w':760}


