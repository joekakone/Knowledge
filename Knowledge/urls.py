from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path#, include

from .views import index
from posts.views import blog, post, search, category, profile, create_post
from news.views import news
from forum.views import forum

from team.views import team, team_member
from users.views import login, register

from newsletter.views import newsletter
from contact.views import contact, contact_message

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='home'),

    ### Blog ###
    path('blog/', blog, name='blog'),
    path('blog/recherche/', search, name='search'),
    path('blog/article/<id>/', post, name='post-detail'),
    path('blog/creation/', create_post, name='create_post'),
    path('blog/categorie/<id>/', category, name='category-post'),
    path('blog/profil/<id>/', profile, name='author-profile'),
    #path('tinymce/', include('tinymce.urls')),

    ### Actualités ###
    path('actualites/', news, name='news'),
    #path('news/', news, name='news'),

    ### Forum ###
    path('forum/', forum, name='forum'),

    ### Forum ###
    path('contact/', contact, name='contact'),

    ### Équipe ###
    path('equipe/', team, name='team'),
    path('equipe/<id>/', team_member, name='team-member'),

    path('connexion/', login, name='login'),
    path('inscription/', register, name='register'),

    path('contact_message/', contact_message, name='contact_message'),
    path('newsletter/', newsletter, name='newsletter'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
