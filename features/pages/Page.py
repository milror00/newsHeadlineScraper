import urllib3


class Page():

    def __getURL__(self, context):
        http = urllib3.PoolManager()
        context.response = http.request('GET', context.currentURL)