from rest_framework import serializers
# from ..backend_notary_now.account.models import Account
import sys
sys.path.append('..')
# import file
from account.models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name',
                  'last_name',
                  'is_notary',
                  'profile_photo',
                  'is_active')
