
from django.db import models
from django.contrib.auth.models import User

# Doctor model (inherits from User model)
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Patient model (inherits from User model)
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

# Appointment model (Doctor - Patient relation)
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.date}"

