import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Instantiate fastAPI with appropriate descriptors
app = FastAPI(
    title='FEC Data Visualization',
    description="For displaying data gathered from FEC's API",
    version="1.0",
    docs_url='/docs'
)

# Instantiate templates path
templates = Jinja2Templates(directory="src/viz/templates/")

# Mount static files
app.mount(
    '/assets', StaticFiles(directory='src/viz/templates/assets/'), name='assets')
app.mount(
    '/images', StaticFiles(directory='src/viz/templates/images/'), name='images')

# Define routes
@app.get('/', response_class=HTMLResponse)
def display_index(request: Request):
    """
    Displays the index page
    """
    return templates.TemplateResponse('index.html', {"request": request})

@app.get('/landing', response_class=HTMLResponse)
def display_landing(request: Request):
    """
    Displays the landing page
    """
    return templates.TemplateResponse('landing.html', {"request": request})

@app.get('/generic', response_class=HTMLResponse)
def display_generic(request: Request):
    """
    Displays the generic page
    """
    return templates.TemplateResponse('generic.html', {"request": request})

@app.get('/elements', response_class=HTMLResponse)
def display_elements(request: Request):
    """
    Displays the elements page
    """
    return templates.TemplateResponse('elements.html', {"request": request})

@app.get('/map', response_class=HTMLResponse)
def display_elements(request: Request):
    """
    Displays the map page
    """
    return templates.TemplateResponse('map.html', {"request": request})

@app.post('/generic')
def display_map_results(request: Request, location: str=Form(...), locality: str=Form(...), administrative_area_level_1: str=Form(...), postal_code: str=Form(...), country: str=Form(...)):
    """
    Displays the generic page with map results
    """
    
    return templates.TemplateResponse('generic.html', {"request": request, "location": location, "locality": locality, "state": administrative_area_level_1, "postal_code": postal_code, "country": country})



if __name__ == '__main__':
    uvicorn.run(app)
