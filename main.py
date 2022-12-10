from blockchain import Blockchain
from car_sharing import Owner, Car, Customer


def show_balance(customer, owner):
    print("Customer's Name: %s" % (customer.name,))
    print("Car Accessed by Customer: %s" % (owner.contract.booking_details.car.car_info,))
    print("Customer's Balance: %s" % (customer.balance))
    print("Owner's Balance: %s" % (owner.balance))

def show_rental_cost(cost):
    print("Rental cost: ", cost)


def start():
    blockchain = Blockchain()
    
    # Create a new Owner
    owner = Owner(1000)
    eth = 50

    # Create a smart contract for owner
    owner.deploy(eth, blockchain)

    ############# Owner adding information about the car #######################

    carName = input("Enter name of the car:\n")
    price = int(input("Enter price of car per day:\n"))
    owner.add_car_to_rent(price, carName)

   
    ############################################################################

    ############## Adding Customer Information ###################

    customerName = input("Enter Customer Name:\n")
    days= int(input("Enter number of days to rent:\n"))
    
    # Creating a new object for customer
    customer = Customer(1000,customerName)
      
    # Send request for Customer
    customer.request_book(eth, blockchain)
    customer.pass_number_of_days(days)

  
  # Store the details in blockchain
    owner.encrypt_and_store_details(blockchain)
    owner.allow_car_usage()
    
    # Customer access to car
    customer.access_car()
    customer.end_car_rental()

    # Updating balance of customer and owner 
    owner.withdraw_earnings()
    customer.retrieve_balance()

    show_rental_cost(price*days)
    show_balance(customer, owner)
    print("Thank you for choosing our service!!")


if __name__ == '__main__':
    start()
