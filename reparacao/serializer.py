from rest_framework.serializers import ModelSerializer,SerializerMethodField,SlugRelatedField

from .models import Reparacao, Cliente

class ReparacaoListSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)
    name_id = SlugRelatedField(read_only=True,slug_field="name" )
    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name_id',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget' ,
            'foto',
            'price',
            'materials',
            'faturado',
            'pagamento_parcial',
            'pago',
            'discount',
            'quantity',
            'units',
            'tax',
            'tax_to_pay',
            'total_to_pay',
            'total_to_pay_with_tax'

        )
        read_only_fields = ['id','date_created']

class ReparacaoCreateSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name_id',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget' ,
            'foto',
            'price',
            'materials',
            'faturado',
            'pagamento_parcial',
            'pago',
            'discount',
            'quantity',
            'units',
            'tax',
            'tax_to_pay',
            'total_to_pay',
            'total_to_pay_with_tax'

        )
        read_only_fields = ['id,','date_created']

class ReparacaoDeleteSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)


    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name_id',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget' ,
            'foto',
            'price',
            'materials',
            'faturado',
            'pagamento_parcial',
            'pago',
            'discount',
            'quantity',
            'units',
            'tax',
            'total_to_pay'

        )
        read_only_fields = ['id','date_created']

class ReparacaoUpdateSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)



    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name_id',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget',
            'foto',
            'price',
            'materials',
            'faturado',
            'pagamento_parcial',
            'pago',
            'discount',
            'quantity',
            'units',
            'tax',
            'tax_to_pay',
            'total_to_pay',
            'total_to_pay_with_tax'


        )
        read_only_fields = ['id', 'date_created']

class ReparacaoDetailSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)
    name_id = SlugRelatedField(read_only=True,slug_field="name" )

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name_id',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget',
            'foto',
            'price',
            'materials',
            'faturado',
            'pagamento_parcial',
            'pago',
            'discount',
            'quantity',
            'units',
            'tax',
            'tax_to_pay',
            'total_to_pay',
            'total_to_pay_with_tax'
        )
        read_only_fields = ['id', 'date_created']