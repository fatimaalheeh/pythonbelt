from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Thought(models.Model):
    user_id = models.ForeignKey(User, related_name="thoughts", on_delete=models.CASCADE)
    thought = models.TextField()
    user_id = models.ForeignKey(User, related_name="thoughts_liked", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user_id = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    thought_id = models.ForeignKey(Thought, related_name="likes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def insert_new_user(first_name, last_name, email, password):
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    


def is_duplicate_email(email):
    users = User.objects.filter(email=email).values()
    if len(users)>0:
        return True
    return False


def get_user(email, passwd):
    users = User.objects.filter(email=email, password=passwd)
    if len(users)<1:
        return None
    return users[0]


def get_all_thoughts():
    all_thoughts = Thought.objects.all().order_by("created_at")
    return all_thoughts


def insert_thought(user_id, post_data):
    user = User.objects.get(id=user_id)
    thought = Thought.objects.create(thought=post_data)
    lastthought=Thought.objects.last()
    t=lastthought[0]
    user.thoughts.id=t.id

    return thought


def insert_like(user_id,thought_id):
    user = User.objects.get(id=user_id)
    thought = Thought.objects.get(thought_id=thought_id)
    like =  Like.objects.create(user_id=user,thought_id=thought_id)
    return like


def get_all_likes(thought_id):
    likes=Like.objects.all
    return likes
    

def get_likes(thought_id):
    thought = Thought.objects.get(id=thought_id)
    likes = User.objects.filter(thought_id=thought_id).order_by("created_at")
    return likes
def get_likes_count(thought_id):
    all_thought_likes=Like.objects.filter(thought_id==thought_id)
    count=len(all_thought_likes)
    return count