from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import Person
from .serializers import PersonSerializer


@permission_classes([IsAuthenticated])
class Add(APIView):
    def post(self, request):
        name = request.data.get("name")
        strengths = request.data.get("strengths")
        weaknesses = request.data.get("weaknesses")
        happiness = request.data.get("happiness")
        img = request.data.get("img")
        description = request.data.get("description")
        age = request.data.get("age")
        habits = request.data.get("habits")

        args = {
            "name": name,
            "strength_list": strengths,
            "weakness_list": weaknesses,
            "happiness": happiness,
            "img": img,
            "description": description,
            "age": age,
            "habit_list": habits,
        }
        try:
            Person.objects.create(**args, user=request.user)
        except Exception as e:
            print(str(e))
            # print("-------------------------------------------------------")
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Person: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class Delete(APIView):
    def post(self, request):
        id = request.data.get("id")
        print(id)
        try:
            Person.objects.filter(id=id, user=request.user).delete()
        except Exception as e:
            print(str(e))
            print("-------------------------------------------------------")
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Person: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class GetAll(APIView):
    def get(self, request):
        people = Person.objects.filter(user=request.user).values()
        return Response(status=status.HTTP_200_OK, data=people)


@permission_classes([IsAuthenticated])
class Get(APIView):
    def get(self, request):
        id = request.GET.get("id")
        try:
            person = Person.objects.get(id=id, user=request.user)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data=PersonSerializer(person).data)


@permission_classes([IsAuthenticated])
class Edit(APIView):
    def post(self, request):
        id = request.data.get("id")
        name = request.data.get("name")
        age = request.data.get("age")
        habits = request.data.get("habits")
        strengths = request.data.get("strengths")
        weaknesses = request.data.get("weaknesses")
        happiness = request.data.get("happiness")
        description = request.data.get("description")
        img = request.data.get("img")
        try:
            person = Person.objects.get(id=id, user=request.user)
            person.name = name
            person.age = age
            person.habit_list = habits
            person.strength_list = strengths
            person.weakness_list = weaknesses
            person.happiness = happiness
            person.description = description
            person.img = img
            person.save()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data=PersonSerializer(person).data)
