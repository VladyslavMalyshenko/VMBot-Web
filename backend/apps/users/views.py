from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status, generics

from django.shortcuts import redirect

from .models import User
from .serializers import UserSerializer, DiscordUserSerializer
from .services import DiscordUserMixin, PayloadHeadersMixin


def test_token(request):
    s = PayloadHeadersMixin()
    return redirect(s.login_url)


class DiscordUserCreate(DiscordUserMixin,
                        generics.GenericAPIView):
    serializer_class = DiscordUserSerializer

    def post(self, *args, **kwargs):
        discord_code = self.request.query_params.get('code')
        if discord_code is None:
            return Response({
                'error': 'Invalid discord code'
            }, status=status.HTTP_403_FORBIDDEN)

        data = self.get_user(discord_code)
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(DiscordUserMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class GetUserAPIVIew(DiscordUserMixin, APIView):
    pass

    # def post(self, *args, **kwargs):
    #     code = self.request.query_params.get('code')
    #
    #     if code is None:
    #         return Response({'error': 'The code is None!'}, status=400)
    #
    #     access_token = get_access_token(code)
    #     user_json = get_user_json(access_token)
    #     return Response({'user': user_json}, status=200)
