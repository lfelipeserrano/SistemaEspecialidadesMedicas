from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from django.contrib.auth.models import User
from CEM.models import Doctor
class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			# if request.user.groups.filter(name = 'Asistentes').exists() or request.user == tempInstance.idDoctor:
			d += f'<li> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><u> {d} </u></td>"
		return '<td></td>'
		

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, doctor = None, withyear=True):
		doctores = Doctor.objects.all()
		for doc in doctores:
			if doc == doctor:
				events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month, idDoctor = doctor)
				break
			else :
				events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal