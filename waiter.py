import chime
import random
from time import sleep
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel


console = Console()
chime.theme(random.choice(chime.themes()))
def waiter():
    with console.screen(style="bold white on red") as screen:
        try:
            while True:
                 text = Align.center(
                     Text.from_markup(
                             f"""[blink]Timer's Up ![/blink]""",justify="center"
                     ),vertical="middle"
                 )
                 screen.update(text)
                 chime.success()
                 sleep(1)
        except KeyboardInterrupt:
            quit()


