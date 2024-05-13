from rest_framework import serializers
from hospital.models import Hospital_Information, Patient, User 
from doctor.models import Doctor_Information

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital_Information
        fields = '__all__'
