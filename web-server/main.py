import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #Creating an instance of an application

@app.get('/') #Decorator syntax: Specifying route for getting in 
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse) #Adding another route
def get_list():
    return """
        <h1>Hola soy una página</h1>
        <p>soy un parrafo</p>

    """  


def run():
    store.get_categories()

if __name__ == '__main__':
    run()
