import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "facess.settings")

application = get_asgi_application()

# Quando habilitar Channels:
# from channels.routing import ProtocolTypeRouter, URLRouter
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # "websocket": AuthMiddlewareStack(URLRouter([...]))
# })
