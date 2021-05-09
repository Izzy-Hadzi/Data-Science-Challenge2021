# running with anaconda3/bin.python3
import pandas
import seaborn

#helper methods
#method to find traditional average
def average(array):
    return array['order_amount'].mean()

#method for adjusted average with outliers
def adjusted_average(data):
    #printing shape of the data (number of rows, number of columns)
    print("Original data shape:")
    print(data.shape)
    #finding the different quartiles to observe any outliers
    seaborn.boxplot(data=data, x=data['order_amount'])
    Q1 = data['order_amount'].quantile(0.25)
    Q3 = data['order_amount'].quantile(0.75)
    IQR = Q3-Q1
    print("Q1:")
    print(Q1)
    print("Q2:")
    print(Q3)
    print("IQR:")
    print(IQR)
    Lower_Whisker = Q1 - 1.5*IQR
    Upper_Whisker = Q3 + 1.5*IQR
    print("Lower whisker and Upper whisker:")
    print(Lower_Whisker, Upper_Whisker)
    #removing outliers that were found 
    outliers = data[data['order_amount']>Upper_Whisker]
    data = data[data['order_amount'] < Upper_Whisker]
    #for testing purposes printing the outliers
    #print(outliers) 
    #printing shape again (number of rows, number of columns)
    print("New data shape:")
    print(data.shape)
    #finding the mean without outliers
    print("New mean:")
    print(data['order_amount'].mean())


#importing data, without the method of payment and date
#1st column is order_id, 2nd is shop_id, 3rd is	user_id, 4th is	order_amount, 5th is total_items
data = pandas.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.tsv", dtype = int, sep = "\t", skiprows=0, usecols=[0,1,2,3,4])
#print(data)
print("Naive average: " )
print(average(data))
adjusted_average(data)


