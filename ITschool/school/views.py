from django.shortcuts import render, HttpResponse, get_object_or_404
from school import models
from django.views import generic


# Create your views here.

def index(request):
    return render(request, 'school/index.html')

def students(request):
    return render(request, 'school/students.html')

def course(request):
    course = models.Course.objects.all()
    return render(request, 'school/course.html',
                  {'course': course})

def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk = pk)
    return render(request, 'school/course_detail.html', {'course':course})

class CourseDetail(generic.DetailView):

    model = models.Course

class CourseList(generic.ListView):

    queryset = models.Course.objects.select_related('lector')

    model = models.Course
    template_name = "school/course.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']
        context['paginator_range'] = paginator.get_elided_page_range(page_obj.number)

        return context




