from rest_framework         import serializers
from mapsapp.models.user    import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'name', 'last_name', 'email']

    def to_representation(self,  obj):
            user = User.objects.get(id = obj.id)
            return {
                'id'                   : user.id,
                'name'                 : user.name,
                'last_name'            : user.last_name,
                'email'                : user.email,
            }