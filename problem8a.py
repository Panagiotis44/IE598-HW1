# Define a list of lists with more data
data = [
    [3, 6, 2],
    [7, 1, 4],
    [5, 9, 8],
    [12, 8, 3],
    [6, 15, 7],
    [9, 4, 10],
    [2, 11, 6]
]

# Print the original data
print("Original data:")
for row in data:
    print(row)

# Number of bundles
num_bundles = 3

# Initialize a list to store top elements from each bundle
top_elements = []

# Initialize a list to store lists acquired by each bundle
bundle_lists = [[] for _ in range(num_bundles)]

# Loop until all elements are allocated
while data:
    # Loop through each bundle
    for i in range(num_bundles):
        # If data is empty, break out of the loop
        if not data:
            break
        
        # Sort the data based on the i-th element of each inner list in reverse order
        data.sort(key=lambda x: x[i], reverse=True)
        
        # Select the top element from the sorted list, remove it, and append it to the top_elements list
        top_element = data.pop(0)
        top_elements.append(top_element)
        
        # Add the list that acquired the bundle to the bundle_lists list
        bundle_lists[i].append(top_element)

        
# Print the lists acquired by each bundle separately
for i, bundle_list in enumerate(bundle_lists):
    print(f"\nLists acquired by bundle {i+1}:")
    for acquired_list in bundle_list:
        print(acquired_list)

