from django.db import models
from django.contrib.auth.hashers import make_password
from uuid import uuid4

class User(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True)
    name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(unique=True)
    Admin = 0
    Bowler = 1
    Coach = 2
    Wicketkeeper = 3
    Mentor = 4

    ROLE = (
        (Admin , "Admin"),
        (Bowler , "Bowler "),
        (Coach, "Coach"),
        (Wicketkeeper, "Wicketkeeper"),
        (Mentor, "Mentor")
)       
    created_at = models.DateTimeField(auto_now_add=True)



    password = models.CharField(max_length=128) 
    role = models.SmallIntegerField(choices=ROLE, default=1, null=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.email
    

class Survey(models.Model):
    yes = 0
    no = 1
    

    ROLE = (
        (yes , "yes "),
        (no , "no "),
       
)      
    id = models.UUIDField(default = uuid4, primary_key = True)
    name = models.CharField(max_length=30,blank=False)
    scheduled_date = models.DateField()
    scheduled_time = models.TimeField()

    creator = models.ForeignKey(User, related_name='created_surveys', on_delete=models.CASCADE)
    target_users = models.ManyToManyField(User, related_name='targeted_surveys')
    invitations_send_flag = models.SmallIntegerField(choices=ROLE, default = 1, null=True)
    notification_send_flag = models.SmallIntegerField(choices=ROLE, default = 1, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True)
    questionlabel = models.CharField(max_length=250,blank=False)
    survey_id=models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = 0
    radio_single = 1
    radio_multiple = 2
    file = 3
 

    TYPE = (
        (text , "text "),
        (radio_single , "radio_single "),
        (radio_multiple, "radio_multiple"),
        (file, "file"),
        
)     
    type = models.SmallIntegerField(choices=TYPE, default=1, null=True)

    instructions = models.CharField(max_length=500,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    id = models.UUIDField(default = uuid4, primary_key = True)
    question_id=models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=550,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)













