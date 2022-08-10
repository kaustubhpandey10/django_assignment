from rest_framework import serializers
from .models import Project, User, Issue, Label, Comment, Assign, Watcher


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','project_name')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','user_name','p')



class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issue
        fields=('id','issue_name','type','sprint','status','project')
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Label
        fields=('id','label_name','issue')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id','comment','user','project')
class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assign
        fields=('id','uid','iss')
class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Watcher
        fields=('id','issueid','userid','active')