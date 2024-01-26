from rest_framework.generics import ListCreateAPIView, DestroyAPIView,RetrieveDestroyAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser,FileUploadParser
from .models import FinancialDataSet,FinancialFile 
from .serializers import FinancialFileSerializer,FinancialDataSetSerializer
from .utils import process_csv_file,insert_data_into_financial_data_set

class FileUploadListCreateView(ListCreateAPIView):
    queryset = FinancialFile.objects.all() 
    serializer_class = FinancialFileSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uploaded_file = serializer.validated_data['file']
        try:
            return_data_object = process_csv_file(uploaded_file)
        except Exception as e:
            return Response('An unexpected error occurred during processing the CSV file.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
           
        
        if return_data_object['is_error']:
            return Response(return_data_object['error_message'], status=status.HTTP_400_BAD_REQUEST)
        
        data_frame = return_data_object["data_frame"]
        
        print(data_frame)
        last_three_columns = data_frame.iloc[:, -3:]

        # Convert the DataFrame to a list of dictionaries
        result_list = last_three_columns.to_dict(orient='list')
        
        file = serializer.save()
        
        try:
            insert_data_into_financial_data_set(return_data_object['data_frame'],file)
        except Exception as e :
            return Response(return_data_object['An unexpected error occurred during storing the data.'], status=status.HTTP_400_BAD_REQUEST)
        
        return Response(result_list, status=status.HTTP_201_CREATED)
    
class FileUploadDestroyView(DestroyAPIView):
    serializer_class = FinancialFileSerializer
    queryset = FinancialFile.objects.all()
    lookup_field = "id"


class FinancialDataListView(ListAPIView):
    serializer_class = FinancialDataSetSerializer
   
