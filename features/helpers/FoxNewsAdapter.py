from datetime import datetime
import hashlib
from features.helpers.NewspaperAdapter import NewspaperAdapter


class FoxNewsAdapter(NewspaperAdapter):

    def headlineExist(self, context, imageurl):
        query = 'SELECT imageurl from headlines WHERE newspaper = "FOXNEWS" ORDER BY headlinedate DESC LIMIT 1  '
        record = self.getRecords(context, query)
        return imageurl == record[0][0]

    def getLatestHeadline(self, context, newspaper):
        query = 'SELECT headline from headlines WHERE newspaper = "'+ newspaper + '" ORDER BY headlinedate DESC LIMIT 1  '
        record = self.getRecords(context, query)
        return record

    def getAllHeadlines(self, context):
        query = 'SELECT * from headlines WHERE newspaper = "FOXNEWS"  '
        records = self.getRecords(context, query)
        return records

    def insertNewsheadline(self, context):
        sql = "INSERT INTO headlines (newspaper, headline, imageurl, headlinedate) " + \
              "VALUES('" + context.headlines[0]['newspaper']+ "'," + \
              "'" + context.headlines[0]['headline'].replace("'","\'") + "'," + \
              "'" + context.headlines[0]['imageurl'] + "'," + \
              "'" + self.__getNow__()  +"')"
        while self.headlineExist(context, context.headlines[0]['imageurl']) == False:
               if not self.insertRecord(context, sql):
                   exit(-1)

    def asText(self, context):
        print("Latest FOXNEWS headline scrape: \n" + context.headlines[0]['headline'])