from rest_framework.routers import SimpleRouter
from .views import CadastroViewSet


router = SimpleRouter()
router.register('cadastros', CadastroViewSet)

