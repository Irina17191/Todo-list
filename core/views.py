from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from core.forms import TaskForm
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


class TaskCreateView(generic.CreateView):
    model = Task
    # fields = "__all__"
    form_class = TaskForm
    success_url = reverse_lazy("core:index")
    template_name = "core/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:index")
    template_name = "core/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:index")
    template_name = "core/task_confirm_delete.html"


def toggle_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("core:index"))
