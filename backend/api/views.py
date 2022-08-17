from drf_spectacular.utils import (OpenApiExample, OpenApiParameter,
                                   OpenApiTypes, extend_schema,
                                   extend_schema_view)
from rest_framework import mixins, viewsets

from api.models import FeedbackForm
from api.serializers import FormSerializer


@extend_schema_view(
    list=extend_schema(
        summary='Отображение списка сообщений формы',
        parameters=[
            OpenApiParameter(
                name='email', description='фильтрация по email', required=False, type=OpenApiTypes.EMAIL
            )
        ]
    ),
    create=extend_schema(
        summary='Отправка сообщения формы',
        examples=[
            OpenApiExample(
                name='пример запроса',
                value={'email': 'test@test.com', 'phone': '+79005005050', 'message': 'A test message'}
            )
        ],
        responses={201: FormSerializer}
    )
)
class FormViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = FeedbackForm.objects.all()
    filterset_fields = ('email', )
    serializer_class = FormSerializer
