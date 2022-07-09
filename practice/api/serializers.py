from django.utils.text import slugify

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
#         slug_field='album_name'
#     )

#     class Meta:
#         model = Album
#         fields = ['id','album_name', 'artist', 'tracks']
#         lookup_field = 'slug'
#         extra_kwargs = {'url': {'lookup_field': 'slug'}}

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

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = TrackSerializer(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ['id','album_name', 'artist', 'tracks']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    track_slug = serializers.HyperlinkedIdentityField(view_name='album-detail')

    def get_track_slug(self, instance):
        return slugify(instance.album_name)

    class Meta:
        model = Album
        fields = ['url','id','album_name', 'artist', 'track_slug']

# class ExampleSerializer(serializers.ModelSerializer):
#     title_slug = serializers.SerializerMethodField()

#     def get_title_slug(self, instance):
#         return slugify(instance.title)

#     class Meta:
#         model = Example
#         fields = ("title_slug", )