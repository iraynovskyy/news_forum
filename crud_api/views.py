from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Preference
from .forms import PostForm
from .serializers import PostSerializer, UpdatePostSerializer


# Create your views here.
@api_view(["GET"])
def welcome(request):
    content = {"Message": "Welcome! It is a Home page!"}
    return JsonResponse(content)


@api_view(["GET"])
def index(request):
    allposts = Post.objects.all()

    serializer = PostSerializer(allposts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def user_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return Response(f"Username '{username}' is already taken.")
            elif User.objects.filter(email=email).exists():
                return Response(f"Email '{email}' is already taken.")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email
                )
                user.save()
                # print('user created')

        else:
            print("Passwords not matching...")
            return Response("Passwords not matching...!")

        return Response(f"User '{username}' created successfully!")


@api_view(["POST"])
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return Response(f"Hello, {user}, you are logged in!")
        else:
            messages.info(request, "invalid credentials")
            return Response(f'{"Please, register or enter valid credentials..."}')


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_creation(request):
    form = PostForm(request.POST)
    data = {}
    if form.is_valid():
        instance = form.save(commit=False)

        instance.author = request.user
        instance.save()

        data["response"] = "successfully added a new post."
        data["title"] = instance.title
        data["link"] = instance.link
        data["author"] = str(instance.author)

        return Response(data)
    return Response("the form is not valid...")


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def post_update(request, post_id):
    try:
        post = Post.objects.filter(pk=post_id)[0]
    except Post.DoesNotExist:
        return Response("dodnt exist")
    if request.method == "PUT":
        serializer = UpdatePostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response("serializer bad request 400error")

    return Response("the form is not valid...")


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def post_delete(request, post_id):
    try:
        post = Post.objects.filter(pk=post_id)[0]

    except IndexError:
        return Response("Object does not exist!")

    if request.method == "DELETE":
        operation = post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
            return Response(data=data)
        else:
            data["failure"] = "delete failed"
            return Response(data=data)


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def post_like(request, post_id):
    if request.method == "POST":
        eachpost = get_object_or_404(Post, id=post_id)

        try:
            obj = Preference.objects.get(user=request.user, post=eachpost)

            valueobj = (
                obj.value
            )  # value of userpreference: 0 - default; 1 - has liked already

            valueobj = int(valueobj)

            if valueobj == 1:
                context = {
                    "Message": "User has liked that post already!",
                    "eachpost": str(eachpost),
                    "post_id": post_id,
                }

                return Response(context)

        except Preference.DoesNotExist:
            upref = Preference()

            upref.user = request.user
            upref.post = eachpost

            upref.value = 1
            eachpost.upvotes += 1

            upref.save()
            eachpost.save()

            context = {
                "Message": "User has liked that post!",
                "eachpost": eachpost,
                "post_id": post_id,
            }

            return Response(
                {
                    "Message": "User has liked that post!",
                    "eachpost": str(eachpost),
                    "post_id": post_id,
                }
            )
