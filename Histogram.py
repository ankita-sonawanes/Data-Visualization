import matplotlib.pyplot as plt
import numpy as np
data=np.random.randn(1000)
plt.hist(data,bins=10,color="skyblue",edgecolor="blue")
plt.xlabel('values')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()