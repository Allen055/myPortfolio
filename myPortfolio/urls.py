"""
URL configuration for personalWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sitemaps
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from accounts import urls as accounts_urls
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView


sitemaps_dict = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("about/", include("about.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("skills/", include("skills.urls")),
    path("education/", include("education.urls")),
    path("blog/", include("blog.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("experience/", include("experience.urls")),
    path( "accounts/",include((accounts_urls, "accounts"),namespace="accounts")),
    path("contact/", include("contact.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='django.contrib.sitemaps.views.sitemap'), 

    path("robots.txt", TemplateView.as_view( template_name="robots.txt", content_type="text/plain"),),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


