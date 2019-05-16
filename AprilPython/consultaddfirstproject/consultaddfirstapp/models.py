from django.db import models

# Create your models here.

class Candidate(models.Model):
    Name_of_Can=models.CharField(max_length=100,unique=True)


class CandidateInfo(models.Model):
    CanID=models.ForeignKey(Candidate,on_delete=models.PROTECT)




