from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class VideoPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        data = super().get_paginated_response(data).data
        data['count'] = math.ceil(data['count']/self.page_size)
        return Response(data)

