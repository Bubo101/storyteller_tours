from rest_framework import serializers
from .models import Tour, Stop, SubStop

class SubStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubStop
        fields = '__all__'

class StopSerializer(serializers.ModelSerializer):
    sub_stop = SubStopSerializer(many=True, required=False)

    class Meta:
        model = Stop
        fields = '__all__'

    # def create(self, validated_data):
    #     sub_stop_data = validated_data.pop('sub_stop')
    #     stop = Stop.objects.create(**validated_data)
    #     for sub_stop_item in sub_stop_data:
    #         SubStop.objects.create(stop=stop, **sub_stop_item)
    #     return stop

class TourSerializer(serializers.ModelSerializer):
    stops = StopSerializer(many=True, required=False)

    class Meta:
        model = Tour
        fields = '__all__'

    # def create(self, validated_data):
    #     stops_data = validated_data.pop('stops')
    #     tour = Tour.objects.create(**validated_data)
    #     for stop_data in stops_data:
    #         sub_stops_data = stop_data.pop('sub_stop')
    #         stop = Stop.objects.create(tour=tour, **stop_data)
    #         for sub_stop_data in sub_stops_data:
    #             SubStop.objects.create(stop=stop, **sub_stop_data)
    #     return tour


'''
Why are the stop serializer and tour serializer more complicated than previous serializers written?

The StopSerializer and TourSerializer are more complicated than the previous serializers because they handle nested relationships and create related objects.

In the case of StopSerializer, it includes a nested serializer SubStopSerializer to handle the sub_stop relationship. 
This allows the serializer to handle the serialization and deserialization of SubStop instances that are related to a Stop instance. 
By using a nested serializer, we can control how the SubStop objects are represented and validated within the Stop serializer.

The StopSerializer also overrides the create method to handle the creation of related SubStop objects. When creating a Stop instance, 
the serializer extracts the sub_stop data from the validated data and creates the Stop object. 
Then, it iterates over the sub_stop data and creates the corresponding SubStop objects, associating them with the created Stop instance.

Similarly, the TourSerializer handles the nested relationship with Stop objects. 
It includes a nested serializer StopSerializer to handle the serialization and deserialization of the related Stop instances. 
The TourSerializer overrides the create method to handle the creation of related Stop and SubStop objects. 
It creates the Tour instance, then iterates over the stops data, creating the Stop objects. For each Stop object, it further creates the associated SubStop objects.

The complexity in these serializers arises from the need to handle nested relationships and properly manage the creation and association of related objects. 
By using nested serializers and custom create methods, 
we can handle the serialization and deserialization of nested data structures and maintain the integrity of the relationships between objects.
'''