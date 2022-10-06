from pyexpat import model
from rest_framework import serializers
from MergePDf.models import modelA, modelB


class ModelASerializer(serializers.ModelSerializer):
    class Meta:
        model = modelA
        fields ='__all__'