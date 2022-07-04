from rest_framework import serializers


from .models import Album

# class AlbumSerializer(serializers.ModelSerializer):
#     """
#     StringRelatedField
#     """
#     tracks = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

# class AlbumSerializer(serializers.ModelSerializer):
#     """
#     PrimaryKeyRelatedField
#     """

#     tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

class AlbumSerializer(serializers.ModelSerializer):
    """
    HyperLinkedRelatedField
    """

    tracks = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True,
        # source='pk',
        view_name='tracks'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']