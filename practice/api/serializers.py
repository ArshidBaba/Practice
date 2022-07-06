from rest_framework import serializers


from .models import Album, Track

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

# class AlbumSerializer(serializers.ModelSerializer):  Pending 
#     """
#     HyperLinkedRelatedField
#     """

#     tracks = serializers.HyperlinkedRelatedField(
#         many=True, 
#         read_only=True,
#         # source='pk',
#         view_name='track-detail'
#     )

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']

# class AlbumSerializer(serializers.ModelSerializer):
#     """
#     SlugRelatedField
#     """
#     tracks = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='title'
#     )

#     class Meta:
#         model = Album
#         fields = ['id','album_name', 'artist', 'tracks']

# class AlbumSerializer(serializers.HyperlinkedModelSerializer):  Pending
#     """
#     HyperLinkedIdentityField.
#     """
#     track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'track_listing']

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id','album_name', 'artist', 'tracks']