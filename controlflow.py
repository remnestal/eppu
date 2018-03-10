import sys

class Signals(object):
    """ Hub for control flow operations
        api:
            exit    handler for exiting the application
    """

    def __init__(self, app):
        self.app = app
        self.exit = _ExitHandler()

class _ExitHandler(object):
    """ Responds to exit-requests from the application
        api:
            graceful()  exit event is triggered directly by the user
            crash()     exit event is triggered indirectly by errors
    """

    def graceful(self, reason=None):
        """ exit gracefully
            exit beauty, exit grace; exit miss United States
        """
        self.__exit(status='OK', reason=reason)

    def crash(self, reason='you messed up'):
        """ crash to desktop """
        self.__exit(status='Error', reason=reason)

    def __exit(self, status, reason):
        """ exit the program """
        sys.exit('\n'.join([
            '[terminating] {status}'.format(status=status),
            '     [reason] {reason}'.format(reason=reason) if reason else '',
        ]).strip())
