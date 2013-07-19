from django.conf.urls import patterns, url
from grants import views

urlpatterns = patterns(
    '',
    url(r'^grants/', views.GrantList.as_view()),
    url(r'^regulations/', views.RegulationList.as_view()),
    url(r'^organizations/', views.OrganizationList.as_view()),
    url(r'^ministries/', views.MinistryList.as_view()),
)
