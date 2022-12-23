from django.db import models


# Create your models here.
class CollegeAdmissionForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    photo = models.FileField(upload_to='admission/photo')
    signature = models.FileField(upload_to='admission/signature')
    sslc = models.FileField(upload_to='admission/sslc')
    hsc = models.FileField(upload_to='admission/hsc')
    aadhaar = models.FileField(upload_to='admission/aadhaar')
    community = models.FileField(upload_to='admission/community')
    transfer = models.FileField(upload_to="admission/transfer")
    conduct = models.FileField(upload_to='admission/conduct')
    verify = models.BooleanField()

    class Meta:
        verbose_name = "College Admission Form"
        verbose_name_plural = "College Admission Forms"

    def __str__(self):
        return self.name


class PgAdmissionFormModel(CollegeAdmissionForm):
    degree_certificate = models.FileField(upload_to='admission/degree')
    provisional_certificate = models.FileField(upload_to='admission/provisional')
