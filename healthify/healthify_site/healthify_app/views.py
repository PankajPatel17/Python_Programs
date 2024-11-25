from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor, Patient
from django.contrib.auth.decorators import login_required

# Doctor registration view
def doctor_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            specialty = request.POST['specialty']
            doctor = Doctor(user=user, specialty=specialty)
            doctor.save()
            return render(request,'doctor_register.html')
    else:
        form = UserCreationForm()
    return render(request, 'doctor_register.html', {'form': form})

# Patient registration view
def patient_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            age = request.POST['age']
            patient = Patient(user=user, age=age)
            patient.save()
            return redirect('patient_login')
    else:
        form = UserCreationForm()
    return render(request, 'patient_register.html', {'form': form})

# Login view (for both doctors and patients)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'doctor'):
                return redirect('doctor_dashboard')
            elif hasattr(user, 'patient'):
                return redirect('patient_dashboard')
    return render(request, 'login.html')

# Doctor dashboard view (shows list of all patients)
@login_required
def doctor_dashboard(request):
    if hasattr(request.user, 'doctor'):
        appointments = Appointment.objects.filter(doctor__user=request.user)
        return render(request, 'doctor_dashboard.html', {'appointments': appointments})
    return redirect('doctor_login')

# Patient dashboard view (allows booking an appointment)
@login_required
def patient_dashboard(request):
    if hasattr(request.user, 'patient'):
        doctors = Doctor.objects.all()
        return render(request, 'patient_dashboard.html', {'doctors': doctors})
    return redirect('patient_login')

# Book appointment for a patient with a doctor
@login_required
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    patient = request.user.patient
    appointment = Appointment.objects.create(patient=patient, doctor=doctor, date=request.POST['date'])
    appointment.save()
    return redirect('patient_dashboard')
