""" Minimalistic timer app."""
import argparse as arg
from CONFIG import pickle_database_name
from database import DatabaseManager
from show import Show
parser = arg.ArgumentParser()
parser.add_argument(
    "-c","--create",help="""Creates a database.
    You can change the database name in CONFIG.py
    """,action="store_true"
)
parser.add_argument(
    "-a","--add",help="""Adds a new entry.
    Usage: interval. Should be in minutes.""",nargs=3
)
parser.add_argument(
    "-d","--delete",help="""Remove an entry.
    Usage: timer_number""",nargs=1
)
parser.add_argument(
    "-s","--show",help="""Shows timers.""",action="store_true"
)
args = parser.parse_args()
database_manager = DatabaseManager(pickle_database_name)
show = Show()
if args.create:
    database_manager.create_database()

if args.add:
    data = database_manager.read_data_from_database()
    data.add(args.add)
    database_manager.dump_data_to_database(data)

if args.delete:
    data = database_manager.read_data_from_database()
    data.remove(data.remove(list(a)[list(a).index(int(args.delete))]))
    database_manager.dump_data_to_database(data)

if args.show:
    data = database_manager.read_data_from_database()
    show = Show()
    show.show(data)
