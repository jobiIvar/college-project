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
        (ARTS, "Arts"),
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


class RankHolder(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='rank_holders')
    rank = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    year = models.IntegerField()

    class Meta:
        verbose_name = "Rank Holder"
        verbose_name_plural = "Rank Holders"

    def __str__(self):
        return f"{self.name} - {self.department}"


class UniversityPlayer(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    image = models.ImageField(upload_to='univ_player/')

    class Meta:
        verbose_name = "University Player"
        verbose_name_plural = "University Players"

    def __str__(self):
        return f"{self.name} - {self.sport}"