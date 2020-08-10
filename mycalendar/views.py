from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view
import datetime

from .models import Day, Task
from .serializers import TaskSerializer, DaySerializer


@permission_classes([IsAuthenticated])
class GetDay(APIView):
    def get(self, request):
        year = request.GET.get("year")
        month = request.GET.get("month")
        day = request.GET.get("day")
        try:
            instance = Day.objects.get(year=year, month=month, day=day, user=request.user)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_200_OK, data=None)
        data = DaySerializer(instance).data
        data["taskNames"] = []
        data["completed"] = []
        for el in data["tasks"]:
            try:
                cur = Task.objects.get(id=el)
            except Exception as e:
                print(str(e))
                return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
            data["taskNames"].append(cur.name)
            print(cur.name, cur.done)
            if cur.done and cur.get_finish_day() == int(day) and cur.get_finish_month() == int(
                    month) and cur.get_finish_year() == int(year):
                data["completed"].append(True)
            else:
                data["completed"].append(False)
        # print(data)
        return Response(status=status.HTTP_200_OK, data=data)


@permission_classes([IsAuthenticated])
class EditDay(APIView):
    def post(self, request):
        year = request.data.get("year")
        month = request.data.get("month")
        day = request.data.get("day")
        mood = request.data.get("mood").upper()
        note = request.data.get("note")
        tasks = request.data.get("tasks")
        args = {"year": year, "month": month, "day": day, "mood": Day.Mood[mood], "note": note,
                "user": request.user}
        try:
            instance = Day.objects.get(year=year, month=month, day=day, user=request.user)
            instance.note = note
            instance.mood = Day.Mood[mood]
            try:
                instance.tasks.set(tasks)
                instance.save()
            except Exception as e:
                print(str(e))
                return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
            return Response(status=status.HTTP_200_OK, data="Calendar: CF black shygar")
        except Exception as e:
            try:
                instance = Day.objects.create(**args)
                instance.tasks.set(tasks)
                instance.save()
            except Exception as e:
                print(str(e))
                return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
            return Response(status=status.HTTP_200_OK, data="Calendar: CF black shygar")


@permission_classes([IsAuthenticated])
class AddTask(APIView):
    def post(self, request):
        name = request.data.get("name")
        done = False

        args = {
            "name": name,
            "done": done,
            "user": request.user
        }
        try:
            Task.objects.create(**args)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Task: Codeforces redblack koi")


@permission_classes([IsAuthenticated])
class GetAllTasks(APIView):
    def get(self, request):
        tasks = Task.objects.values()
        new_tasks = []
        for task in tasks:
            if task["user_id"] != request.user.id:
                continue
            cur = {"id": task["id"], "name": task["name"], "date": task["date"]}
            if task["done"]:
                cur["done"] = task["finish_date"]
            else:
                cur["done"] = "X"
            new_tasks.append(cur)
        return Response(status=status.HTTP_200_OK, data=new_tasks)


@permission_classes([IsAuthenticated])
class GetTask(APIView):
    def get(self, request):
        id = request.GET.get("id")
        try:
            task = Task.objects.get(id=id, user=request.user)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data=TaskSerializer(task).data)


@permission_classes([IsAuthenticated])
class DeleteTask(APIView):
    def post(self, request):
        id = request.data.get("id")
        try:
            Task.objects.get(id=id, user=request.user).delete()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Task: OK")


@permission_classes([IsAuthenticated])
class UpdateTask(APIView):
    def post(self, request):
        id = request.data.get("id")
        name = request.data.get("name")
        try:
            task = Task.objects.get(id=id, user=request.user)
            task.name = name
            task.save()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Task: OK")


@permission_classes([IsAuthenticated])
class FinishTask(APIView):
    def post(self, request):
        id = request.data.get("id")
        year = request.data.get("year")
        month = request.data.get("month")
        day = request.data.get("day")
        date = datetime.date(year, month, day)
        try:
            task = Task.objects.get(id=id, user=request.user)
            task.done = True
            task.finish_date = date
            print(task.finish_date)
            task.save()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
        return Response(status=status.HTTP_200_OK, data="Task: OK")


@permission_classes([IsAuthenticated])
class UnFinishTask(APIView):
    def post(self, request):
        id = request.data.get("id")
        try:
            task = Task.objects.get(id=id, user=request.user)
            task.done = False
            task.save()
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
        return Response(status=status.HTTP_200_OK, data="Task: OK")
