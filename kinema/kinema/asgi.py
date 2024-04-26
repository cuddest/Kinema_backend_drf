from notifications import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo_project.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)
