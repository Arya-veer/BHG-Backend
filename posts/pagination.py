import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    def get_paginated_response(self, data):
        data = super().get_paginated_response(data).data
        data['count'] = math.ceil(data['count']/self.page_size) # This converts count to number of pages in the pagination
        return Response(data)

class VideoPagination(CustomPagination):
    page_size = 2

class BookPagination(CustomPagination):
    page_size = 1

