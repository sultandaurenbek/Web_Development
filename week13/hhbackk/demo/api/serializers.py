from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Company
from api.models import Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        company = Company(**validated_data)
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        company = serializers.IntegerField(write_only=True)

        model = Company
        fields = '__all__'

class CompanyWithVacancies(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'