from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper.forms import (
    NewspaperForm,
    NewspaperSearchForm,
    RedactorCreationForm,
    RedactorSearchForm,
    TopicSearchForm
)
from newspaper.models import (
    Topic,
    Redactor,
    Newspaper
)


class IndexView(generic.View):

    def get(self, request):
        context = {
            "num_redactors": Redactor.objects.count(),
            "num_newspapers": Newspaper.objects.count(),
            "num_topics": Topic.objects.count(),
        }

        return render(request, "newspaper/index.html", context=context)


class NewspaperListView(LoginRequiredMixin, generic.ListView):

    model = Newspaper
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all()
        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(initial={
            "username": username
        })

        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        username = self.request.GET.get("username")

        if username:
            return queryset.filter(username__icontains=username)

        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspapers__topic")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")
