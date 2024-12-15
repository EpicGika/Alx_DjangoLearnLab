from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        notification_data = [{
            'actor': notification.actor.username,
            'verb': notification.verb,
            'timestamp': notification.timestamp,
            'is_read': notification.is_read
        } for notification in notifications]

        return Response(notification_data)
