from django.contrib import admin
from .models import ChaiVarity,ChaiReview,store,ChaiCertificate
# Register your models here.

class chaiReviewInLine(admin.TabularInline):
    model= ChaiReview
    extra = 2

class chaiVarietyAdmin(admin.ModelAdmin):
    list_display  = ('name','type','date_added')
    inlines = [chaiReviewInLine]

class storeAdmin(admin.ModelAdmin):
    list_display = ['name','location']
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
     list_display = ['chai','certificate_number']


admin.site.register(ChaiVarity,chaiVarietyAdmin)
admin.site.register(store,storeAdmin)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)