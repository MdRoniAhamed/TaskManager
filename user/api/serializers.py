from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

# Register Serializer 
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'},validators=[validate_password])
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True,validators=[validate_password])
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.pop('password2')
            if password != password2:
                raise serializers.ValidationError({"password":"Password and confirm password did't match"})
            return attrs

    def save(self):
        password = self.validated_data['password']
        account = User(**self.validated_data)
        account.set_password(password)
        account.save()
        
        return account


# Password Change serializer
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True,validators=[validate_password])
    new_password = serializers.CharField(required=True, validators=[validate_password])

# Password Reset Serializer
class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
