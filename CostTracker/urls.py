# urls.py
from django.urls import path
from .views import (
    CostDetailAPIView,
    CostListCreateAPIView,
    CostModelCreate,
    CostModelList,
    CostModelUpdate,
    CostModelDelete,
)

urlpatterns = [
    path("create/", CostModelCreate.as_view(), name="model_create"),
    path("list/", CostModelList.as_view(), name="model_list"),
    path("update/<int:pk>/", CostModelUpdate.as_view(), name="model_update"),
    path("delete/<int:pk>/", CostModelDelete.as_view(), name="model_delete"),
    path("api/costs/", CostListCreateAPIView.as_view(), name="cost-list-create"),
    path("api/costs/<int:pk>/", CostDetailAPIView.as_view(), name="cost-detail"),
]
