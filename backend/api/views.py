from rest_framework import viewsets, mixins
from api.serializers import FormSerializer, FormWriteSerializer
from django_filters import rest_framework as filters
from api.models import FeedbackForm
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes, OpenApiExample


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
class FormViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FeedbackForm.objects.all()
    filterset_fields = ('email', )
    serializer_class = FormSerializer

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve', ):
    #         return FormSerializer
    #     return FormWriteSerializer
