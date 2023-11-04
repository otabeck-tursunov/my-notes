from rest_framework.serializers import ModelSerializer
from .models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'user')
        model = Note

    def create(self, validated_data):
        request = self.context.get('request')
        note = Note(
            title=validated_data.get('title'),
            content=validated_data.get('content'),
            created_at=validated_data.get('created_at'),
            updated_at=validated_data.get('updated_at'),
            user=request.user
        )
        note.save()
        return note
