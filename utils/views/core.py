from rest_framework import viewsets
from users.models import CustomUser
from clients.models import ClientProfile
from caregivers.models import CaregiverProfile
from jobs.models import Job
from payments.models import Payment
from reviews.models import Review
from chat.models import Message

from utils.serializers.core import (
    UserSerializer, ClientProfileSerializer, CaregiverProfileSerializer,
    JobSerializer, PaymentSerializer, ReviewSerializer, MessageSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ClientProfileViewSet(viewsets.ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

class CaregiverProfileViewSet(viewsets.ModelViewSet):
    queryset = CaregiverProfile.objects.all()
    serializer_class = CaregiverProfileSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer