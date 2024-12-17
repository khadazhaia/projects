## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

We might have missing values or values that state "No Signal" in the dataset due to issues during data collection such as poor internet connectivety or data never being recorded. The risk of filtering out these values could be loss of data.

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

In the context of heart rate, the standard deviation describes how much heart rate values can vary around the average heart rate over time. A high standard deviation means it far from the mean and theres a high or irregular heart rate, while a low standard deviation means the values are close to the mean and a stable heart rate.

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

From the graph labeled "averages.png," there are significant differences in values along the x-axis approximately at the following points:

10 to 12: There is a significant increase in values, from 55 to 90

25 to 30: The values significant decrease, dropping from the peak near 95 down to around 55

35 to 40: There is increase in values, from 50 to 80 and then drops back down to 50

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

There are corresponding differences in values in the "stdevs.png" graph and these differences do align with trends seen in the "averages.png" graph.

10 to 12: In the averages.png graph, there is a significant increase in values. In the stdevs.png graph, there is also an increase. 

25 to 30: In the averages.png graph, there is a significant decrease in values. In the stdevs.png graph, there is a significant decrease as well.

35 to 40: In the averages.png graph, there is a rise followed by a drop. In the stdevs.png graph, there is also a rise followed by a drop.
