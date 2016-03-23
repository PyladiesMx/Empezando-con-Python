import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Cargar los datos

titanic = pd.read_csv("titanic.csv")

#Plot

f = sns.FacetGrid(titanic, row= "Sex", col = "Pclass", margin_titles=True)

f.map(plt.hist, "Survived", color = "blue")

plt.show()

