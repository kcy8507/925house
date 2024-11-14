from rest_framework import serializers

from mango.models import Request
from mango.mail import EmailMultiAlternatives


class RequestSerializer(serializers.ModelSerializer):
    # applicant_count = serializers.SerializerMethodField(read_only=True)
    service = serializers.ListField(
        child=serializers.ChoiceField(choices=Request.need_to_services)
    )
    request = serializers.ListField(
        child=serializers.ChoiceField(choices=Request.need_to_requests)
    )

    class Meta:
        model = Request
        fields = [
            "service",
            "company_name",
            "manager_name",
            "phone",
            "email",
            "request",
            "started",
            "ended",
            "budget",
        ]
    
    def create(self, validated_data):
        with open("email.html", "r", encoding="utf-8") as file:
            mail = file.read()
        title = '[망고소프트] 홈페이지 연락'
        html_content = mail
        mail_msg = EmailMultiAlternatives(subject=title, to=['hyunga127@gmail.com'], body='홈페이지에서 의뢰함.')
        mail_msg.attach_alternative(html_content, "text/html")
        mail_msg.send()
        return super().create(validated_data)
    # def get_applicant_count(self, obj):
    #     return obj.schedule_date.count()
    # def validate(self, attrs):
    #     filter_arg = {"schedule_date": attrs.get("schedule_date")}
    #     participation = Participation.objects.filter(**filter_arg)
    #     if participation.count() >= 38:
    #         raise serializers.ValidationError("해당 날짜의 정원이 차서 신청이 불가능합니다.")
    #     return super().validate(attrs)