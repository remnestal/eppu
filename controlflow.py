import sys

class Signals(object):

    def __init__(self, app):
        self.app = app

    def quit(self, status='OK', ):
        """ quits
            no bullshit, just quit the program already
        """
        sys.exit('[terminating] {status}'.format(status=status))
