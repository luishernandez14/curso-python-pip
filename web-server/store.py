import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #Getting all info
    print(r.status_code) #That info has an status
    #print(r.text) #What info is giving us that API
    #print(type(r.text)) #We have an string (It has written on it a list of dictionaries)
    categories = r.json() #Asking for json format gives us the info on a python format

    for category in categories:
        print(category['name'])

   