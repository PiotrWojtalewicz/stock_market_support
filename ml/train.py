from sklearn.metrics import accuracy_score, classification_report
from ml.models import get_random_forest,get_linear_regression
import numpy as np

def train_model_random_forest(X_train,y_train,X_test,y_test):
    #najpierw tworze model
    model_random_forest = get_random_forest()
    #Potem trenuje model
    model_random_forest.fit(X_train,y_train)
    # Potem robię predykcje na danych testowych 
    y_prob = model_random_forest.predict_proba(X_test)[:,1]

    y_pred = (y_prob > 0.3).astype(int)
   # y_pred =model.predict(X_test)
   #test progów
    for t in [0.3,0.4,0.5]:
        y_prob = (y_prob>t).astype(int)
        print(f"\nTreshold: {t}")
        print(classification_report(y_test,y_pred))


    
    #Oceniam model 
    acc = accuracy_score(y_test, y_pred)
    print(f"Dokładność modelu: {acc:.2f}")
    print("Raport klasyfikacji:")
    print(classification_report(y_test,y_pred))
    print("Min:", y_prob.min())
    print("Max:", y_prob.max())
    print("Unique sample:", np.unique(y_prob[:50]))
    print(y_train.value_counts())
    print(X_train.describe())   
    return model_random_forest

def train_model_linear_regression(X_train, y_train, X_test):
    model_linear_regression = get_linear_regression()
    model_linear_regression.fit(X_train, y_train)
    y_prob = model_linear_regression.predict_proba(X_test)[:,1]
    print(np.unique(y_prob[:20]))
    return 