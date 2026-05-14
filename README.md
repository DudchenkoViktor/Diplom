# EduConnect

## Overview

This project is designed to facilitate the search and study of all those who want to develop in a certain direction, but can not find a mentor for advice and other aids. The platform is oriented to people of any age, both for schoolchildren and for people of age, there are no age restrictions for development. 

The convenience of the project lies in the intuitive interface, quick and efficient search for teachers on selected topics, as well as it is worth noting that to use the full functionality does not necessarily register on the site, it is only necessary to log in and immediately get down to business, without wasting time to create an account. It is possible to create an account as a teacher, if you want to be a mentor for hundreds of people: to do this you need to register an account, as well as, if you want to add information to your profile, so that users can learn more about you, which will increase the chance of appealing to you for help. 

Also, a system of complaints about unfriendly teachers has been implemented, after which the admin team will study the complaints and make decisions. For convenient monitoring and management of the product an admin panel with all the tools has been developed.

## Technologies

+ Backend
  + Django Core
    + Django
    + Django ORM
    + Django Admin:
  + PostgreSQL
  + Pillow
+ Frontend
  + Django Templates
  + CSS/SASS
  + JS/JQuery
  + Bootstrap5
+ Docker, Docker-compose
+ Nginx, Gunicorn

## Application development 
The entire application was developed using __Django Core__, for every user request for a new page, the request is processed and sends a new HTML page i.e. _MPA_. The platform was built using __MVT (Model View Template)__. All logic was created in View, using __Django and other technologies, Django ORM__ was used for database handling, sorting and selection, __PostgreSQL__ was chosen as the main database. 

This is an example of how _full-text search_ in the help was implemented using django packages, for easy use of the user.

``` python
def search_query(query):

    vector = SearchVector("first_name", "last_name")
    query = SearchQuery(query)

    result = (
        Teacher_profile.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline_firstname=SearchHeadline(
            "first_name",
            query,
            start_sel='<span style="color: #E2725B;'
                      'font-style: italic;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        headline_lastname=SearchHeadline(
            "last_name",
            query,
            start_sel='<span style="color: #E2725B;'
                      'font-style: italic;">',
            stop_sel="</span>",
        )
    )

    return result
```
And how this full-text search is used in a real query from a user.
```python
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

```

For the frontend part implementation __Django template__ was used as a basic layout, __CSS/SASS Bootstrap5__ as styles and ready-made templates. __Javascript/JQuery__ is necessary to realize automatic loading of content without loading the whole page, sending data to the server and processing them. 

__Docker, Docker-compose__ technologies were used to create the container and deploy the project, also __Gunicorn__ and __Nginx__ were connected for correct work of django application.

```
version: '3'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: home
      POSTGRES_USER: home
      POSTGRES_PASSWORD: root
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  web:
    build: .
    command: gunicorn app_store.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://home:root@db:5432/home

  nginx:
    image: nginx:latest
    ports:
      - "8081:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

volumes:
  postgres_data:
```