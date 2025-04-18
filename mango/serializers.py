from rest_framework import serializers

from mango.models import Request, Portfolio, Image
from mango.mail import EmailMultiAlternatives


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        image = {
            "url": representation.pop("image"),
            "size": instance.image.size,
            "name": instance.image.name,
        }
        representation["image"] = image
        return representation

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            "business",
            "industry",
            "manager_name",
            "phone",
            "email",
            "budget",
            "needs",
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

class PortfolioSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(
            write_only=True,
            required=False,
            allow_null=True,
        ),
        write_only=True,
        required=False,
        allow_null=True,
    )
    image = ImageSerializer(many=True, required=False)
    class Meta:
        model = Portfolio
        fields = [
            "id",
            "name",
            "files",
            "image",
            "thumb",
            "created",
        ]

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     image = {
    #         "url": representation.pop("image"),
    #         "size": instance.image.size,
    #         "name": instance.image.name,
    #     }
    #     representation["image"] = image
    #     return representation

    def create(self, validated_data):
        files = validated_data.pop("files", [])
        instance = Portfolio.objects.create(**validated_data)

        images = []
        pic = ["png", "jpg", "jpeg"]
        for file in files:
            if file.name.split(".")[-1].lower() in pic:
                images.append(Image(image=file, board_id=instance.id))
            else:
                raise serializers.ValidationError("이미지 파일이 아닙니다.")
        Image.objects.bulk_create(images)
        return instance
