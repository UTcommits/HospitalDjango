from django.shortcuts import render, redirect
from .decorators import *
from .forms import *
from .models import *


from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            group = form.cleaned_data.get('group')

            user = User.objects.get(username=user_name)

            my_group = Group.objects.get(name=group) 
            user.groups.add(my_group)
            if group=='patient':
                Patient.objects.create(
                    user=user,
                    name=user.first_name + ' '+user.last_name ,
                    email=user.email
                    )
            if group=='doctor':
                Doctor.objects.create(
                    user=user,
                    name=user.first_name + ' '+user.last_name ,
                    email=user.email
                    )

            messages.success(request, 'Account was created for ' + user_name)

            return redirect('login')
        
        

    context = {'form':form}
    return render(request, 'profiles/register.html', context)


@unauthenticated_user
def login_auth(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    
    context = {}
    return render(request, 'profiles/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
    return render(request, 'profiles/index.html')

def about(request):
    return render(request, 'profiles/about.html')

def contact(request):
    return render(request, 'profiles/contact.html')


@login_required(login_url='login/')
@allowed_users(allowed_roles=['patient','doctor'])
def patient_appoint(request):
    if request.user.groups.exists():
	    group = request.user.groups.all()[0].name
    if group == 'patient': 
        appoint = request.user.patient.appoinments_set.all()
    else:
        appoint = request.user.doctor.appoinments_set.all()
    
    info = {'appoints':appoint}
    return render(request, 'profiles/cust_appoint.html', info)


@login_required(login_url='login/')
@allowed_users(allowed_roles=['patient',])
def patients_invoice(request):
    invoice = request.user.patient.account_set.all()
    
    info = {'invoice':invoice}
    return render(request, 'profiles/cust_invoice.html', info)


@login_required(login_url='login/')
@allowed_users(allowed_roles=['patient','doctor',])
def patients_profile(request):
    if request.user.groups.exists():
	    group = request.user.groups.all()[0].name
    if group == 'patient': 
        patient = request.user.patient
        form = PatientForm(instance=patient)

        if (request.method == 'POST'):
            form = PatientForm(request.POST, request.FILES, instance=patient)
            if form.is_valid():
                form.save()
    else:
        doctor = request.user.doctor
        form = DoctorForm(instance=doctor)

        if (request.method == 'POST'):
            form = DoctorForm(request.POST, request.FILES, instance=doctor)
            if form.is_valid():
                form.save()

    info = {'form':form}
    return render(request , 'profiles/prof_form.html', info)

@login_required(login_url='login/')
@allowed_users(allowed_roles=['receptionist'])
def create_profile(request,pk):
        patient = Patient.objects.get(id = pk)
        form = PatientForm(instance=patient)
        if (request.method == 'POST'):
            form = PatientForm(request.POST, request.FILES, instance=patient)
            if form.is_valid():
                form.save()

        info = {'form':form}
        return render(request , 'profiles/prof_form.html', info)

@login_required(login_url='login')
def error(request):

	return render(request, 'profiles/error.html')



@login_required(login_url='login/')
@allowed_users(allowed_roles=['patient','doctor'])
def prescription(request):
    if request.user.groups.exists():
	    group = request.user.groups.all()[0].name
    if group == 'doctor':
        prescriptions = request.user.doctor.perscription_set.all()
        info = {'prescriptions':prescriptions,'us':group}
    else:
        prescriptions = request.user.patient.perscription_set.all()
        info = {'prescriptions':prescriptions,'us':group}
    return render(request, 'profiles/prescription.html', info)



@login_required(login_url='login/')
@allowed_users(allowed_roles=['doctor'])
def addpres(request, pk):
    print(pk)
    doctor = Doctor.objects.get(id=pk)
    form = PerscriptionForm(initial={'doctor':doctor})
    if request.method == 'POST':
        form = PerscriptionForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('prescription')
    
    info = {'form':form}
    return render(request, 'profiles/new_p.html', info)




@login_required(login_url='login')
@allowed_users(allowed_roles=['receptionist'])
def dashboard(request):
    appoinments = Appoinments.objects.all()
    patient = Patient.objects.all()

    total = appoinments.count()
    delivered = appoinments.filter(status='Completed').count()
    pending = appoinments.filter(status='Pending').count()

    info = {'orders':appoinments, 'customers':patient, 'total':total, 'delivered':delivered,
	'pending':pending}
    return render(request, 'profiles/dashboard.html', info)



@login_required(login_url='login/')
@allowed_users(allowed_roles=['receptionist'])
def create_appoint(request):
        form = AppointmentForm()
        if (request.method == 'POST'):
            form = AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

        info = {'form':form}
        return render(request , 'profiles/crea_pres.html', info)


@login_required(login_url='login')
@allowed_users(allowed_roles=['receptionist'])
def delPatient(request,pk):
    item = Patient.objects.get(id=pk)
    item.delete()
    return redirect('dashboard')
   


