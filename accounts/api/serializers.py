from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add first_name,last_name,email,active
    and roles information about user"""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['is_active'] = user.is_active
        token['role'] = user.roles
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    """ User registration model serializer """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'roles', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Password Are not same !!'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already taken !!'})
        account = User(username=self.validated_data['username'],
                       email=self.validated_data['email'],
                       first_name=self.validated_data['first_name'],
                       last_name=self.validated_data['last_name'],
                       roles=self.validated_data['roles']
                       )
        account.set_password(self.validated_data['password'])
        account.save()
        return account
