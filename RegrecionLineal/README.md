# Regrecion Lineal y Regrecion Lineal Multiple

## Regrecion Lineal
Algoritmo de aprendizaje supervisado que nos indica la tendencia de un conjunto de datos continuos, modelando la relación entre una
variable dependiente Y una explicativa llamada X.

## Regrecion Lineal Multiple
Si nuestro problema tiene más de dos variables se le considera lineal múltiple

## ¿Que es prediccion de datos?
Algoritmos que se definen como "clasificados" que identifican a qué conjunto de categorías pertenecen los datos.
Podemos entrenar con datos historicos que entreguen resultados para ser aplicados al negocio

## Sobreajuste y Subajuste

### Sobreajuste
Es cuando nuestro modelo lo "obligamos" a ajustarse a los datos de entrada y salida.

### Subajuste
Es cuando el modelo fallará en el reconocimiento por falta de muestras suficientes. No generaliza el
conocimiento.

# Models we are using here

## train_test_split
Split arrays or matrices into random train and test subsets.

### División del conjunto de datos para entrenamiento y pruebas:
`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)`

`sklearn.model_selection.train_test_split`

**Parameters**

```
test_size: float or int, default=None
If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. If int, represents the absolute number of test samples. If None, the value is set to the complement of the train size. If train_size is also None, it will be set to 0.25.
```

```
random_state: int, RandomState instance or None, default=None
Controls the shuffling applied to the data before applying the split. Pass an int for reproducible output across multiple function calls
```
