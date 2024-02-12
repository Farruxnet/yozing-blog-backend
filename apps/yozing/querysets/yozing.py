from django.db.models import QuerySet


class YozingQuerySet(QuerySet):

    def search(self, search=None):
        query = self
        return query
