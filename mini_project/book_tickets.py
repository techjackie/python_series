import os
import pickle

inital_movie_list = [
    {"movie_name":"aavesham","available_tickets":100, "total_tickets":150, "cost_per_ticket":130},
    {"movie_name":"star","available_tickets":110, "total_tickets":150, "cost_per_ticket":120},
    {"movie_name":"maharaja","available_tickets":105, "total_tickets":150, "cost_per_ticket":120},
    {"movie_name":"garudan","available_tickets":90, "total_tickets":150, "cost_per_ticket":140}
    ]

"""
1. checking (database) file is exists or not
2. if not exists do the following,
    * file content --> movie list
"""

if not os.path.isfile('database'):
    with open('database','wb') as file:
        pickle.dump(inital_movie_list, file)


with open('database','rb') as file:
    movies = pickle.load(file)
 


def get_movie_list():

    print("---------Movie List ---------")
    for ele in movies:
        print(f"Movie Name: {ele['movie_name']}")
        print(f"Available Tickets: {ele['available_tickets']}")
        print(f"Cost Per Ticket: {ele['cost_per_ticket']}\n")

    print("------------------")


def get_ticket(movie, no_of_tickets, bk_name):
    """
    1. movie name validation
    2. checking no_of_tickets <= available_tickets
    3. Estimation Cost 
    4. Printing Receipt
    """


    for ele in movies:
        if movie == ele['movie_name']:
            if no_of_tickets <= ele['available_tickets']:
                total_cost = no_of_tickets * ele['cost_per_ticket']

                print('Before Updation Available_Tickets: ',ele['available_tickets'])
                # Movie List Updation
                ele["available_tickets"] = ele['available_tickets'] - no_of_tickets

                print('After Updation Available_Tickets: ',ele['available_tickets'])

                print("---------Receipt-----------")
                print(f"Booking Name: {bk_name}")
                print(f"Total Ticket Cost: {total_cost}")
                print("---------------------")

                # saving changes
                with open('database','wb') as file:
                    pickle.dump(movies, file)

            else:
                print(f"Ticket Limit Exceeded! Only We have {ele['available_tickets']} tickets")
            return

    print('Invalid Movie Name :(')

    