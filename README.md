# Description

Finding the best point in multidimentional space for a new point. <br>
Metrics which is used is K-means. <br>
Ideally addresses in multidimentional space should be normalized. <br>

```
# Function to normalize a list of dictionaries
def normalize_elements(elements):
    # Initialize min and max dictionaries
    min_values = {key: float('inf') for key in elements[0]}
    max_values = {key: float('-inf') for key in elements[0]}
    
    # Find min and max values for each attribute
    for element in elements:
        for key in element:
            min_values[key] = min(min_values[key], element[key])
            max_values[key] = max(max_values[key], element[key])
    
    # Normalize elements
    normalized_elements = []
    for element in elements:
        normalized_element = {}
        for key in element:
            # Min-max normalization
            normalized_element[key] = (element[key] - min_values[key]) / (max_values[key] - min_values[key])
        normalized_elements.append(normalized_element)
    
    return normalized_elements

# Normalize the elements
normalized_elements = normalize_elements(elements)

# Print the normalized elements
for element in normalized_elements:
    print(element)
```
