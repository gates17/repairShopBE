from rest_framework import serializers

from .models import Reparacao

import datetime

class ReparacaoSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Reparacao
        fields = [
            'url',
            'id',
            'name',
            'description',
            'date_created',
            'date_completed',
        ]
        read_only_fields = ['id','date_created']



    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_reparacao_url(request=request)

    def validate_title(self, value):
        qs = Reparacao.objects.filter(name__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This name has already been used")
        self.instance.date_created=date.now()
        return value