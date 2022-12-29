import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    #Read csv and print the first 5 raw 
    dataset = pd.read_csv('salarios_32849f3e-7f53-4139-b334-b8de8beb144a.csv')
    print(dataset.head(5))

    #With this dataset we are going to train our model. 
    #This dataset have 30 examples and 2 columns
    print("\n The dataset have 30 examples and 2 columns: ",dataset.shape)

    #Start to load the data 
    x = dataset.iloc[:, :-1].values #iloc it's for search some data .value give us the value
    y = dataset.iloc[:, 1].values

    #Starting the use of train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)

    #data we are using to train our model
    print("Training data for x: \n",X_train)

if __name__ == '__main__':
    main()