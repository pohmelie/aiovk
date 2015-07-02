
class VkError(Exception):
    pass


class VkAuthorizationError(VkError):
    pass


class VkAPIMethodError(VkError):
    __slots__ = ['error', 'code', 'message', 'request_params', 'redirect_uri']

    def __init__(self, error):
        super(VkAPIMethodError, self).__init__()
        self.error = error
        self.code = error.get('error_code')
        self.message = error.get('error_msg')
        self.request_params = error.get('request_params')
        self.redirect_uri = error.get('redirect_uri')

    def __str__(self):
        error_message = '{self.code}. {self.message}. request_params = {self.request_params}'.format(self=self)
        if self.redirect_uri:
            error_message += ',\nredirect_uri = "{self.redirect_uri}"'.format(self=self)
        return error_message