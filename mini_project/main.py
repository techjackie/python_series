import sys
import book_tickets as bt

"""
--help
1. movie list
2. book movie_name
"""

arg1 = sys.argv[1] # [file_name, arg1, arg2]

if len(sys.argv) >= 3:
    arg2 = sys.argv[2]

if arg1 == "movie" and arg2 == "list":
    # Show Movie List
    bt.get_movie_list()

elif arg1 == "book":
    # Book Ticket for Specific Movie
    no_of_tickets = int(input("No of tickets: "))
    bk_name = input("Booking Name: ")
    bt.get_ticket(arg2, no_of_tickets, bk_name)

elif arg1 == "--help":
    # Show help menu
    print("-------------Help Menu---------------\nCommands:")
    print("1. movie list")
    print("2. book {movie_name}")
    print("----------------------------")
