import json

from .models        import Order, Cart, PaymentOption, Card, Coupon, PackageType, BillingAddress, WishList
from products.models import Product
from user.models    import User

from django.views import View
from django.http  import HttpResponse,JsonResponse


class WishListCreateView(View):
#    @token_check_decorator
    def post(self, request):

        try:
            wishlist_data = json.loads(request.body)
            wishlist_user = User.objects.get(email = wishlist_data['email'])        # token_check_decorator가 완성되면, (email = request.user)
            new_item      = Product.objects.get(name = wishlist_data['product'])

            if Product.objects.filter(name = wishlist_data['product'], is_in_stock = True).exists():
                WishList.objects.create(product = new_item, user = wishlist_user, quantity = wishlist_data['quantity'])
                return JsonResponse({'message': 'SUCCESS'}, status=200)

            else:
                return JsonResponse({'message': 'OUT_OF_STOCK'}, status=200)

        except WishList.DoesNotExist:
            return JsonResponse({'message': 'INVALID_ACTION'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)

#   @token_check_decorator
    def get(self, request):
        signed_in_user = User.objects.get(id = 1)    # token_check_decorator가 완성되면 삭제할 코드
        saved_wishlist = WishList.objects.filter(user_id = signed_in_user)  # token_check_decorator가 완성되면, (user_id = request.user)

        saved_items = []

        [saved_items.append({'name' : item.product.name, 'price' : item.product.price, 'thumbnail_url' : item.product.thumbnail_url, 'quantity' : item.quantity})
         for item in saved_wishlist]

        return JsonResponse({'wishlist': saved_items}, status=200)

#   @token_check_decorator
    def delete(self,request):
        data = json.loads(request.body)

        if WishList.objects.filter(id=data['id']).exists():
            WishList.objects.get(id=data['id']).delete()

            return JsonResponse({"message": "SUCCESS"}, status=200)

        else:
            return JsonResponse({"message": "INVALID_INPUT"}, status=200)
