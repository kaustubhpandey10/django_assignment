from django.test import TestCase
from .models import Project,User
from django.utils import timezone

class ProjectTest(TestCase):
    def create_project(self,project_name="angular project"):
        return Project.objects.create(project_name=project_name)
    def test_project_creation(self):
        project=self.create_project()
        self.assertTrue(isinstance(project,Project))
        self.assertEqual(project.__str__(),project.project_name)
"""
class UserTest(TestCase):
    def create_project(self, project_name="angular project"):
        return Project.objects.create(project_name=project_name)


    def create_user(self,user_name="shristi"):
        p=self.create_project()
        return User.objects.create(user_name=user_name,p=p)
    def test_user_creation(self):
        user=self.create_user()
        self.assertTrue(isinstance(user,User))
        self.assertEqual(user.__str__(),user.project_name)
"""