class exampleSerializer(serializers.ModelSerializer):
    last_log = serializers.SerializerMethodField()

    class Meta:
        db_table = 'example'
        model = ExampleModel
        fields = ('id', 'last_log', 'quantity')

    def get_last_log(self, obj):
        last_log = obj.state(self.context['last_log'])
        last_log_serializer = LoggerSerializer(last_log)
        return last_log_serializer.data




from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ('mobile_number',)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_number',)


class UserSerializer(serializers.ModelSerializer):
    userdetail = UserDetailSerializer()
    account = AccountSerializer()
    user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('userdetail', 'account', 'user')

    def get_user(self, obj):
        return {
            'first_name': 'obj.first_name',
            'last_name': 'obj.last_name',
            'email': 'obj.email',
            }




Serialize M2M relation with through table
class Packing(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50,blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    packing = models.ManyToManyField(Packing,related_name='products',through='Presentation')

class Presentation(models.Model):
    product = models.ForeignKey(Product)
    packing = models.ForeignKey(Packing)
    weight = models.DecimalField(decimal_places=3,max_digits=10)
    price = models.DecimalField(decimal_places=2,max_digits=10)

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation

class ProductSerializer(serializers.ModelSerializer):
    packing = PresentationSerializer(many=True,read_only=True,)
    class Meta:
        model = Product
        fields = ('name','packing')
# The expected result:

# {
#     'name': 'produt',
#     'packing': [
#         {'name':'abcd','size':'big','weight':200,'price':222.22},
#         {'name':'qwert','size':'small','weight':123,'price':534.21},
#         {'name':'foo','size':'xxx','weight':999,'price':999.99}
#     ]
# }




# https://www.geeksforgeeks.org/serializer-relations-django-rest-framework/#getting_started