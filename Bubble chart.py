import matplotlib .pyplot as plt
hours_studied=[1,2,3,4,5,6,7,8]
test_score=[50,55,60,65,70,75,80,85]
bubble_sizes=[100,200,300,400,500,600,700,800]

plt.figure(figsize=(8,6))
plt.scatter(hours_studied,test_score,bubble_sizes,alpha=0.7,color='black',edgecolors='w')

plt.title('bubble chart for hours sudied vs test score')
plt.xlabel('hours studied')
plt.ylabel('test score')
plt.grid(True)
plt.show()

