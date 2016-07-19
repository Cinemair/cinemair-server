class NestedViewSetMixin:
    def get_queryset(self):
        return self._filter_queryset_by_parents_lookups(super().get_queryset())

    def _filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self._get_parents_query_dict()
        if parents_query_dict:
            return queryset.filter(**parents_query_dict)
        else:
            return queryset

    def _get_parents_query_dict(self):
        result = {}
        for kwarg_name in self.kwargs:
            if kwarg_name.startswith("parent_lookup_"):
                query_lookup = kwarg_name.replace("parent_lookup_", "", 1)
                query_value = self.kwargs.get(kwarg_name)
                result[query_lookup] = query_value
        return result
