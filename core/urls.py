from django.urls import path
from . import views

urlpatterns = [
    path('<slug>/', views.redirect_urls, name='redirect_urls'),  # redirect urls. slug = document.slug. Slug kabul ettiğini urls.py'de belirttik. (<>). Mesela /cv_en yazınca cv nin yüklü olduğu dosyaya gider.
]
