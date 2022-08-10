from django.contrib import admin
from django.urls import path,include
from .views import ProjectAPIView,ProjectDetails,UserAPIView,UserDetails,IssueAPIView,IssueDetails,IssueDetailsPagination,LabelAPIView,IssueEditStatus,IssueFilter,CommnetAPIView,AssignAPIView,AssignDetails,WatcherAPIView,WatcherDetails
from rest_framework import routers

#router=routers.DefaultRouter()
#router.register('courses',views.ProjectView)

urlpatterns = [
#path('',include(router.urls))
    path('projects/',ProjectAPIView.as_view()),
    path('projectdetail/<int:id>/',ProjectDetails.as_view()),


    path('users/',UserAPIView.as_view()),
    path('projectAllUsers/<int:id>/', UserDetails.as_view()),


    path('issues/',IssueAPIView.as_view()),
    path('projectAllIssues/<int:id>/', IssueDetails.as_view()),
    path('statusupdate/<int:id>/', IssueEditStatus.as_view()),
    path('projectAllIssuesPagination/',IssueDetailsPagination.as_view()),
    path('labels/', LabelAPIView.as_view()),
    path('filterissue/',IssueFilter.as_view()),
    path('comments/', CommnetAPIView.as_view()),
    path('assign/', AssignAPIView.as_view()),
    path('usersIssue/', AssignDetails.as_view()),
    path('watcher/', WatcherAPIView.as_view()),
    path('waterChangestatus/',WatcherDetails.as_view())


]