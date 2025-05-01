from rest_framework import serializers
from ht_app.models import Community

class CommSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('id', 'name', 'description', 'updates', 'image')
