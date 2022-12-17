import pandas as pd

def main():
#   simpler data structure with pandas
#   the follow structure it's similar to diccionary in python
#   this type of structure is called Series.
    structure = pd.Series([5, 10, 15, 20, 25])
    print("first data structure with function Series: \n", structure)
#   Print just one index
    print("Printing one index: \n",structure[3])

#   The following type of data is called Dataframe
    lst = ['Hello', 'universe']
#   After creating an array structure we will use a dataframe for printing
#   the structure as a dataframe or similar to a table
    df  = pd.DataFrame(lst)
    print("This is a example of dataframe: \n", df)

#   Second example
    data = {'Name' : ['Juan', 'Maria', 'Pedro'],
            'Age'  : [30, 40, 20],
            'Country' : ['Arg', 'US', 'MX']}
    print("Printing data without changing to dataframe: \n", data)
#   Using dataframe
    print("Printing data using dataframe: \n", pd.DataFrame(data))
    two_colums = pd.DataFrame(data)
    print("Printing just selected columms: \n", two_colums[['Name', 'Age']])

#   Taking a csv an print it
    csv = pd.read_csv("canciones-2018_b2c776e4-1cce-40eb-b3e7-591ea6d29f83.csv")
    print("Printing csv file: \n",csv)
#   printing a specific value of the csv
    print("printing a specific value of the csv:  \n",csv.name[5])
#   to check the type of data we are taking from the csv
    print("check the type of data we are taking from the csv: \n", csv.iloc[5])

if __name__ == '__main__':
    main()