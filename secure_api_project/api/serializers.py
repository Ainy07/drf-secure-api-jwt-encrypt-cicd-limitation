from rest_framework import serializers
from .models import SecureData

class SecureDataSerializer(serializers.ModelSerializer):
    plain_text = serializers.CharField(write_only=True)
    decrypted_text = serializers.SerializerMethodField()

    class Meta:
        model = SecureData
        fields = ['id', 'plain_text', 'decrypted_text']  

    def create(self, validated_data):
        plain_text = validated_data.pop('plain_text')
        obj = SecureData()
        obj.save_encrypted(plain_text)
        return obj

    def get_decrypted_text(self, obj):
        return obj.get_decrypted()
