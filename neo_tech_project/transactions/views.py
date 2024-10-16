from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.utils.dateparse import parse_date
from .models import Transaction
from .serializers import TransactionSerializer
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit

@method_decorator(ratelimit(key='ip', rate='5/m', method='GET'), name='dispatch')

class ClientTransactionsView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        queryset = Transaction.objects.filter(client_id=client_id)

        # Date range filtering
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date:
            start_date_parsed = parse_date(start_date)
            if start_date_parsed:
                queryset = queryset.filter(transaction_date__gte=start_date_parsed)
            else:
                raise ValidationError("Invalid start date format.")

        if end_date:
            end_date_parsed = parse_date(end_date)
            if end_date_parsed:
                queryset = queryset.filter(transaction_date__lte=end_date_parsed)
            else:
                raise ValidationError("Invalid end date format.")

        return queryset

# Simple Home View
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")





