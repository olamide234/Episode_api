from django.shortcuts import render
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import filters
from rest_framework import viewsets
from .serializers import EpisodeSerializer, CharacterSerializer, CommentSerializer, LocationSerializer
from .models import Episode, Character, Comment, Location

# Create your views here.
class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['released_date']

    def update(self, request, *args, **kwargs):
        episode = self.get_object()
        data = request.data
        episode.name = data['name']
        episode.released_date = data.get('released_date', episode.released_date)
        episode.episodeCode = data['episodeCode']
        
        for char in episode.characters.all():
            episode.characters.remove(char)

        given_characters = data['characters']
        for ch in given_characters:
            character = Character.objects.get(id=ch)
            episode.characters.add(character)

        # episodeComment = Comment.objects.get(id=data['episodeComments'])
        # episode.episodeComments.add(episodeComment)
        # episodeComment = Comment.objects.all()
        # for epcomment in episodeComment:
        # episode.episodeComments.add(episodeComment)
        episode.save()

        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        episode = self.get_object()
        episode.name = request.data.get('name', episode.name)
        episode.released_date = request.data.get('released_date', episode.released_date)
        episode.episodeCode = request.data.get('episodeCode', episode.episodeCode)

        data = request.data
        # episodeComment = Comment.objects.get(id=data['episodeComments'])
        # episode.episodeComments.add(episodeComment)

        given_characters = data.get('characters', None)
        if given_characters != None:
            for char in episode.characters.all():
                episode.characters.remove(char)

            for ch in given_characters:
                character = Character.objects.get(id=ch)
                episode.characters.add(character)
        else:
            pass

        episode.save()

        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [ django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gender', 'status']#, 'location'
    search_fields = ['$firstName', '$lastName', 'location__name']#'episodes__name'
    ordering_fields = ['firstName', 'lastName', 'gender']
    lookup_fields = 'id'

    def update(self, request, *args, **kwargs):
        character = self.get_object()
        data = request.data
        character.firstName = data['firstName']
        character.lastName = data['lastName']
        character.status = data['status']
        character.stateOfOrigin = data['stateOfOrigin']
        character.gender = data['gender']
        character.created = data.get('created', character.created)

        for episode in character.episodes.all():
            character.episodes.remove(episode)

        given_episode = data['episodes']
        for epi in given_episode:
            episode = Episode.objects.get(id=epi)
            character.episodes.add(episode)
        
        character.save()
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        character = self.get_object()
        data = request.data
        character.firstName = data.get('firstName', character.firstName)
        character.lastName = data.get('lastName', character.lastName)
        character.status = data.get('status', character.status)
        character.stateOfOrigin = data.get('stateOfOrigin', character.stateOfOrigin)
        character.gender = data.get('gender', character.gender)
        character.created = data.get('created', character.created)

        given_episodes = data.get('episodes', None)
        if given_episodes != None:
            for episode in character.episodes.all():
                character.episodes.remove(episode)

            for ep in given_episodes:
                episode = Episode.objects.get(id=ep)
                character.episodes.add(episode)
        else:
            pass

        character.save()
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    # def get_queryset(self):
    #     queryset = Character.objects.all()
    #     location = self.request.query_params.get('location', None)

    #     if location:
    #         import pdb; pdb.set_trace()
    #         queryset = queryset.filter(location__icontains=location)
    #     else:
    #         queryset

    #     return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['-created']

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer