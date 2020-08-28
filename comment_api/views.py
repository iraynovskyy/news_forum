from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Comment
from .forms import CommentForm
from .serializers import CommentSerializer, UpdateCommentSerializer


# Create your views here.
@api_view(["GET"])
def comments_all(request):
    allcomments = Comment.objects.all()

    serializer = CommentSerializer(allcomments, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def comment_creation(request):
    form = CommentForm(request.POST)
    data = {}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()

        data["response"] = "successfully added a new comment."
        data["content"] = instance.content
        data["author"] = str(instance.author)

        return Response(data)
    return Response("the form is not valid...")


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def comment_update(request, comment_id):
    try:
        comment = Comment.objects.filter(pk=comment_id)[0]
    except IndexError:
        return Response("Comment does not exist!")
    if request.method == "PUT":
        serializer = UpdateCommentSerializer(comment, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response("serializer bad request 400error")

    return Response("the form is not valid...")


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def comment_delete(request, comment_id):
    try:
        comment = Comment.objects.filter(pk=comment_id)[0]
    except IndexError:
        return Response("Comment does not exist!")

    if request.method == "DELETE":
        operation = comment.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
