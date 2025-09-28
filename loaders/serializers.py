from rest_framework import serializers
from .models import Loader
import re

class LoaderSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='group_id')

    class Meta:
        model = Loader
        fields = ['pk', 'id', 'css', 'is_light', 'created_at', 'updated_at']
        read_only_fields = ['pk', 'created_at', 'updated_at']

    def validate_css(self, value):
        """
        Multi-line CSS ni compact qiladi, JSON formatiga mos qiladi
        Har doim class nomi: loader-{group_id}-{pk}
        content:"..." ichidagi \A lar saqlanadi
        """
        import re

        # group_id va pk
        group_id = self.initial_data.get('id') or getattr(self.instance, 'group_id', 'classic')
        pk = self.instance.pk if self.instance and self.instance.pk else '0'
        class_name = f"loader-{group_id}-{pk}"

        # 1. comment larni olib tashlash
        value = re.sub(r'/\*.*?\*/', '', value, flags=re.DOTALL)
        # 2. bo'sh joy va newline larni olib tashlash (content:"..." ichida emas)
        def remove_spaces(match):
            content = match.group(0)
            if 'content:' in content:
                return content  # content:"..." ichidagi \A ni saqlaymiz
            return re.sub(r'\s+', ' ', content).strip()
        value = re.sub(r'.*?;', remove_spaces, value)
        # 3. .loader yoki eski loader-xxx-yyy classlarni yangisiga almashtirish
        value = re.sub(r'\.loader(-[a-zA-Z0-9-]+)?', f'.{class_name}', value)
        # 4. JSON escape va ortiqcha \ belgilarni olib tashlash (content:"..." ichidagi \A saqlansin)
        value = re.sub(r'\\(?=[^A])', '', value)  # \ dan keyin A bo'lmasa olib tashlash
        value = value.replace(r'\"', '"')

        return value






