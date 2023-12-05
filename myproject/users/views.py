from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserRegisterSerializer, LoginSerializer, UserHeaderSerializer, RegistrationConfirmView
from .models import User, OneTimePassword
from .utils import send_generated_otp_to_email


class RegisterSendOTPView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            user_data = serializer.data
            send_generated_otp_to_email(user_data['email'], request)

            return Response({
                'data': user_data,
                'message': 'waiting otp verify'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterConfirmView(GenericAPIView):
    serializer_class = RegistrationConfirmView

    def post(self, request, commit=False):
        try:
            passcode = request.data
            user_pass_obj = OneTimePassword.objects.filter(email=request.data.get('email')).first()
            serializer = self.serializer_class(data=passcode)

            if serializer.is_valid(raise_exception=True) and serializer.data['otp'] == user_pass_obj.otp:
                return Response({
                    # 'data': user_data,
                    'message': 'thanks for signing up, start creating'
                }, status=status.HTTP_200_OK)
            return Response({
                'messege''otp uncorrect'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class RegisterCreateView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                # 'data': user_data,
                'message': 'thanks for signing up, start creating'
            }, status=status.HTTP_201_CREATED)
        return Response({},status=status.HTTP_400_BAD_REQUEST)



class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        try:
            passcode = request.data.get('otp')
            user_pass_obj = OneTimePassword.objects.filter(email=request.data.get('email')).first()
            user = user_pass_obj.user
            if not user:
                user.is_verified = True
                user.save()
                return Response({
                    'message': 'account email verified successfully'
                }, status=status.HTTP_200_OK)
            return Response({'message': 'passcode is invalid user is already verified'},
                            status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist as identifier:
            return Response({'message': 'passcode not provided'}, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TestAuthView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {'it': 'works'}
        return Response(data, status=status.HTTP_200_OK)
# Create your views here.
