from django.db import models
from multiselectfield import MultiSelectField
import datetime


class Request(models.Model):
    business = models.CharField(null=True, blank=True, max_length=50, verbose_name="회사명")
    industry = models.CharField(null=True, blank=True, max_length=50, verbose_name="업종")
    manager_name = models.CharField(null=True, blank=True, max_length=50, verbose_name="담당자명")
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name="연락처")
    email = models.EmailField(null=True, blank=True, verbose_name="이메일")
    budget = models.CharField(max_length=10, verbose_name="예산")
    needs = models.TextField("문의사항", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일")

    class Meta:
        verbose_name = "의뢰목록"
        verbose_name_plural = "의뢰목록"

class Portfolio(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50, verbose_name="이름")
    thumb = models.ImageField(verbose_name="썸네일이미지", upload_to="thumb/%Y/%m/%d")
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일")

    class Meta:
        verbose_name = "포토폴리오"
        verbose_name_plural = "포토폴리오"

class Image(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="image"
    )
    image = models.ImageField(verbose_name="이미지", upload_to="image/%Y/%m/%d")

    class Meta:
        verbose_name = "이미지"
        verbose_name_plural = "이미지"
