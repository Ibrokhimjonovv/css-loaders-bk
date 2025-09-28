from rest_framework import viewsets
from .models import Loader
from .serializers import LoaderSerializer

class LoaderViewSet(viewsets.ModelViewSet):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer

    def perform_create(self, serializer):
        # 1. Objectni saqlaymiz
        loader = serializer.save()
        # 2. CSS ni haqiqiy PK bilan yangilaymiz
        class_name = f"loader-{loader.group_id}-{loader.pk}"
        import re

        css = re.sub(r'/\*.*?\*/', '', loader.css, flags=re.DOTALL)
        css = re.sub(r'\s+', ' ', css).strip()
        css = re.sub(r'\.loader(-[a-zA-Z0-9-]+)?', f'.{class_name}', css)
        css = css.replace(r'\"', '"')
        css = css.replace('\\', '')

        loader.css = css
        loader.save()
