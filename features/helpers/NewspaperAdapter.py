from features.helpers.Adapter import Adapter


class NewspaperAdapter(Adapter):

    def getAllDistinctNewspapers(self, context):
        query = 'SELECT DISTINCT newspaper from headlines '
        records = self.getRecords(context, query)
        return records


