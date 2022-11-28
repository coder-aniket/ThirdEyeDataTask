
from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    hr = serializers.CharField(read_only=True)
    in_time = serializers.DateTimeField(read_only=True)
    out_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Attendance
        fields = ['user', 'in_time', 'out_time', 'hr']