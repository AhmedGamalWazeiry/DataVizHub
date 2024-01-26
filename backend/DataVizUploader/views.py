from rest_framework.generics import ListCreateAPIView, DestroyAPIView,RetrieveDestroyAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser,FileUploadParser
from .models import FinancialDataSet,FinancialFile 
from .serializers import FinancialFileSerializer,FinancialDataSetSerializer
from .utils import process_csv_file

class FileUploadListCreateView(ListCreateAPIView):
    queryset = FinancialFile.objects.all() 
    serializer_class = FinancialFileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        # Handle the uploaded file here
        
        uploaded_file = serializer.validated_data['file']
        process_csv_file(uploaded_file)
        print(type(uploaded_file))
        # Process or save the file as needed
        serializer.save()

class FileUploadDestroyView(DestroyAPIView):
    serializer_class = FinancialFileSerializer
    queryset = FinancialFile.objects.all()
    lookup_field = "id"


class FinancialDataListView(ListAPIView):
    serializer_class = FinancialDataSetSerializer
   
