from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

# This root routing configuration specifies that when a connection is made to
# the Channels development server, the ProtocolTypeRouter will first inspect the
# type of connection. If it is a WebSocket connection (ws:// or wss://),
# the connection will be given to the AuthMiddlewareStack.

channel_route = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
