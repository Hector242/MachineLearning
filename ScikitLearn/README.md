# Scikit Learn

## Definition
´Scikit-learn´ is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection, model evaluation, and many other utilities.

## Uses
1. Simple and efficient tools for predictive data analysis
2. Accessible to everybody, and reusable in various contexts
3. Built on NumPy, SciPy, and matplotlib
4. Open source, commercially usable - BSD license

On this library you can import the models you want to use with

´from sklearn import MODEL-NAME´

example

´from sklearn import tree´

### División del conjunto de datos para entrenamiento y pruebas:
´ X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)´

### Entrenar modelo:
´[modelo].fit(X_train, y_train)´

### Predicción del modelo:
´Y_pred = [modelo].predict(X_test)´

### Matriz de confusión:
´metrics.confusion_matrix(y_test, y_pred)´

### Calcular la exactitud:
´metrics.accuracy_score(y_test, y_pred)´
