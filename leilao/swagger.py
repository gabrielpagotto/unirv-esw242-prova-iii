from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Leilão API",
        description="Api para leilão da faculdade UniRV",
        default_version="v1",
        contact=openapi.Contact(email="gabriel.n.p.batista@academico.unirv.edu.br"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    authentication_classes=[],
)