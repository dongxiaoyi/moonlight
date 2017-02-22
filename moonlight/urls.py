#_*_encoding:utf-8_*_

from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from users.views import LoginView,LogoutView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from  organization.views import OrgView
from django.views.static import serve
from moonlight.settings import MEDIA_ROOT,STATIC_ROOT
from users.views import IndexView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(),name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
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
    # 配置静态资源的访问处理函数
    url('^static/(?P<path>.*)', serve, {'document_root': STATIC_ROOT}),

]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'