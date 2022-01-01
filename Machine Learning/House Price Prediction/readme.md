## House Price Predictor App
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![html](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![css3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![python](https://img.shields.io/badge/Python-0078D4?logo=python&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit_learn-0078D4?logo=scikit-learn&logoColor=white)
![fastapi](https://img.shields.io/badge/fastapi-109989?logo=FASTAPI&logoColor=white)
![jupyterlab](https://img.shields.io/badge/Jupyter_lab-F37626.svg?logo=Jupyter&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

House Price Predictor App used to predict the price of the house based on certain input parameters created using python's scikit-learn, fastapi, numpy and joblib packages.

### Dataset Description :-

A real estate agent gives you some information about a bunch of houses in regions of the United States.This data has taken from USA site, and this data is already preproccessed.

The data contains the following columns:

| Feature Name                 | Feature Description                                       |
|------------------------------|-----------------------------------------------------------|
| Avg. Area Income             | Avg. Income of residents of the city house is located in. |
| Avg. Area House Age          | Avg Age of Houses in same city                            |
| Avg. Area Number of Rooms    | Avg Number of Rooms for Houses in same city               |
| Avg. Area Number of Bedrooms | Avg Number of Bedrooms for Houses in same city            |
| Area Population              | Population of city house is located in                    |
| Price                        | Price that the house sold at                              |
| Address                      | Address for the house                                     |

### Installation :- 
Open Anaconda prompt and create new environment 👇
```
conda create -n your_env_name python = (any_version_number)
```
Then Activate the newly created environment 👇
```
conda activate your_env_name
```
To install all requirement packages for the app 👇
```
pip install -r requirements.txt
```
Then, Run the app 👇
```
uvicorn main:app --reload
```

### Demo GIF Image 👇:- 
![output_image](https://github.com/PrakashAnalyst/Python/blob/main/Machine%20Learning/House%20Price%20Prediction/static/images/demo.gif)
