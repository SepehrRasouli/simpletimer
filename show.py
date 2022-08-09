from rich.console import Console
from simple_term_menu import TerminalMenu
from datetime import datetime,timedelta
console = Console()
class Show:
    @staticmethod
    def _error_handler(func):
        def handler(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                raise e
        return handler

    @_error_handler
    def show_menu(self,data):
        """ Shows a menu of timers."""
        with console.screen():
            timers = sorted([[index,timer] for index,timer in enumerate(data)],key=lambda x:x[1])
            options = [f"Timer: {timer[1]} Minutes" for timer in timers]
            term_menu = TerminalMenu(options)
            selected = term_menu.show()
            return timers[selected][1]


