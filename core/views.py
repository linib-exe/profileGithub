from django.shortcuts import render, get_list_or_404
from .models import Student
from django.core.paginator import Paginator

def index(request):
    # Get the search term from the request
    search = request.GET.get('search', '')


    try:
        # Use get_list_or_404 to handle the case when no students are found
        students = Student.objects.all().order_by('full_name')
    except Student.DoesNotExist:
        # Provide a more specific exception
        return render(request, 'home.html')

    # If search is provided, filter the students
    if search:
        students = Student.objects.filter(full_name__icontains=search)

    # Paginate the result
    paginator = Paginator(students, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # print(type(page_number))

    return render(request, 'core/index.html', {'students': page_obj, 'search_term': search})
