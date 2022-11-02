from .models import Cadastro
from .serializers import CadastroSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"msg": "Cadastro finalizado com sucesso!"}, status=status.HTTP_201_CREATED, headers=headers)
