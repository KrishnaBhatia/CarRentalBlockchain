from blockchain import Blockchain
from car_sharing import Owner, Car, Customer


def show_balance(cust_balance, owner_balance):
    print("Customer's balance: %s" % (cust_balance,))
    print("Owner's balance: %s" % (owner_balance,))

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start():
    blockchain = Blockchain()
    #customer = Customer(1000)
    owner = Owner(1000)
    eth = 50

    #show_balance(customer.balance, owner.balance)

    #1
    owner.deploy(eth, blockchain)

    #2
    #customer.request_book(eth, blockchain)

    #3
    #car = "Porsche"
    
    
    ############# Owner adding information about the car #######################

    car1 = input("Enter name of the car:\n")
    #daily_price = 200
    price = int(input("Enter price of car per day:\n"))
    #owner.add_car_to_rent(daily_price, car)
    owner.add_car_to_rent(price, car1)

    ############################################################################

    ############## Adding Customer Information ###################

    # Dictionary for storing customer info
    customerDict = {}
    mess = input("Do you want to continue Y or N?")

    while(mess == "Y"):
        customerName = input("Enter Customer ID:\n")
        days= int(input("Enter number of days to rent:\n"))

        # If new customer, then add to database
        if customerName not in customerDict.keys():
            customer = Customer(1000)
            customerDict[customerName] = customer
        
        # Send request for specific Customer
        customerDict[customerName].request_book(eth, blockchain)
        customerDict[customerName].pass_number_of_days(days)

    ##############################################################
    #customer.pass_number_of_days(days_no)
    #customer.pass_number_of_days(days)

    #4
        owner.encrypt_and_store_details(blockchain)
        owner.allow_car_usage()

        #5
        customer.access_car()

        #6
        customer.end_car_rental()

        #7
        owner.withdraw_earnings()
        customer.retrieve_balance()

        show_rental_cost(price*days)
        show_balance(customer.balance, owner.balance)
    
    print("Thank you for choosing our service!!")


if __name__ == '__main__':
    start()
