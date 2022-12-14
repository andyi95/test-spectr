from rest_framework import serializers

from api.models import FeedbackForm


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedbackForm
        fields = '__all__'
