from django.db import models
from django.utils import timezone
import hashlib


class User(models.Model):
    # 0 - Our Portal
    # 1 - Instagram
    username = models.CharField(max_length=50, unique=False)
    email = models.EmailField(null=True)
    platform = models.IntegerField(default=0)
    password = models.CharField(max_length=500, null=True, default=" ")
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username + "|" + str(self.platform)

    def save(self, *args, **kwargs):
        m = hashlib.md5()     
        m.update(self.password.encode("utf-8")) 
        self.password = str(m.digest())
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('username', 'platform',)



class Idea(models.Model):
    keys = {"PENDING":0, "PUBLISHED":1, "REJECTED":2}
    project_title = models.CharField(max_length=60)
    project_description = models.TextField()
    tags = models.CharField(max_length=300)
    is_reviewed = models.IntegerField(default=keys["PENDING"])
    votes = models.IntegerField(default=0)
    reviewer_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="admin_id_idea")
    date_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    body = models.TextField()
    parent_comment_id = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id_comment")
    idea_id = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="idea_id_comment")
    date_time = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    vote_type_key = {"UPVOTE":1, "DOWNVOTE":-1}
    vote_type = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id_vote")
    idea_id = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="idea_id_vote")
    date_time = models.DateTimeField(auto_now_add=True)

class UserToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_token", unique=True)