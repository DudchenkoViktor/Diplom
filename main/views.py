from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = "main/main_page.html"

class AboutUsView(TemplateView):
    template_name = 'main/about_us.html'

