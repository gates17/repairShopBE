from rest_framework import serializers

from .models import Repairing


class RepairingSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Repairing
        fields = [
            'url',
            'id',
            'name',
            'description',
            'date_created',
        ]
        read_only_fields = ['id']

    def get_url(self, obj):
        # request
        request = self.context.get("request")

        print request.data
        return obj.get_product_url(request=request)

    def validate_title(self, value):
        qs = Repairing.objects.filter(name__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This title has already been used")
        return value

    """
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('name', instance.description)
        instance.save()
        return instance
    """
