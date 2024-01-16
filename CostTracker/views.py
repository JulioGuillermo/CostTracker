from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from .models import Cost
from .serializer import CostSerializer


class CostModelCreate(CreateView):
    model = Cost
    fields = [
        "category",
        "amount",
        "date",
        "file",
    ]
    success_url = reverse_lazy("model_list")


class CostModelUpdate(UpdateView):
    model = Cost
    fields = [
        "category",
        "amount",
        "date",
        "file",
    ]
    success_url = reverse_lazy("model_list")


class CostModelList(ListView):
    model = Cost
    context_object_name = "costs"


class CostModelDelete(DeleteView):
    model = Cost
    success_url = reverse_lazy("model_list")


class CostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
