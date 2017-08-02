from django.contrib import admin

from scriptsports.models import*
# Register your models here.
class GameshowAdmin(admin.ModelAdmin):
    list_per_page=50
    ordering = ('-game_time',)
    list_filter = ('game_time',)

class TalkAdmin(admin.ModelAdmin):
    list_per_page=50
    list_filter = ('ttime',)

class SharingAdmin(admin.ModelAdmin):
    list_per_page=50
    list_filter = ('share_time',)


admin.site.register(Regame)
admin.site.register(Newsleixin)
admin.site.register(Streamtvlogo)
admin.site.register(Gamebigleixin)
admin.site.register(News)
admin.site.register(Team)
admin.site.register(Tv)
admin.site.register(Man)
admin.site.register(Gameshow,GameshowAdmin)
admin.site.register(Gameleixin)
admin.site.register(Talk,TalkAdmin)
admin.site.register(Sharing,SharingAdmin)
admin.site.register(Video)
admin.site.register(Stream)
admin.site.register(Jijin)
admin.site.register(Nation)
admin.site.register(Important)
admin.site.register(Language)
admin.site.register(Sportsleixin)
admin.site.register(Author)
