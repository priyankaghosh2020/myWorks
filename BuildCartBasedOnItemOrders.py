import json
from collections import deque
import threading
import time
import math
import pandas as pd
from matplotlib import pyplot as plt

######
NumberOfParallel = 10
######

itemTxtFile = "/Users/prosenjitdas/Desktop/orderdata/items.json"
orderTxtFile = "/Users/prosenjitdas/Desktop/orderdata/orders.json"
itemsFromMenu = {}
cartFromOrder = []
dataframe = None

# Persist Data for Transformation the Existing CART
class Cart() :

    def __init__(self, order , seq ) :
        self.name = order['name']
        self.service = order['service']
        self.orderId = math.ceil(time.time() * 1000) + seq
        self.tasks = deque()
        self.totalCost = 0
        self.totalWaitTime = 0
        # Loop through Each Items
        for item in order['items'] :
            processTime = itemsFromMenu[item['name']]
            self.totalCost += item['price_per_unit'] * item['quantity']
            self.totalWaitTime += int(processTime * item['quantity'] / NumberOfParallel)
            # Based on Quatity again split Orders in mutiple Pieces
            for _ in range(item['quantity']) :
                self.tasks.append(str(self.orderId) + '->>' + str(seq) + ">>" + item['name'] + '/' + str(item['quantity']) + ' :'+ str(processTime) + '/' + self.service)


# Get items
def getItems () :
    # Build Item as constant
    with open(itemTxtFile,'r') as json_file:
        data = json.load(json_file)
        for p in data :
            itemsFromMenu.update([(p['name'] , p['cook_time'])])
    return itemsFromMenu

# Get Order in Stream
def getOrders () :
    # Get Json in Chunk
    fileQueue = [deque()] * NumberOfParallel
    with open(orderTxtFile,'r') as json_file:
        data = json.load(json_file)
        count = 1
        for p in data :
            cart = Cart(p , count)

            # Display Order Details
            print(cart.orderId, " / ", cart.name , " / ", cart.service ," --> Total Cost : " , cart.totalCost , ", Total WaitTime :", cart.totalWaitTime)
            count += 1
            ind = 0
            while cart.tasks :
                # Popup Task one by One and Add in Queue
                fileQueue[ind].append(cart.tasks.popleft())
                ind += 1
                if ind >= NumberOfParallel :
                    ind = 0
            # End of While

            # Prepare Cart Data for Persist
            cartFromOrder.append([cart.orderId ,cart.name ,  cart.service, cart.totalCost , cart.totalWaitTime])
            # For Testing
            if count > 50 :
                break


        dataframe = pd.DataFrame(cartFromOrder,columns=['OrderId','Name' , 'Service' , 'TotalCost' , 'Total Wait-Time'])

    return fileQueue , dataframe

# Thread Function
def processAllDataFromQueue(cartInQueue , indx):
    # Get the orders from Queue and execute
    while cartInQueue :
        p = cartInQueue.popleft()
        # Execute the Order
        print(indx , '--> CART: ' , p)
        time.sleep(1)


# Get Data on Buffer
itemsFromMenu = getItems ()  # constant
queue , dataframe = getOrders ()

# Process Streaming and collect Threads
processes = []
for indx in range(NumberOfParallel) :
    processes.append(threading.Thread(target=processAllDataFromQueue, args=(queue[indx],indx)))

# Start All Threads
for proc in processes:
    proc.start()

# wait until threads are completely executed
for proc in processes:
    proc.join()


dataframe.plot(kind='scatter',x='TotalCost',y='Total Wait-Time',color='red')
dataframe.plot(kind='bar',x='Service',y='TotalCost')
plt.show()

dataframe.groupby('Service')['TotalCost'].sum().plot(kind='bar') #,x='Service',y='TotalCost')
plt.show()

