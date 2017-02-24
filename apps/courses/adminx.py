#_*_coding:utf-8_*_
import xadmin

from models import Course,CourseResource,Vidoe,Lesson,BannerCourse
from organization.models import CourseOrg

class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResiurceInline(object):
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums','add_time','get_zjs_nums','go_to']
    #搜索框
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums']
    #过滤器
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums','add_time']
    ordering = ['-click_nums']
    list_editable = ['degree','desc']
    readonly_fields = ['click_nums',]
    exclude = ['fav_num']
    refresh_times = [3,5]
    inlines = [LessonInline,CourseResiurceInline]

    def queryset(self):
        qs = super(CourseAdmin,self).queryset()
        qs = qs.filter(is_banner=False)
        return qs
    def save_models(self):
        #在保存课程的时候统计机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not  None:
            course_org = obj.course_org
            course_org.course_num = Course.objects.filter(course_org=course_org).count()
            course_org.save()

xadmin.site.register(Course,CourseAdmin)

class BannerCourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums','add_time']
    #搜索框
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums']
    #过滤器
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_num','image','click_nums','add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums',]
    exclude = ['fav_num']
    inlines = [LessonInline,CourseResiurceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin,self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

xadmin.site.register(BannerCourse,BannerCourseAdmin)


class LessonAdmin(object):
    list_display = ['course','name','add_time',]
    #搜索框
    search_fields = ['course','name',]
    #过滤器
    list_filter = ['course','name','add_time',]

xadmin.site.register(Lesson,LessonAdmin)

class VidoeAdmin(object):
    list_display = ['lesson','name','add_time',]
    #搜索框
    search_fields = ['lesson','name',]
    #过滤器
    list_filter = ['lesson','name','add_time',]

xadmin.site.register(Vidoe,VidoeAdmin)

class CourseResourceAdmin(object):
    list_display = ['course','name','download','add_time',]
    #搜索框
    search_fields = ['lesson','name','download',]
    #过滤器
    list_filter = ['course','name','download','add_time',]

xadmin.site.register(CourseResource,CourseResourceAdmin)