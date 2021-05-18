from django.db import models
class Track(models.Model):
    name=models.CharField(max_length = 50)
    def __str__(self):
        return self.name


class Student(models.Model):
    fname=models.CharField(max_length = 50 , null= True, default='someone') #fname varchar(50)
    lname=models.CharField(max_length = 50 , null= True, default='someone') 
    age=models.IntegerField()  #ageint
    student_track=models.ForeignKey(Track,on_delete=models.CASCADE)
    def __str__(self):
        return self.fname + " " +self.lname

    def is_graduated(self):
         if self.age > 20 :
              return True
         else:
             return False
    is_graduated.short_description = 'Post Graduate Student'
    is_graduated.boolean = True