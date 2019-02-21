from django.conf.urls import url, include

from lot import views as v

# TODO: loop throuh views to make it compact?

urlpatterns = [url(v.LotteryCreate.url_pattern, v.LotteryCreate.as_view(),
                   name=v.LotteryCreate.url_name), ]
