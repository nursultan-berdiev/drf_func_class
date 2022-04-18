from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from django.forms.models import model_to_dict
import json

