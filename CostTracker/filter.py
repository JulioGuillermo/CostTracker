import django_filters
from .models import Cost


class CostFilter(django_filters.FilterSet):
    class Meta:
        model = Cost
        fields = ["category", "amount", "date"]
