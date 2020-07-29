from django.contrib import admin
from To_Do.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('supervisor', 'title', 'category', 'description', 'task_done', 'start_date', 'end_date', 'developer')
    search_fields = ('developer__username', 'supervisor__username','title',)
    list_filter = ('task_done', 'category', )
    list_editable = ('task_done',)

    # def get_ordering(self, request):
    #     if request.user.is_superuser:
    #         return ('title', '-start_date')
    #     return ('title',)


admin.site.register(Task, TaskAdmin)
