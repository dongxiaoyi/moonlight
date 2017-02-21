#_*_encoding:utf-8_*_

from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from  organization.views import OrgView
from django.views.static import serve
from moonlight.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"),name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/',include('captcha.urls')),
    url('^active/(?P<active_code>.*)/$',ActiveUserView.as_view(), name="user_active"),
    url('^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url('^reset/(?P<reset_code>.*)/$',ResetView.as_view(), name="reset_pwd"),
    url('^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    #课程机构url
    url(r'^org/', include('organization.urls',namespace='org'),),
    #课程相关url
    url(r'^course/', include('courses.urls',namespace='course'),),
    # 个人中心相关url
    url(r'^users/', include('users.urls', namespace='users'), ),
    #配置上传文件的访问处理函数
    url('^media/(?P<path>.*)', serve,{'document_root':MEDIA_ROOT}),

]
