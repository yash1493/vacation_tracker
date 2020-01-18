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
from datetime import datetime,timedelta
import uuid


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


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def updateVacation(request):
    employee=Employee.objects.all()
    if request.method == 'POST':
        UniqueId=request.POST.get('employee')
        if UniqueId != None:
            emp=Employee.objects.get(EmpId=UniqueId)
            emp_id=emp.EmpId
            emp_name=emp.EmpName
            vacationId=uuid.uuid1().int
            startdate=request.POST['startdate']
            enddate=request.POST['enddate']
            start_date = datetime.strptime(startdate, '%Y-%m-%d')
            end_date = datetime.strptime(enddate, '%Y-%m-%d')
            if (end_date - start_date).days < 0:
                return render(request, 'updateVacation.html',{'errorCode':'Validation Failure : Start Date ( %s ) exceeds End Date ( %s )' % (startdate,enddate),'employee':employee})
            vacation=Vacation.objects.create(
                VacationId=vacationId,
                EmpName=emp_name,
                EmpId=emp_id,
                vacationStartdate=startdate,
                vacationEnddate=enddate,
            )
            updateCalendar(vacation)
        else:
            return render(request, 'updateVacation.html',{'employee':employee,'INFO_employee':'Please select an employee !!'})
    return render(request, 'updateVacation.html',{'employee':employee})

def updateCalendar(vacation):
    start_date = datetime.strptime(vacation.vacationStartdate, '%Y-%m-%d')
    end_date = datetime.strptime(vacation.vacationEnddate, '%Y-%m-%d')
    day_delta = timedelta(days=1)
    for i in range((end_date - start_date).days+1):
        new_event=Event.objects.create(
        title=vacation.EmpId+" - "+vacation.EmpName,
        start_time=start_date + i*day_delta,
        end_time=start_date + i*day_delta,
        vacationId=Vacation.objects.get(VacationId=vacation.VacationId)
        )
    return

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
