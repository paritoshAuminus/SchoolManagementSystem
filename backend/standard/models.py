from django.db import models
from school.models import School

# Create your models here.
class Standard(models.Model):
    standards = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    ]

    title = models.CharField(max_length=2, choices=standards)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"Standard {self.title} - {self.school}"


class Section(models.Model):
    sections = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    ]

    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    title = models.CharField(max_length=1, choices=sections)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)

    def __str__(self):
        return f"Section {self.title} - {self.standard}"