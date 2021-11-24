from django.conf                            import settings
from rest_framework                         import status
from rest_framework.response                import Response
from rest_framework.serializers             import Serializer
from rest_framework_simplejwt.backends      import TokenBackend #me ayuda a decodificar el token
from rest_framework_simplejwt.views         import TokenVerifyView
from rest_framework_simplejwt.exceptions    import TokenError, InvalidToken
from rest_framework_simplejwt.serializers   import TokenVerifySerializer

class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = TokenVerifySerializer(data= request.data)
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])

        try:
                serializer.is_valid(raise_exception=True)
                token_data  = token_backend.decode(request.data['token'])
        
        except TokenError as e:
                raise InvalidToken(e.args[0])
        except Exception as e:
                print(e)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

