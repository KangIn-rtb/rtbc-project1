# sklearn 제공 Regressior 성능 비교
# pipeline + GridSearchCV + 교차검증 + 성능비교

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score,mean_squared_error

data = load_diabetes()
x = data.data
y = data.target
print(x[:2])
print(y[:2])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
# pipeline + gridsearch 
models = {
    "LinearRegression":{
        "pipeline":Pipeline([
            ("scaler", StandardScaler()),
            ("model",LinearRegression())
        ]),
        "params":{
            "model__fit_intercept":[True, False]
        }
    },
    "RandomForest":{
        "pipeline":Pipeline([
            ("model",RandomForestRegressor(random_state=42))
        ]),
        "params":{
            "model__n_estimators":[100,200],
            "model__max_depth":[None,5,10],
            "model__min_samples_split":[2,5]
        }
    },
    "XGBoost":{
        "pipeline":Pipeline([
            ("model",XGBRegressor(random_state=42, verbosity=0))
        ]),
        "params":{
            "model__n_estimators":[100,200],
            "model__learning_rate":[0.01,0.05],
            "model__max_depth":[3,5]
        }
    },
    "SVR":{
        "pipeline":Pipeline([
            ("scaler", StandardScaler()),
            ("model",SVR())
        ]),
        "params":{
            "model__C":[0.1,1,10],
            "model__gamma":["scale","auto"],
            "model__kernel":["rbf"]
        }
    },
    "KNN":{
        "pipeline":Pipeline([
            ("scaler", StandardScaler()),
            ("model",KNeighborsRegressor())
        ]),
        "params":{
            "model__n_neighbors":[3,5,7],
            "model__weights":["uniform","distance"]
        }
    },
}

# GridSearchCV 실행
results = []
best_models = {}
# 각 모델을 순서대로 반복 처리 : best 모델 추출, 성능 저장
for name, config in models.items():
    print(f"{name} 튜닝중...")
    grid = GridSearchCV(
        config["pipeline"],
        config["params"],
        cv = 5,
        scoring = "r2",
        n_jobs=-1
    )
    grid.fit(x_train, y_train)
    
    best_model = grid.best_estimator_
    pred = best_model.predict(x_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)
    
    results.append([name, rmse, r2])
    best_models[name] = best_model
    print(grid.best_params_)
    print(r2)
    
df_results = pd.DataFrame(results,columns=["modelname","rmse","r2"])
df_results = df_results.sort_values("r2",ascending=False)
print(df_results)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.barplot(x="modelname",y="r2",data=df_results)
plt.xticks(rotation=30)
plt.subplot(1,2,2)
sns.barplot(x="modelname",y="rmse",data=df_results)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

best_modelname = df_results.iloc[0]["modelname"]
best_model = best_models[best_modelname]
pred = best_model.predict(x_test)

plt.figure(figsize=(6,6))
plt.scatter(y_test, pred)
plt.plot([y_test.min(), y_test.max()],[y_test.min(), y_test.max()], 'r--')
plt.title("최고 모델 {best_modelname}")
plt.xlabel("실제값")
plt.ylabel("예측값")
plt.show()
