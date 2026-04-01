from django.db import models
from django.contrib.auth.models import AbstractUser
from school.models import School

# Create your models here.
class User(AbstractUser):
    pass

class SchoolMember(models.Model):
    ROLES = [
        ('principal', 'Principal'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['school'],
                condition=models.Q(role='principal'),
                name='unique_principal_per_school'
                )
        ]
    
    def __str__(self):
        return self.user.username

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
