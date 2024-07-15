from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data = {
            'id': str(self.user.pk),
            'token': str(refresh.access_token),
            'username': self.user.username
        }
        return data