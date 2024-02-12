from django.db.models import QuerySet


class YozingQuerySet(QuerySet):

    def search(self, search=None):
        query = self
        return query

    def my_posts(self, user):
        query = self.filter(created_by=user)
        return query

    def users_posts(self, user_id):
        query = self.filter(created_by__id=user_id)
        return query
