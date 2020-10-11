#print(1729)
'''
What is kNN?

k-Nearest Neighbors is one of the easiest Machine Learning algorithms. It is a “Classification” algorithm to be specific. But due to its generic procedure, it can be also used for feature selection, outlier detection(Wilson editing), and missing value imputations. It is also called Instance-Based Learning and Lazy Learning because at training time it does nothing! In the kNN, the hyper-parameter is “k”.

Working of kNN

kNN has a simple working mechanism. I will explain it in 4 steps. When a test point comes in, this is what we do in kNN,
Fix the value of k
Find k nearest neighbors by Euclidean distance formula( or any distance finding algorithm )
Vote the class labels
Prediction
Let me illustrate kNN with a simple example. Let us assume that our data set has 3 class labels( A, B, C). Let us fix the value of k as 3 i.e we find 3 nearest neighbors. Now when a test point comes in, we find the 3 nearest neighbors in our data set. Let us assume that our algorithm gave us the 3 nearest neighbors as A, A, C. Since, the test point must belong to only one class, we have to select only one out of A, A, C. We introduce a voting mechanism now since A’s are 2 and C’s are 1. “A” wins the game and we assign the test point belongs to the class label “A”. It is as simple as that!
Now, let us look at the detailed explanation with code.
Explanation of kNN Algorithm
0. Import the required libraries
'''

