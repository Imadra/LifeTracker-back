from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import Value


@permission_classes([IsAuthenticated])
class Add(APIView):
    def post(self, request):
        name = request.data.get("name")
        importance = request.data.get("importance")
        value_type = request.data.get("value_type").upper()

        args = {
            "name": name,
            "importance": importance,
            "value_type": Value.Type[value_type]
        }
        try:
            Value.objects.create(**args, user=request.user)
        except Exception as e:
            # print(str(e))
            # print("-------------------------------------------------------")
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Value: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class Delete(APIView):
    def post(self, request):
        id = request.data.get("id")
        print(id)
        try:
            Value.objects.filter(id=id, user=request.user).delete()
        except Exception as e:
            print(str(e))
            print("-------------------------------------------------------")
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Value: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class GetAll(APIView):
    def get(self, request):
        values = Value.objects.filter(user=request.user).values()
        return Response(status=status.HTTP_200_OK, data=values)
