from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.models import Tag, Task


def index(request):
    tasks = Task.objects.all()

    context = {
        "title": 'TODO List',
        "tasks": tasks,
    }
    return render(request, "core/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")
    template_name = "core/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")
    template_name = "core/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("core:tag-list")
    template_name = "core/tag_confirm_delete.html"