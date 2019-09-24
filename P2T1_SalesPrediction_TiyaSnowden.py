# In this project we are using print and input functions to get sale predictions. 
# September 16, 2019
# CTI-110 P2T1- Sales Prediction
# Tiya Snowden
 
# Get the prjected total sales.
total_sales = float(input('enter the projected sales: '))
 
# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23
 
# Display the profit.
print('The profit is $', format (profit, ',.2f'))
