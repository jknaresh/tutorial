from django.conf.urls import patterns, url

urlpatterns = patterns('employee.views',
    url(r'emp/$','emp_list', name='employee_list'),
    url(r'emp/(?P<pk>[0-9]+)/$', 'emp_detail', name='employee_detail'),
    url(r'emp-thum/(?P<pk>[0-9]+)/$', 'emp_thum', name='employee_thum')
)

