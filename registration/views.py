from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mongo import get_mongo_client

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        client, db = get_mongo_client()
        users_collection = db['users']

        if users_collection.find_one({'email': email}):
            return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = {
            'username': username,
            'email': email,
            'password': password  # ⚠️ NOTE: In production, hash the password!
        }
        users_collection.insert_one(user)
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        client, db = get_mongo_client()
        users_collection = db['users']

        user = users_collection.find_one({'email': email, 'password': password})
        if user:
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
