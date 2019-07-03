list_of_items=[]
item_name=""
while item_name!="done":    #while True:   this is another method to do

    item_name=input("item (enter \"done\" when finished):")
    if item_name="done"
        break
    price= float(input("price:"))
    quantity=float(input("quantity: "))

    item={
        "name": item_name,
        "price": price,
        "quantity": quantity
    }
    
    list_of_items.append(item)
print("------------------------------------")
print("Receipt")
print("------------------------------------")
total=0
for item in list_of_items:
    print("%s %s %sKD"%(item["quantity"],item["name"],(item["quantity"]*item["price"])))
    total=total+item["quantity"]+item["price"]
print("--------------------------------")
print("Total: %s KD"% total)