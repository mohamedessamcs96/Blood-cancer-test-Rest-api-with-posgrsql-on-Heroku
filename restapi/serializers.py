from rest_framework import serializers
from .models import UserData

class UserSerializers(serializers.ModelSerializer):

	class Meta:
		model=UserData
		#fields=('firstname','lastname','userid')
		fields='__all__'


