import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("result.csv")

df.plot(kind='scatter',x='x',y='y')

plt.xlabel(r"$\beta d [rad]$")
plt.ylabel("Frequency [GHz]")

plt.show()