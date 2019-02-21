from django.conf.urls import url, include

from speed import views as v

# TODO: loop throuh views to make it compact?

urlpatterns = [url(v.PrepopulateGroupSView.url_pattern, v.PrepopulateGroupSView.as_view(),
                   name=v.PrepopulateGroupSView.url_name),
               url(v.GroupSCreate.url_pattern, v.GroupSCreate.as_view(),
                   name=v.GroupSCreate.url_name),
               url(v.PrepopulateRoundSView.url_pattern, v.PrepopulateRoundSView.as_view(),
                   name=v.PrepopulateRoundSView.url_name),
               ]
