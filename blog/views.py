from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post
from .serializers import Post_Serialzer


@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    s = Post_Serialzer(posts, many=True)
    return Response(s.data)


@api_view(['GET'])
def get_one_post(request):
    pass
