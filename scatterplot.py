import matplotlib .pyplot as plt
hours_studied=[1,2,3,4,5,6,7,8]
test_score=[100,300,200,400,800,600,500,700]

plt.figure(figsize=(8,6))
plt.scatter(hours_studied,test_score,color='black',marker='D')

plt.title('scatter plot for hours sudied vs test score')
plt.xlabel('hours studied')
plt.ylabel('test score')
plt.grid(True)
plt.show()

