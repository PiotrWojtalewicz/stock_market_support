from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def get_random_forest ():
    "Buduję model random forest do klasyfikacji ruchu ceny"
    model_random_forest = RandomForestClassifier (
        n_estimators= 300,
        max_depth=5,
        min_samples_leaf=10,
        random_state=42,
        class_weight= 'balanced'
    )
    return model_random_forest

def get_linear_regression ():
    "model Linear Regression dla ruchu cen"
    model_linear_regression =LogisticRegression(max_iter=1000)
    return model_linear_regression

