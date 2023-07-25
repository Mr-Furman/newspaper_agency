from django.urls import path
from newspaper.views import (
    IndexView,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView
)

urlpatterns = [
    path("",
         IndexView.as_view(),
         name="index"),
    path("newspapers/",
         NewspaperListView.as_view(),
         name="newspaper-list"),
    path("newspapers/<int:pk>/",
         NewspaperDetailView.as_view(),
         name="newspaper-detail"),
    path("newspapers/create/",
         NewspaperCreateView.as_view(),
         name="newspaper-create",),
    path("newspapers/<int:pk>/update/",
         NewspaperUpdateView.as_view(),
         name="newspaper-update",),
    path("newspapers/<int:pk>/delete/",
         NewspaperDeleteView.as_view(),
         name="newspaper-delete",),
    path("redactors/",
         RedactorListView.as_view(),
         name="redactor-list"),
    path("redactors/<int:pk>/",
         RedactorDetailView.as_view(),
         name="redactor-detail"),
    path("redactors/create/",
         RedactorCreateView.as_view(),
         name="redactor-create"),
    path("redactors/<int:pk>/update/",
         RedactorUpdateView.as_view(),
         name="redactor-update"),
    path("redactors/<int:pk>/delete/",
         RedactorDeleteView.as_view(),
         name="redactor-delete"),
    path("topics/",
         TopicListView.as_view(),
         name="topic-list"),
    path("topics/create/",
         TopicCreateView.as_view(),
         name="topic-create"),
    path("topics/<int:pk>/update/",
         TopicUpdateView.as_view(),
         name="topic-update"),
    path("topics/<int:pk>/delete/",
         TopicDeleteView.as_view(),
         name="topic-delete"),
]

app_name = "newspaper"
