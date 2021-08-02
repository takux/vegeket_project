from django.shortcuts import redirect
from django.views.generic import View, TemplateView
from django.conf import settings
from base.models import Item
import stripe
from django.contrib.auth.mixins import LoginRequiredMixin

stripe.api_key = settings.STRIPE_API_SECRET_KEY

tax_rate = stripe.TaxRate.create(
    display_name="消費税",
    description="消費税",
    country="JP",
    jurisdiction="JP",  # 管轄を指定
    percentage=settings.TAX_RATE * 100,  # 10%
    inclusive=False,  # 外税を指定（内税の場合はTrue）
)


class PaySuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/success.html'

    def get(self, request, *args, **kwargs):
        # 最新のOrderオブジェクトを取得し、注文確定に変更

        # カート情報削除
        del request.session['cart']

        return super().get(request, *args, **kwargs)


class PayCancelView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/cancel.html'

    def get(self, request, *args, **kwargs):
        # 最新のOrderオブジェクトを取得

        # 在庫数と販売数を元の状態に戻す

        # is_confirmedがFalseであれば削除（仮オーダー削除）

        return super().get(request, *args, **kwargs)


def create_line_item(unit_amount, name, quantity):
    return {
        'price_data': {
            'currency': 'jpy',
            'unit_amount': unit_amount,
            'product_data': {'name': name, },
        },
        'quantity': quantity,
        "tax_rates": [tax_rate.id],
    }


def check_profile_filled(profile):
    if profile.name is None or profile.name == '':
        return False
    elif profile.zipcode is None or profile.zipcode == '':
        return False
    elif profile.prefecture is None or profile.prefecture == '':
        return False
    elif profile.city is None or profile.city == '':
        return False
    elif profile.address1 is None or profile.address1 == '':
        return False
    return True


class PayWithStripe(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        # プロフィールが埋まっているかチェック
        if not check_profile_filled(request.user.profile):
            return redirect('/profile/')

        cart = request.session.get('cart', None)
        if cart is None or len(cart) == 0:
            return redirect('/')

        line_items = []
        for item_pk, quantity in cart['items'].items():
            item = Item.objects.get(pk=item_pk)
            line_item = create_line_item(
                item.price, item.name, quantity)
            line_items.append(line_item)

        checkout_session = stripe.checkout.Session.create(
            customer_email=request.user.email,  # ログインしている現ユーザーのemailを渡す
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=f'{settings.MY_URL}/pay/success/',
            cancel_url=f'{settings.MY_URL}/pay/cancel/',
        )
        return redirect(checkout_session.url)
