def init_session(get_response):

    def middleware(request):
        if not hasattr(request.session, 'session_key') or request.session.session_key is None:
            request.session.create()

        return get_response(request)
    return middleware
