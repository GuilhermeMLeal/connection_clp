from rest_framework import serializers
from clp_api.models.ClpEntity import ClpInformation

class ClpInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClpInformation  
        fields = '__all__'