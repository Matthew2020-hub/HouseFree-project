from django.shortcuts import get_object_or_404
from Authentication.models import User
from .serializers import EditProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    api_view, permission_classes, authentication_classes
)

# User profile's endpoint
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def profile(request, email):
    if request.method =='GET':
        try:
            user = get_object_or_404(User, email=email)
            email = user.email
            full_name = user.name
            phone_number = str(user.phone_number)
            profile_image = user.profile_image
            background_image = user.background_image
            entry_type = user.entry
            
            if not background_image and not profile_image:
                background_image = 'https://www.rocketmortgage.com/resources-cmsassets/RocketMortgage.com/Article_Images/Large_Images/TypesOfHomes/types-of-homes-hero.jpg'
                profile_image = 'https://www.rocketmortgage.com/resources-cmsassets/RocketMortgage.com/Article_Images/Large_Images/TypesOfHomes/types-of-homes-hero.jpg'
            context = {
                'email': email,
                'full_name': full_name,
                'phone_number': phone_number,
                'entry': entry_type,
                'background_image': background_image,
                'profile_image': profile_image
                }
            return Response(context,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response('User does not exist!', status=status.HTTP_204_NO_CONTENT)
    elif request.method =='PUT':
        serializer = EditProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['Full_name']
        phone_number = serializer.validated_data['Phone_number']
        user_email = serializer.validated_data['Email']
        profile_image = serializer.validated_data['Profile_image']
        background_image = serializer.validated_data['Background_image']
        location = serializer.validated_data['Location']
        get_user = User.objects.filter(email=email)
        get_user.name=name
        get_user.profile_image=profile_image
        get_user.background_image=background_image
        get_user.email=user_email
        get_user.phone_number=phone_number
        get_user.agent_location=location
        context = {
            'message': 'Profile Update is sucessful',
            'data': serializer.data
            }
        return Response(context, status=status.HTTP_200_OK)
