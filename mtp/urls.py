from django.conf.urls import re_path
from mtp import views
from django.views.generic import TemplateView

indexpatterns = [
	re_path(r'^$', views.IndexPageView.as_view(), name='index'),
	re_path(r'test/', TemplateView.as_view(template_name='test.html'), name='test'),
	re_path(r'about/',TemplateView.as_view(template_name='about.html'), name='about')
]