from django.contrib import admin 
from .models import Categories, Items, Orders, Payment, Profile, Reviews, Transactions, User

# Register your models here.
admin.site.register(Categories)
admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(Payment)
admin.site.register(Profile)
admin.site.register(Reviews)
admin.site.register(Transactions)
admin.site.register(User)