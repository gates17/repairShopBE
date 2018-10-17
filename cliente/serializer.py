from rest_framework import serializers

from .models import Cliente

from datetime import date

class ClienteSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cliente
        fields = [
            'url',
            'id',
            'name',
            'address',
            'date_created',
            'tlf',
            'zip_code',
            'localidade',
            'total_spent_by_client'
        ]
        read_only_fields = ['id','date_created','total_spent_by_client']



    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_cliente_url(request=request) + "detail/" + str(obj.id)

    def validate_title(self, value):
        qs = Cliente.objects.filter(name__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This name has already been used")
        self.instance.date_created=date.now()
        return value