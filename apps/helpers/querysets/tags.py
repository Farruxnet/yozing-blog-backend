from django.db.models import QuerySet


class TagQuerySet(QuerySet):
    def search(self, search=None):
        params = {}
        if search:
            params = {"name__icontains": search}
        query = self.filter(**params) if search else self
        return query

