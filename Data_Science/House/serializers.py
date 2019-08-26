from .models import Home
from rest_framework import serializers
from .lnr import Data

class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        fields = '__all__'

    def create(self, validated_data):
        area = validated_data.__getitem__('area')
        seria = validated_data.__getitem__('seria')
        region=validated_data.__getitem__('region')
        rooms = validated_data.__getitem__('rooms')
        floor = validated_data.__getitem__('floor')
        furniture = validated_data.__getitem__('heating')
        price = validated_data.__getitem__('price')
        h = Home(area=area, seria=seria, rooms=rooms, floor=floor, heating=heating)
        print(h)
        a = []
        a.append(h.rooms)
        a.append(h.seria)
        a.append(h.region)
        a.append(h.area)
        a.append(h.heating)
        a.append(h.floor)
        e = []
        e.append(a)
        print(e)

        d = Data.data_min(e)
        prediction = int(d[0])
        price = prediction
        h.price = price
        h.save()
        print(h)
        return h
