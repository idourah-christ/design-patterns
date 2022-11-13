from handlers import Handler

def search(handler:Handler, request):
    return handler.execute(request)