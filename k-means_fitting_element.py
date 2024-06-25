from sklearn.neighbors import NearestNeighbors
import numpy as np

# Define the existing elements
elements = [
    {"length":40,"popularity":10,"age":10},
    {"length":41,"popularity":5,"age":9},
    {"length":52,"popularity":10,"age":10},
    {"length":49,"popularity":10,"age":0},
    {"length":50,"popularity":0,"age":3},
    {"length":51,"popularity":10,"age":0},
    {"length":45,"popularity":10,"age":4},
    {"length":38,"popularity":9,"age":1},
    {"length":44,"popularity":10,"age":0},
    {"length":41,"popularity":3,"age":2}
]

# Convert the elements to a 2D array
X = np.array([[e["length"], e["popularity"], e["age"]] for e in elements])
# Create a nearest neighbors model
model = NearestNeighbors(n_neighbors=1)
model.fit(X)
# Define the new element
new_element = np.array([[42, 7, 0]])
# Find the index of the most similar element
dist, ind = model.kneighbors(new_element)
print(f"The most similar element to the new element is: {elements[ind[0][0]]}")
