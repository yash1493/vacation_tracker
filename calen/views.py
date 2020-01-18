from datetime import datetime
from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from .models import *
from .utils import Calendar
import calendar
from .forms import EventForm
from board.models import Employee

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def updateVacation(request):
    employee=Employee.objects.all()
    if request.method == 'POST':
        UniqueId=request.POST['employee']
        if UniqueId != "noselection":
            emp=Employee.objects.get(id=UniqueId)
            emp_id=emp.EmpId
            emp_name=emp.EmpName
            startdate=request.POST.get('startdate','enddate')
            enddate=request.POST['enddate']
            vacation=Vacation.objects.create(
                EmpName=emp_name,
                EmpId=emp_id,
                vacationStartdate=startdate,
                vacationEnddate=enddate,
            )
            
    return render(request, 'updateVacation.html',{'employee':employee})

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})
