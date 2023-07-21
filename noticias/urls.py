from django.conf.urls.static import static
from mysite import settings

urlpatterns = [
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)