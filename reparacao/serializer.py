from rest_framework.serializers import ModelSerializer,SerializerMethodField,SlugRelatedField

from .models import Reparacao, Cliente


class ReparacaoListSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)
    nome2 = SlugRelatedField(read_only=True,slug_field="name" )
    def get_url(self, obj):
        # request
        request = self.context.get("request")
        print "URL"
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name',
            'nome2',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget' ,
            'foto',
            'price',
            'materials',
            'faturado'
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
            'name',
            'nome2',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget' ,
            'foto',
            'price',
            'materials',
            'faturado'

        )
        read_only_fields = ['id,','date_created']

class ReparacaoDeleteSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)


    def get_url(self, obj):
        # request
        request = self.context.get("request")
        print "URL"
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name',
            'nome2',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget' ,
            'foto',
            'price',
            'materials',
            'faturado'

        )
        read_only_fields = ['id','date_created']

class ReparacaoUpdateSerializer(ModelSerializer):
        url = SerializerMethodField(read_only=True)

        def get_url(self, obj):
            # request
            request = self.context.get("request")
            print "URL"
            return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

        class Meta:
            model = Reparacao
            fields = (
                'url',
                'id',
                'name',
                'nome2',
                'description',
                'date_created',
                'date_completed',
                'weight',
                'budget',
                'foto',
                'price',
                'materials',
            'faturado'

            )
            read_only_fields = ['id', 'date_created']

class ReparacaoDetailSerializer(ModelSerializer):
    url = SerializerMethodField(read_only=True)

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        print "URL"
        return obj.get_reparacao_url(request=request) + "detail/" + str(obj.id)

    class Meta:
        model = Reparacao
        fields = (
            'url',
            'id',
            'name',
            'nome2',
            'description',
            'date_created',
            'date_completed',
            'weight',
            'budget',
            'foto',
            'price',
            'materials',
            'faturado'

        )
        read_only_fields = ['id', 'date_created']