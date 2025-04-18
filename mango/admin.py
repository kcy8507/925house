from django import forms
from django.contrib import admin
from mango.models import Request, Portfolio, Image
from django.forms.models import BaseInlineFormSet


class ImageInlineFormSet(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        files = form.files.getlist("image")
        instances = []
        for f in files:
            instance = Image(portfolio=form.cleaned_data["portfolio"], image=f)
            if commit:
                instance.save()
            instances.append(instance)
        return instances

class ImageInlineForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        required=False,
    )

    class Meta:
        model = Image
        fields = ["image"]

class ImageInline(admin.StackedInline):
    model = Image
    form = ImageInlineForm
    formset = ImageInlineFormSet
    extra = 1

class RequestAdmin(admin.ModelAdmin):
    # list_filter = ["service"]
    list_display = [
        "business",
        "industry",
        "email",
        "budget",
        "created",
    ]
    
    # def get_service_display(self, obj):
    #     return obj.get_service_display()
    
    # def get_request_display(self, obj):
    #     return obj.get_request_display()
    
    # get_service_display.short_description = "필요서비스"
    # get_request_display.short_description = "의뢰요청"

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]
    inlines = [ImageInline]


admin.site.register(Request, RequestAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
