from django.db import models
from multiselectfield import MultiSelectField
import datetime


class Request(models.Model):
    need_to_services = (
        (0, '웹사이트'),
        (1, '앱개발'),
        (2, 'BI/BX'),
        (3, '마케팅'),
        (4, '유지보수'),
        (5, '영상제작'),
        (6, '카탈로그'),
        (7, '컨설팅'),
        (8, '인터뷰요청'),
        (9, '기타문의'),
    )
    need_to_requests = (
        (0, '신규구축'),
        (1, '개선구축'),
        (2, '컨설팅'),
        (3, '유지보수'),
        (4, '기타'),
    )

    service = MultiSelectField(choices=need_to_services, max_length=10, max_choices=10, verbose_name="필요서비스")
    company_name = models.CharField(null=True, blank=True, max_length=50, verbose_name="회사명")
    manager_name = models.CharField(null=True, blank=True, max_length=50, verbose_name="담당자명")
    phone = models.CharField(null=True, blank=True, max_length=15, verbose_name="연락처")
    email = models.EmailField(null=True, blank=True, verbose_name="이메일")
    request = MultiSelectField(choices=need_to_requests, max_length=5, max_choices=5, verbose_name="의뢰요청")
    started = models.DateField(verbose_name="예상시작일", default=datetime.date(2024, 1, 1))
    ended = models.DateField(verbose_name="예상종료일", default=datetime.date(2030, 12, 31))
    budget = models.CharField(max_length=10, verbose_name="예산")
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성일")

    class Meta:
        verbose_name = "의뢰목록"
        verbose_name_plural = "의뢰목록"
