from requests import get

loc = get('https://ipapi.co/json/') 
ip = loc.json() 
while (True) :
    choice = input("\nWhat do you want to display? \n"
                   "1. Public IP Address \n"
                   "2. Current Location \n"
                   "3. Capital of the Country \n"
                   "4. Country Population\n"
                   "5. Postal code\n"
                   "6. Latitude\n"
                   "7. Longitude\n"
                   "8. Timezone\n"
                   "9. Currency\n"
                   "10. Languages\n"
                   "11. Autonomous System Number\n"
                   "12. Internet Service Provider \n"
                   "13. Display all of the above\n"
                   )
    
    if choice == '1':
        print("Your public IP address is " + ip['ip'])
    elif choice == '2':
        print("Your Location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['region_code'] + ", " + ip['country_name']  + ", " + ip['country_code'])
    elif choice == '3':
        print("Your country's Capital is " + ip['country_capital'])
    elif choice == '4':
        print("Your country\'s Population is {}" .format(ip['country_population']))
    elif choice == '5':
        print("Your Postal/Zip code is "+ ip['postal'])
    elif choice == '6':
        print("Your Latitude is {}" .format(ip['latitude']))
    elif choice == '7':
        print("Your Longitude is {}" .format(ip['longitude']))
    elif choice == '8':
        print("Your country\'s Timezone is " + ip['timezone'])
    elif choice == '9':
        print('Your country\'s Currency is ' + ip['currency_name']  + ", " + ip['currency'])
    elif choice == '10':
        print('Your country\'s Languages is ' + ip['languages'])
    elif choice == '11':
        print("Your Autonomous System Number is " + ip['asn'])
    elif choice == '12':
        print("Your Internet Service Provider is " + ip['org'])
    elif choice =='13':
        print("Your public IP address is " + ip['ip'])
        print("Your Location is  " + ip['city'] + ", " + ip['region'] + ", " + ip['region_code'] + ", " + ip['country_name'] + ", " + ip['country_code'])
        print("Your country's Capital is " + ip['country_capital'])
        print("Your country\'s Population is {}" .format(ip['country_population']))
        print("Your Postal/Zip code is "+ ip['postal'])
        print("Your Latitude is {}" .format(ip['latitude']))
        print("Your Longitude is {}" .format(ip['longitude']))
        print("Your country\'s Timezone is " + ip['timezone'])
        print('Your country\'s Currency is ' + ip['currency_name']  + ", " + ip['currency'])
        print('Your country\'s Languages are ' + ip['languages'])
        print("Your Autonomous System Number is " + ip['asn'])        
        print("Your Internet Service Provider is " + ip['org'])

    end = input("\nDo you want to continue? (Y/N)")
    if (end.lower() == "n"):
        break
    else:
        continue