import numpy as np
#Using numpy because it's a powerfull library for ML and excelent for array management
#It's useful for using less code avoiding using loops as for and foreach

def main ():
    print ("using numpy for generate some manual arrays")
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a)
    b = np.array([10, 30 , 20, 60, 50, 40])
    print (b[3:])
    print (b[1::3])

#    automatic arrays
    print ("generating some automatic arrays: ")
    auto_array_zero = np.zeros(10)
    print (auto_array_zero)

#    To know the kind of array we have we can use type
    print("checking the type of the array: ")
    type_of_array = type(auto_array_zero)
    print(type_of_array)

#   Another function to keep in mind to generate data linspace
#   the first 2 numbers are the interval and the last one will be number of elements
    print("generating some data with linspace: ")
    generate_some_data = np.linspace(1, 10, 5) 
    print(generate_some_data)

#   generate and array of two dimensions
    print("generating arrays of two dimensions")
    array_two_dim = np.array([['x','y','z'], ['a','c','e']])
    print ("Array of two dimensions: ", array_two_dim)
    print ("type of the array: ", type(array_two_dim))
    print ("number of dimensions of this array: ", array_two_dim.ndim)

#   sorting numbers with numpy
    print("array b: ",b)
    print("sorting numbers from small values to high from array b: ", np.sort(b))

#   making more complex array and sort it
    header = [('name', 'S10'), ('age',int)]
    data = [('caro', 27), ('hector', 28), ('pepi', 5)]
    users = np.array(data, dtype = header)

    print ("users: ", users)

#   sorting users
#   to sort by age
    print("sorting by age: ", np.sort(users, order = 'age'))

#   using arange for filling arrays
    print("array automatic with 25 numbers function arange: ",np.arange(25))

#   make bidimentional array automatic
    print ("bidimentional array: ", np.full((3,5), 10))


if __name__ == '__main__':
    main()