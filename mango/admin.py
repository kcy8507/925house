from django.contrib import admin
from mango.models import Request, Portfolio


class RequestAdmin(admin.ModelAdmin):
    list_filter = ["service"]
    # list_display = [
    #     "",
    #     "",
    #     "",
    #     "",
    #     "",
    #     "",
    # ]
    
    # def get_service_display(self, obj):
    #     return obj.get_service_display()
    
    # def get_request_display(self, obj):
    #     return obj.get_request_display()
    
    # get_service_display.short_description = "필요서비스"
    # get_request_display.short_description = "의뢰요청"

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]


admin.site.register(Request, RequestAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
