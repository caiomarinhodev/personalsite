from django.views.generic import ListView

from app.models import Project


class IndexView(ListView):
    model = Project
    template_name = 'site/index.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
