from django.http import HttpResponse
from django.shortcuts import render
from  rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Project, User, Issue, Label, Comment, Assign, Watcher
from .pagination import MyPagination
from .serializers import ProjectSerializer, UserSerializer, IssueSerializer, LabelSerializer,CommentSerializer,AssignSerializer,WaterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


class ProjectAPIView(APIView):
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    """
    def get(self,request):
        projects=Project.objects.all()
        serializer=ProjectSerializer(projects,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ProjectSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProjectDetails(APIView):
    def get_object(self,id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExsist:
            return  HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        project=self.get_object(id)
        serializer=ProjectSerializer(project)
        return Response(serializer.data)
    def put(self,request,id):
        project=self.get_object(id)

        serializer=ProjectSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        project=self.get_object(id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserDetails(APIView):
    def get_object(self,id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExsist:
            return  HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        project=self.get_object(id)
        all_users=project.user_set.all()
        serializer=UserSerializer(all_users,many=True)
        return Response(serializer.data)



class IssueAPIView(APIView):
    def get(self,request):
        issues=Issue.objects.all()
        serializer=IssueSerializer(issues,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=IssueSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class IssueFilter(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields=['issue_name','type','status','sprint']



class IssueDetails(APIView):
    def get_object(self,id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExsist:
            return  HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        project=self.get_object(id)
        all_issues=project.issue_set.all()
        serializer=IssueSerializer(all_issues,many=True)
        return Response(serializer.data)

class IssueEditStatus(APIView):
    def get_object(self,id):
        try:
            return Issue.objects.get(id=id)
        except Issue.DoesNotExsist:
            return  HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,id):
        issue=self.get_object(id)
        serializer=IssueSerializer(issue,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class IssueDetailsPagination(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    pagination_class = MyPagination




class LabelAPIView(APIView):
    def get(self,request):
        labels=Label.objects.all()
        serializer=LabelSerializer(labels,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=LabelSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class CommnetAPIView(APIView):
    def get(self,request):
        comments=Comment.objects.all()
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CommentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AssignAPIView(APIView):
    def get(self, request):
        assign = Assign.objects.all()
        serializer = AssignSerializer(assign, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignDetails(APIView):

   def get(self, request, format=None):
       uid = self.request.query_params.get('uid', None)


       queryset = Assign.objects.all()
       if uid:
           queryset = queryset.filter(uid=uid)
       print(queryset)
       li=[]
       for i in queryset:
           li.append({"issueId":i.iss.id,"title":i.iss.issue_name,"status":i.iss.status,"sprint":i.iss.sprint,"type":i.iss.type})



       serializer = AssignSerializer(queryset, many=True)
       return Response(li)

class WatcherAPIView(APIView):
    def get(self, request):
        watchers = Watcher.objects.all()
        serializer =WaterSerializer(watchers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WaterSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatcherDetails(APIView):

    def put(self, request, format=None):
        uid = self.request.query_params.get('uid', None)
        issueid = self.request.query_params.get('issueid', None)

        queryset = Watcher.objects.all()
        if uid:
            queryset = queryset.filter(userid=uid)
        if issueid:
            queryset = queryset.filter(issueid=issueid)
        print(queryset)
        serializer = WaterSerializer(queryset,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














