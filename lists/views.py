from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import List, Entry


@permission_classes([IsAuthenticated])
class AddList(APIView):
    def post(self, request):
        name = request.data.get("name")
        args = {
            "name": name,
        }
        try:
            List.objects.create(**args, user=request.user)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="List: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class DeleteList(APIView):
    def post(self, request):
        name = request.data.get("name")
        try:
            List.objects.get(name=name, user=request.user).delete()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="List: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class GetList(APIView):
    def get(self, request):
        name = request.GET.get("name")
        print(name)
        try:
            lst = List.objects.get(name=name, user=request.user)
            resp = dict()
            resp["name"] = name
            resp["entries"] = lst.entries
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data=resp)


@permission_classes([IsAuthenticated])
class GetAllLists(APIView):
    def get(self, request):
        values = List.objects.filter(user=request.user).values()
        return Response(status=status.HTTP_200_OK, data=values)


@permission_classes([IsAuthenticated])
class UpdateList(APIView):
    def post(self, request):
        name = request.data.get("name")
        entries = request.data.get("entries")
        try:
            lst = List.objects.get(name=name, user=request.user)
            lst.entries = entries
            lst.save()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="List: Codeforces redblack koi")