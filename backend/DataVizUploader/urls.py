
from .views import FileUploadListCreateView, FileUploadDestroyView, FinancialDataListView
from django.urls import path

urlpatterns = [
    path('files', FileUploadListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>', FileUploadDestroyView.as_view(), name='file-retrieve-destroy'),
    path('files/<int:pk>/financial-data', FinancialDataListView.as_view(), name='financial-data-list'),
]