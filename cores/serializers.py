from rest_framework import serializers
from .models import Episode, Character, Comment, Location

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comments', 'ipAddressLocation', 'created', 'episode']

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude', 'character_id']

class LocationNestedWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'latitude', 'longitude']

# class CharacterWriteSerializer(serializers.RelatedField):
#     def to_internal_value(self, data):
#         import pdb; pdb.set_trace()
#         validated_data = self.run_validation(data)
        
#         return validated_data

#     def to_representation(self, value):
#         return self.name

#     def __init__(self, **kwargs):
#         kwargs['read_only']= False
#         super().__init__(**kwargs)

class EpisodeReadWriteSerializerMethodField(serializers.SerializerMethodField):
    def __init__(self, method_name=None, **kwargs):
        self.method_name = method_name
        # kwargs['source'] = '*'
        super(serializers.SerializerMethodField, self).__init__(**kwargs)

    def to_internal_value(self, value):       
        return {self.field_name:value}
 

    class Meta:
        model = Episode
        

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    # episodes = serializers.StringRelatedField(many=True)
    episodes = EpisodeReadWriteSerializerMethodField()
    # location = serializers.StringRelatedField()
    location = LocationNestedWriteSerializer()
    
    class Meta:
        model = Character
        fields = ['id', 'firstName', 'lastName', 'status', 'stateOfOrigin', 'gender', 'location', 'episodes']

    def get_episodes(self, obj):
        episods= []
        for i in obj.get_queryset():
            # import pdb; pdb.set_trace()
            episods.append(str(i))
        return episods

    def create(self, validated_data):
        location = validated_data['location']
        del validated_data['location']
        
        episodes = validated_data['episodes']['episodes']
        del validated_data['episodes']

        #to attach location and remaining validated_data to a new character
        locale = Location.objects.create(**location)
        character, created = Character.objects.update_or_create(**validated_data, location=locale)#this is used when OneToOneField is involved, to create and attach
        #to save the newly created location to include connecting primary key(i.e character_id)
        locale.save()

        # to attach episode(s) to the created character
        ep = []
        for episode in episodes:
            obj = Episode.objects.get(pk=episode)
            ep.append(obj)

        character.episodes.set(ep)
        
        character.save()

        return character

class CharacterReadWriteSerializerMethodField(serializers.SerializerMethodField):
    def __init__(self, method_name=None, **kwargs):
        self.method_name = method_name
        # kwargs['source'] = '*'
        super(serializers.SerializerMethodField, self).__init__(**kwargs)

    def to_internal_value(self, value):     
        return {self.field_name:value}
 

    class Meta:
        model = Character

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    count_comments = serializers.SerializerMethodField(method_name='get_count_comments')
    characters = CharacterReadWriteSerializerMethodField()
    # characters = serializers.StringRelatedField(many=True) #read_only=True
    episodeComments = serializers.StringRelatedField(many=True, read_only=True)
    

    class Meta:
        model = Episode
        fields = ['id', 'name', 'released_date', 'episodeCode', 'characters', 'episodeComments', 'count_comments']

    def get_characters(self, obj):
        char= []
        for i in obj.get_queryset():
            # import pdb; pdb.set_trace()
            char.append(str(i))
        return char


    # writable nested serializer
    def create(self, validated_data):
        # this is used for nested serializer(e.g episodeComments = CommentSerializer(many=True))
        # episodeComments = validated_data['episodeComments']
        # del validated_data['episodeComments']
        
        characters = validated_data['characters']['characters']
        del validated_data['characters']

        episode = Episode.objects.create(**validated_data)
        ch = []
        for character in characters:
            obj = Character.objects.get(pk=character)
            ch.append(obj)

        episode.characters.set(ch)

        # this is used for nested serializer(e.g episodeComments = CommentSerializer(many=True)) in continuation 
        # for episodeComment in episodeComments:
        #     comment = Comment.objects.create(**episodeComment)
        #     episode.episodeComments.add(comment)
        
        episode.save()

        return episode

    def get_count_comments(self, obj):
        # return obj.count_comments()
        return obj.episodeComments.all().count()



