from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except KeyError:
#             return Response({"detail": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
#         except TokenError:
#             return Response({"detail": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        




from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def user_api(request):
    if request.method == 'GET':
        return Response({"message": "GET-запрос получен"})

    elif request.method == 'POST':
        name = request.data.get('name')
        return Response({"message": f"POST-запрос получен!"})

