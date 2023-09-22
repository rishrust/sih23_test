from django.db import models




class projects(models.Model):
    student_name=models.CharField(max_length=1000)
    # college_id=models.CharField(max_length=1000)
    project_content=models.CharField(max_length=1000)
    project_title=models.CharField(max_length=1000)
    project_domain=models.CharField(max_length=1000)
    project_content=models.CharField(max_length=1000)
    university_name=models.CharField(max_length=1000)
    student_photo=models.ImageField(upload_to='uploads/')#image
    project_cover=models.ImageField(upload_to='uploads/')#image