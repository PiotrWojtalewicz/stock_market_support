from sklearn.metrics import accuracy_score, classification_report
from ml.models import get_random_forest

def train_model(X_train,y_train,X_test,y_test):
    #najpierw tworze model
    model = get_random_forest()
    #Potem trenuje model
    model.fit(X_train,y_train)
    # Potem robię predykcje na danych testowych 
    y_pred =model.predict(X_test)
    #Oceniam model 
    acc = accuracy_score(y_test, y_pred)
    print(f"Dokładność modelu: {acc:.2f}")
    print("Raport klasyfikacji:")
    print(classification_report(y_test,y_pred))
    
    return model