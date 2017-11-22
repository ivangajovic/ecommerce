from django.conf.urls import url
from shopping import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^update_item/$', views.update_item_quantity, name='update_item_quantity'),
    url(r'^thankyou/$', views.thank_you, name='thank_you'),
    url(r'^confirm_order/$', views.confirm_order, name='confirm_order'),
    url(r'^remove_item/$', views.remove_item, name='remove_item'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^credit_card_page/$', views.credit_card_page, name='credit_card'),
    url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
]
