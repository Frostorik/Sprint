from rest_framework import serializers
from .models import Users, PerevalAdded, Coords, PerevalAreas, PerevalImages, SprActivitiesTypes


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'phone', 'password', 'fam', 'name', 'otc')


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('id', 'latitude', 'longitude', 'height')


class PerevalAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = ('id', 'id_parent', 'title')


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ('id', 'date_added', 'img')


class SprActivitiesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprActivitiesTypes
        fields = ('id', 'title')


class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coord_id = CoordsSerializer()
    images = PerevalImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = (
        'id', 'raw_data', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'winter_level', 'summer_level', 'autumn_level', 'spring_level', 'coord_id', 'images', 'status')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Users.objects.get_or_create(**user_data)[0]

        coord_data = validated_data.pop('coord_id')
        coord = Coords.objects.get_or_create(**coord_data)[0]

        images_data = validated_data.pop('images', [])
        images = []
        for img_data in images_data:
            img = PerevalImages.objects.create(**img_data)
            images.append(img)

        pereval_added = PerevalAdded.objects.create(user=user, coord_id=coord, **validated_data)
        pereval_added.images.set(images)
        return pereval_added
