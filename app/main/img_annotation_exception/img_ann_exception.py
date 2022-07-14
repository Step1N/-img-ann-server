
class ImgAnnServiceException(Exception):
    def __init__(self, message=None, base_exception=None):
        self.message = message
        self.base_exception = base_exception

    def __str__(self):
        if self.base_exception:
            return str(self.base_exception) + ":: " + self.message

        return "An unknown error occurred."


class ImgAnnAPIException(ImgAnnServiceException):
    def __init__(self, status=None, message=None, base_exception=None):
        self.status = status
        self.message = message

    def __str__(self):
        if self.message is None:
            return str(self.status)
        else:
            return "%s (%s)" % (self.status, self.message)
