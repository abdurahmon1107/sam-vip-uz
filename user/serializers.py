from rest_framework import serializers
from django.utils import timezone
from user.untils import send_code
from . import models

class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = models.User.objects.filter(email=email).first()

        if user:
            if user.auth_status:
                raise serializers.ValidationError({'msg': 'This phone number is already in use'})
        else:   
            user = models.User.objects.create_user(email=email, password=password)


        send_code(user.email, user.get_code())
        
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = instance.tokens()
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = models.User.objects.filter(email=email).first()
        if not user.auth_status:
            raise serializers.ValidationError({'msg': 'auth status False'})
        if not user:
            raise serializers.ValidationError({"msg": "User does not exist!"})

        if not user.check_password(password):
            raise serializers.ValidationError({"msg": "Password does not match"})
        
        self.instance = user
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tokens'] = instance.tokens()
        return data


class VerifySerializer(serializers.Serializer):
    code = serializers.CharField()

    def validate(self, attrs):
        user = self.context['request'].user
        code = attrs.get('code')
        now = timezone.now()

        if user.auth_status:
            raise serializers.ValidationError({'msg': 'Authorization status must be'})
        confirmation = user.confirmation
        if confirmation.code != code:  # Updated to expire_datetime
            raise serializers.ValidationError({'msg': 'Code doesn\'t match or has expired'})
        
        user.auth_status = True

        user.save()
        return attrs