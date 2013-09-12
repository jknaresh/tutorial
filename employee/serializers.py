from employee.models import Emp
from rest_framework import serializers
import time

class EmpSerializer(serializers.Serializer):
    pk = serializers.Field() # note: Field is an untyped read-only field
    name = serializers.CharField(required=False, max_length=50)
    role = serializers.CharField(required=False, max_length=50)
    exp = serializers.IntegerField(required=False,)
    #ts = serializers.CharField(default=int( time.time() ))
    
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.name = attrs.get('name',instance.name)
            instance.role = attrs.get('role', instance.role)
            instance.exp = attrs.get('exp', instance.exp)
            return instance
        
        #create new instance
        return Emp(**attrs)


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ('id','name','role','exp',)