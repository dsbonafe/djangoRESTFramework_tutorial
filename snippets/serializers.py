# -*- coding: UTF-8 -*-
__author__ = 'douglas_bonafe'

from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
from rest_framework import permissions

# It's obsolet with ModelSerilizers!!!
#from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

# Bellow the wrong way to do the same above...
# PS.: But it works!!!

# class SnippetSerializer(serializers.Serializer):
#     # When we import from serializers.Serializer we don't need use __init__
#
#     pk = serializers.IntegerField(read_only=True)
#
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template' : 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Creates a new Snippet instance
#         :param validated_data:
#         :return: new Snippet instance
#         """
#         # Factory pattern
#
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Updates a existing Snippet
#         :param instance:
#         :param validated_data:
#         :return:a new Snippet instance (the updated Snippet)
#         """
#
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#
#         return instance


