import random
#round-robin works
#maybe a problem with flags EF/EFX or calculating the evaluation matrices

#change instances accordingly (put 10000)
instances=10000
count_ef=0
count_efx=0

#extra counters // skip (not needed just for testing)
count_ef1=0
count_not_ef1=0
count_not_ef=0
count_not_efx=0
#end of extra counters


for k in range(instances):

    # Generate random number of bundles between 20 and 30
    num_bundles = random.randint(20, 30)
    #num_bundles=10

    # Generate random number of lists between 50 and 200
    num_lists = random.randint(50, 200)
    #num_lists=70

    # Generate data with random integer values between 1 and 20
    data = [[random.randint(1, 20) for _ in range(num_bundles)] for _ in range(num_lists)]
    """
    # Print the original data
    print("Original data:")
    for row in data:
        print(row)
    """

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

    """
    # Print the lists acquired by each bundle separately
    for i, bundle_list in enumerate(bundle_lists):
        print(f"\nLists acquired by bundle {i+1}:")
        for acquired_list in bundle_list:
            print(acquired_list)
    """

    # Calculate valuations of bundles towards each other EF
    valuations = []

    for i in range(num_bundles):
        bundle_valuations = []
        for j in range(num_bundles):
            if i == j:
                # Calculate self-valuation
                self_valuation = sum(bundle[i] for bundle in bundle_lists[i])
                bundle_valuations.append(self_valuation)
            else:
                # Calculate valuation based on the sum of elements from lists in bundle j
                valuation = sum(bundle[i] for bundle in bundle_lists[j])
                bundle_valuations.append(valuation)
        valuations.append(bundle_valuations)

    """
    # Print valuations
    print("Valuations:")
    for i, bundle_valuations in enumerate(valuations):
        print(f"Bundle {i+1} valuations towards other bundles:", bundle_valuations)
    """
    # Flag to track if any bundle envies another
    envy_flag = False

    # Check if a bundle envies another
    for i, bundle_valuations in enumerate(valuations):
        if bundle_valuations[i] != max(bundle_valuations):
            envy_flag = True

    # If no bundle envies another, print EF allocation
    if not envy_flag:
        #print("It is an EF (Envy-Free) allocation.")
        count_ef+=1
    else:
        #print("It is not an EF (Envy-Free) allocation.")
        count_not_ef+=1
    # Calculate valuations of bundles towards each other without adding the maximum of the ith elements (EF-1)
    valuations_without_max = []

    for i in range(num_bundles):
        bundle_valuations_without_max = []
        for j in range(num_bundles):
            if i == j:
                # Calculate self-valuation
                self_valuation = sum(bundle[i] for bundle in bundle_lists[i])
                bundle_valuations_without_max.append(self_valuation)
            else:
                # Find the maximum ith element of the lists in bundle j
                max_ith_elements = max(bundle[i] for bundle in bundle_lists[j])
                # Calculate valuation by summing all ith elements of the lists in bundle j, excluding the maximum ith element
                valuation = sum(bundle[i] for bundle in bundle_lists[j] if bundle[i] != max_ith_elements)
                bundle_valuations_without_max.append(valuation)
        valuations_without_max.append(bundle_valuations_without_max)
    """
    # Print valuations without adding the maximum of the ith elements
    print("Valuations without adding the maximum of the ith elements:")
    for i, bundle_valuations in enumerate(valuations_without_max):
        print(f"Bundle {i+1} valuations towards other bundles:", bundle_valuations)
    """

    # Flag to track if the allocation is an EF1 allocation
    is_ef1_allocation = True

    # Check if it is an EF1 allocation
    for i, bundle_valuations in enumerate(valuations_without_max):
        for j, valuation in enumerate(bundle_valuations):
            if i != j and valuation > bundle_valuations[i]:
                is_ef1_allocation = False
                break

    # Print the result
    if is_ef1_allocation:
        #print("It is an EF1 (Envy-Free up to one good) allocation.")
        count_ef1+=1
    else:
        #print("It is not an EF1 (Envy-Free up to one good) allocation.")
        count_not_ef1+=1


    # Calculate valuations of bundles towards each other without adding the minimum of the ith elements EFX
    valuations_without_min = []

    for i in range(num_bundles):
        bundle_valuations_without_min = []
        for j in range(num_bundles):
            if i == j:
                # Calculate self-valuation
                self_valuation = sum(bundle[i] for bundle in bundle_lists[i])
                bundle_valuations_without_min.append(self_valuation)
            else:
                # Find the minimum ith element of the lists in bundle j
                min_ith_elements = min(bundle[i] for bundle in bundle_lists[j])
                # Calculate valuation by summing all ith elements of the lists in bundle j, excluding the minimum ith element
                valuation = sum(bundle[i] for bundle in bundle_lists[j] if bundle[i] != min_ith_elements)
                bundle_valuations_without_min.append(valuation)
        valuations_without_min.append(bundle_valuations_without_min)

    """
    # Print valuations without adding the minimum of the ith elements
    print("Valuations without adding the minimum of the ith elements:")
    for i, bundle_valuations in enumerate(valuations_without_min):
        print(f"Bundle {i+1} valuations towards other bundles:", bundle_valuations)
    """

    # Flag to track if the allocation is an EF1 allocation
    is_efx_allocation = True

    # Check if it is an EF1 allocation
    for i, bundle_valuations in enumerate(valuations_without_min):
        for j, valuation in enumerate(bundle_valuations):
            if i != j and valuation > bundle_valuations[i]:
                is_ef1_allocation = False
                break

    # Print the result
    if is_efx_allocation:
        #print("It is an EFX (Envy-Free up to one good) allocation.")
        count_efx+=1
    else:
        #print("It is not an EFX (Envy-Free up to one good) allocation.")
        count_not_efx+=1


print("Total EF allocations: ", count_ef)
print("Total EFX allocations: ", count_efx)
