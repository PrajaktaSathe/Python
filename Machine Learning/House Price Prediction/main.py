import joblib
import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')
model = joblib.load('models/LinearRegression.pkl')


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('base.html', context={"request": request})


@app.post("/predict")
async def predict(
    request: Request,
    income: int = Form(...),
    house: float = Form(...),
    rooms: int = Form(...),
    bedrooms: int = Form(...),
    population: int = Form(...)
):
    input_features = [income, house,
                      rooms, bedrooms, population]
    final_features = [np.array(input_features, dtype=np.float32)]
    output_value = model.predict(final_features)[0]
    prediction = round(output_value, 2)
    return templates.TemplateResponse(
        "base.html", context={"prediction": prediction, "request": request}
    )
