from rest_framework import serializers

from user.models import BalancerUser


class BalancerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalancerUser
        fields = ('id', 'tg_token', 'date_joined', 'created_at')

    def create(self, validated_data):
        tg_token = validated_data["tg_token"]
        user = BalancerUser.objects.create(
            tg_token=tg_token
        )
        return user
