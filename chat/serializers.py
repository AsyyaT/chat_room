from rest_framework import serializers
import re
from chat.models import Message

#
# def validate_message(value):
#     if not re.match(r"^\w+([-]?\w+)*@\w+([-]?\w+)*(\.\w{2,3})+$", value):
#         raise serializers.ValidationError("Your email don't valid")
#     return value
#
#
# class MessageSerializer(serializers.Serializer):
#     email = serializers.EmailField(allow_null=False, allow_blank=False, validators=[validate_message])
#
# #


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'email', 'text')

    # def validate(self, data):
    #     errors = {}
    #     email = data.get('email')
    #
    #     if not re.match(r"^\w+([-]?\w+)*@\w+([-]?\w+)*(\.\w{2,3})+$", email):
    #         errors['error'] = u'You\'re an idiot!'
    #         raise serializers.ValidationError(errors)
    #
    #     return data


class MessageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'email', 'text', 'dt_created', 'dt_updated')


#
# class MessageCreateSerializers(serializers.Serializer):
#     email = serializers.EmailField(allow_null=False)
#     text = serializers.CharField(allow_null=False, allow_blank=False, max_length=100)
#
#     def create(self, validated_data):
#         return Message.objects.create(**validated_data)
#     #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.dt_created = validated_data.get('dt_created', instance.dt_created)
    #     instance.dt_updated = validated_data.get('dt_created', instance.dt_updated)
    #     instance.save()
    #     return instance
