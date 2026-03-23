money = 20
age = 15
ticket_price = 12
age_restriction = 17

if money >= ticket_price:
    
    if age >= age_restriction:
        print("Je mag naar binnen.")
    else:
        print("Je hebt genoeg geld, maar je mag niet naar binnen.")

else:
    print("Je hebt niet genoeg geld.")