#_*_coding:utf-8_*_
import xadmin
from xadmin import views
from xadmin.views import CommAdminView
from xadmin.plugins.auth import UserAdmin
from models import EmaliVerifyRecord,Banner
from courses.models import Course,Lesson,CourseResource,Vidoe
from operation.models import UserAsk,UserCourse,UserFavorite,UserMessage,CourseComment
from organization.models import CityDict,CourseOrg,Teacher

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetrtings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"

class EmaliVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time',]
    #搜索框
    search_fields = ['code','email','send_type']
    #过滤器
    list_filter = ['code','email','send_type','send_time',]
    model_icon = 'fa fa-address-card-o'



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time' ]
    # 搜索框
    search_fields = ['title', 'image', 'url', 'index',]
    # 过滤器
    list_filter = ['title', 'image', 'url', 'index','add_time'  ]
    model_icon = 'fa fa-area-chart'


xadmin.site.register(EmaliVerifyRecord,EmaliVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetrtings)

#class UserProfileAdmin(UserAdmin):
'''定制user界面显示'''
#    def get_form_layout(self):
#        if self.org_obj:
#            self.form_layout = (
#                Main(
#                    Fieldset('',
#                             'username', 'password',
#                             css_class='unsort no_title'
#                             ),
#                    Fieldset(_('Personal info'),
#                             'first_name', 'last_name',
#                             'email'
#                             ),
#                    Fieldset(_('Permissions'),
#                             'groups', 'user_permissions'
#                             ),
#                    Fieldset(_('Important dates'),
#                             Row('last_login', 'date_joined'),
#                             ),
#                ),
#                Side(
#                    Fieldset(_('Status'),
#                             'is_active', 'is_staff', 'is_superuser',
#                             ),
#                )
#            )
#        return super(UserAdmin, self).get_form_layout()