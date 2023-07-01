from django.shortcuts import render
from comments.models import Comment
from comments.serializers import CommentSerializer


# Create your views here.

from rest_framework import generics


class CommentGeneric(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"
