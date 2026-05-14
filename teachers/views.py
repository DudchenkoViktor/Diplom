from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView


from teachers.models import Specializations, Complaints
from users.models import Locations, Mode_teaching, Teacher_profile
from django.core.cache import cache
from teachers.utils import search_query
from teachers.forms import ComplaintForm

class RosterView(ListView):
    model = Teacher_profile
    template_name = 'teachers/roster_mentors.html'
    context_object_name = 'profiles'
    paginate_by = 3
    allow_empty = True

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_staff=True)

        query = self.request.GET.get('q')
        type_std = self.request.GET.get('type_std')
        speciality = self.request.GET.get('speciality')
        location = self.request.GET.get('location')
        sort = self.request.GET.get('sort')

        if query:
            queryset = search_query(query)
        if speciality:
            queryset = queryset.filter(main_specialty__name_spec=speciality)
        if type_std:
            queryset = queryset.filter(mode_teaching__name_mode=type_std)
        if location:
            queryset = queryset.filter(locations__name=location)
        if sort:
            queryset = queryset.order_by(sort)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles_amount'] = self.get_queryset().count()
        context['modes'] = Mode_teaching.objects.all()
        context['specializations'] = Specializations.objects.all()

        locations = cache.get('locations')
        if not locations:
            locations = Locations.objects.all()
            cache.set('locations', locations, 180)

        context['locality'] = locations

        return context

class MentorView(DetailView):
    template_name = 'teachers/card_mentor.html'
    slug_url_kwarg = "mentors_slug"
    context_object_name = 'profiles'

    def get_object(self, **kwargs):
        profiles = Teacher_profile.objects.filter(slug=self.kwargs.get(self.slug_url_kwarg))
        return profiles

class ComplaintView(CreateView):
    template_name = 'teachers/complaint_to_teacher.html'

    form_class = ComplaintForm
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have successfully submitted a complaint against a teacher, thank you for the information.")
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['complaints'] = Complaints.objects.all()
        return context

