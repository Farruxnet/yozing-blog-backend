from django.db.models import QuerySet


class CategoryQuerySet(QuerySet):
    def search(self, search):
        params = {}
        if search:
            params = {"name__icontains": search}
        query = self.filter(**params) if search else self
        return query
