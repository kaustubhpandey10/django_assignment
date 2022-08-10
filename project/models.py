from django.db import models

# Create your models here.
class Project(models.Model):
    project_name=models.CharField(max_length=200)
    def __str__(self):
        return self.project_name

class User(models.Model):
    user_name=models.CharField(max_length=200)
    p=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.user_name

class Issue(models.Model):
    issue_name=models.CharField(max_length=200)

    type = models.CharField(max_length=200, default="")

    sprint = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=200, default="")
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
   # user=models.OneToOneField(User,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.issue_name

class Label(models.Model):
    label_name=models.CharField(max_length=200)

    issue=models.ForeignKey(Issue,on_delete=models.CASCADE,default=1)



    def __str__(self):
        return self.label_name
class Comment(models.Model):
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.comment



class Assign(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    iss=models.ForeignKey(Issue,on_delete=models.CASCADE,default=1)


class Watcher(models.Model):
    issueid=models.ForeignKey(Issue,on_delete=models.CASCADE,default=1)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    status=(('yes',"YES"),
            ('no','NO'))

    active=models.CharField(max_length=100,default="yes",choices=status)


