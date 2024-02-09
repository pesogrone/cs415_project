from calendar import c
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, Categories, Items, Orders, Payment, Profile, Reviews, Transactions
from cs415.serializers import UserSerializer , CategoriesSerializer, ItemsSerializer, OrdersSerializer, PaymentSerializer, ProfileSerializer, ReviewsSerializer, TransactionsSerializer

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class SingleUserAPIView(APIView):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        serializer = UserSerializer(user)
        return Response({'users': serializer.data})
class CategoriesAPIView(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response({'categories': serializer.data})
class ItemsAPIView(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response({'items': serializer.data})
class OrdersAPIView(APIView):
    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response({'orders': serializer.data})
class PaymentAPIView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response({'payments': serializer.data})
class ProfileAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response({'profiles': serializer.data})
class ReviewsAPIView(APIView):
    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response({'reviews': serializer.data})
class TransactionsAPIView(APIView):
    def get(self, request):
        transactions = Transactions.objects.all()
        serializer = TransactionsSerializer(transactions, many=True)
        return Response({'transactions': serializer.data})
class login(APIView):
    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        if user.password == request.data['password']:
            return Response({'status': 'success'})
        else:
            return Response({'status': 'failed'})
class register(APIView):
    def post(self, request):
        user = User.objects.create(username=request.data['username'], password=request.data['password'], email=request.data['email'])
        return Response({'status': 'success'}) 
class update(APIView):
    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        user.password = request.data['password']
        user.save()
        return Response({'status': 'success'})

    