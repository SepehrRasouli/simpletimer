from time import sleep
from datetime import datetime,timedelta
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel

console = Console()

def _calculate_start_end(time_to_spend:int):
    start = datetime.now()
    end = start + timedelta(seconds=time_to_spend)
    return start,end

def _show_tui(start,end,i,screen):
    """
    Shows TUI of timer app.
    Args:
        start,end: Datetime object
        i: int, current second.
        screen: rich screen object.
    """
    current = start + timedelta(seconds=i)
    text = Align.center(
    Text.from_markup(
        f"""[blink]
        Start: {start.hour}:{start.minute}:{start.second}\n 
        Current: {current.hour}:{current.minute}:{current.second}\n
        End: {end.hour}:{end.minute}:{end.second}[/blink]""",justify="center"
        ),vertical="middle"
    )
    screen.update(text)

def timer(remaining_time:int):
    """ Timer function."""
    remaining_time *= 60
    start,end = _calculate_start_end(remaining_time)
    with console.screen(style="bold #b2b2ff on #101010") as screen:
        for i in range(1,remaining_time+1):
            _show_tui(start,end,i,screen)
            sleep(1)
