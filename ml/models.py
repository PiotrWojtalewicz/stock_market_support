from sklearn.ensemble import RandomForestClassifier

def get_random_forest ():
    "Buduję model random forest do klasyfikacji ruchu ceny"
    model = RandomForestClassifier (
        n_estimators= 100,
        random_state=42,
        class_weight= 'balanced'
    )
    return model
