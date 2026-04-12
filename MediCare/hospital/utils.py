from django.db.models import Q
from .models import Patient, User, Hospital_Information
from doctor.models import Doctor_Information, Appointment
from hospital_admin.models import hospital_department, specialization, service
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchDoctors(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')        
    doctors = Doctor_Information.objects.filter(register_status='Accepted').distinct().filter(
        Q(name__icontains=search_query) |
        Q(hospital_name__name__icontains=search_query) |  
        Q(department__icontains=search_query))
    return doctors, search_query

def searchHospitals(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    hospitals = Hospital_Information.objects.distinct().filter(Q(name__icontains=search_query))
    return hospitals, search_query


def paginateHospitals(request, hospitals, results):
    page = request.GET.get('page')
    paginator = Paginator(hospitals, results)

    try:
        hospitals = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        hospitals = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        hospitals = paginator.page(page)
        
    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, hospitals

def searchDepartmentDoctors(request, pk):  
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    departments = hospital_department.objects.get(hospital_department_id=pk)
    
    doctors = Doctor_Information.objects.filter(department_name=departments).filter(
        Q(name__icontains=search_query))
    return doctors, search_query