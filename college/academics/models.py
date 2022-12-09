from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Courses(models.Model):
    BACHELOR = "BACHELOR"
    MASTER = "MASTER"
    M_PHIL = "M.PHIL"
    PHD = "PH.D"
    level_choice = (
        (BACHELOR, "Bachelor"),
        (MASTER, "Master"),
        (M_PHIL, "M.Phil"),
        (PHD, "PhD")
    )
    ARTS = "ARTS"
    SCIENCE = "SCIENCE"
    COMMERCE = "Commerce"
    BUSINESS = "BUSINESS"
    session_choice = (
        (ARTS,"Arts"),
        (SCIENCE, "Science"),
        (COMMERCE, "Commerce"),
        (BUSINESS, "Business")
    )
    course_name = models.CharField(max_length=10, choices=level_choice, default="BACHELOR")
    session_name = models.CharField(max_length=10, choices=session_choice, blank=True, null=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self):
        if not self.session_name:
            return f"{self.course_name} in {self.department}".upper()

        else:
            return f"{self.course_name} of {self.session_name} in {self.department}".upper()
