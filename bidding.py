# to run this program you need to enable emulate in pycharm
# ---------------------------------------------------------
# Emulating a Terminal in Run Configurations:
#
# For running scripts and seeing output directly in PyCharm's console.
# Access the "Run/Debug Configurations" window (usually under "Run" in the menu bar).
# Find your specific run configuration.
# Check the "Emulate terminal in output console" option.

import os


def find_winner(bid_data):
    os.system('cls' if os.name == 'nt' else 'clear')
    highest_bid = 0
    winner = ""
    for bidder in bid_data:
        bidding_price = bid_data[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"list of bidders participated: {bid_data}")
    print(f"the winner is {winner} with a bid price of {highest_bid}")


bid_pool = {}
more_bids = 'yes'
while more_bids == 'yes':
    party_name = input("Hi, what is bidder name?: ")
    bid_amount = int(input("enter your bid amount:"))
    bid_pool[party_name] = bid_amount
    more_bids = input("are more bidders there? type 'yes' or 'no'").lower()
    if more_bids != 'yes':
        find_winner(bid_pool)
    elif more_bids == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
