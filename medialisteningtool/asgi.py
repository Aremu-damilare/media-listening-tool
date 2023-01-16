"""
ASGI config for web project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.conf import settings
# from dotenv import load_dotenv
from medialisteningtool.middleware import AsyncMiddlewareWrapper

# load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "medialisteningtool.settings")

application = get_asgi_application()
# application = AsyncMiddlewareWrapper()(application)

# import os

# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import products.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medialisteningtool.settings')

# # application = get_asgi_application()
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             products.routing.websocket_urlpatterns
#         )
#     ),
# })