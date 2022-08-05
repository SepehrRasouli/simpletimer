from rich import print
from rich.panel import Panel
from datetime import datetime,timedelta
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
     def show(self,data):
        data = sorted(data,key=lambda x:list(x)[0])
        for entry in enumerate(data):
            print(
                Panel(
                    f"[bold green]{entry} Minutes",
                ),"\n"
            )

