from django.http import JsonResponse
from .forms import PostForm
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)


    posts_serializer = PostSerializer(posts, many=True)
    user_sterializer = UserSerializer(user)

    return JsonResponse({'posts': posts_serializer.data, 
                         'user': user_sterializer.data},
                         safe=False)



@api_view(['POST'])
def post_create(request):
    data = request.data

    form = PostForm(request.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({"error" : "something went wrong"})