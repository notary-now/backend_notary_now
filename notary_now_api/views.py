from rest_framework import viewsets

from .serializers import AccountSerializer
from .models import Account


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer
