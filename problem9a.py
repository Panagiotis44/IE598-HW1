import random

def generate_random_integer_list():
    n = random.randint(50, 200)
    return [random.randint(1, 20) for _ in range(n)]

def split_list_into_n_lists(int_list, n):
    # Calculate the length of each bundle
    bundle_length = len(int_list) // n
    # Create n bundles
    bundles = [int_list[i:i+bundle_length] for i in range(0, len(int_list), bundle_length)]
    # If there are leftover elements, distribute them evenly among the bundles
    if len(int_list) % n != 0:
        remainder = len(int_list) % n
        for i in range(remainder):
            bundles[i].append(int_list[-(i+1)])
    # Create dictionary with bundle names
    bundle_dict = {}
    for i in range(n):
        bundle_name = f"bundle{i+1}"
        bundle_dict[bundle_name] = bundles[i]
    return bundle_dict

def calculate_bundle_sums(bundle_dict):
    bundle_sums = {}
    for bundle_name, bundle_list in bundle_dict.items():
        bundle_sum = sum(bundle_list)
        bundle_sums[bundle_name] = bundle_sum
        sorted_bundles = sorted(bundle_sums.items(), key=lambda x: x[1])  # Sort bundles by sum
    return sorted_bundles


"""
def adjust_bundles(flag,bundle_dict, sorted_bundles):

    min_sum_bundle_i = sorted_bundles[0][1]
    max_sum_bundle_j = sorted_bundles[-1][1]
    min_element_bundle_j = min(bundle_dict[sorted_bundles[-1][0]])

    if max_sum_bundle_j - min_sum_bundle_i > min_element_bundle_j:
        # Move the smallest element from bundle j to bundle i
        min_element = min(bundle_dict[sorted_bundles[-1][0]])
        bundle_dict[sorted_bundles[0][0]].append(min_element)
        bundle_dict[sorted_bundles[-1][0]].remove(min_element)
    else:
        flag_isEfx= True
    #return bundle_dict
"""

# Example usage
            

#integer_list = generate_random_integer_list()
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,23,12,3,12,3,5,3,7,9,7,53,1,34,5,34,23,78,56,94,94,24,87,54]

#num_of_bundles = random.randint(20,30)
num_of_bundles = 8

flag_isEfx = False

bundle_dict = split_list_into_n_lists(integer_list, num_of_bundles)
print(bundle_dict)
while flag_isEfx==False:

    sorted_bundles = calculate_bundle_sums(bundle_dict)

    #print(bundle_dict)
    #print(sorted_bundles)

    min_sum_bundle_i = sorted_bundles[0][1]
    max_sum_bundle_j = sorted_bundles[-1][1]
    min_element_bundle_j = min(bundle_dict[sorted_bundles[-1][0]])

    if max_sum_bundle_j - min_sum_bundle_i > min_element_bundle_j:
        # Move the smallest element from bundle j to bundle i
        min_element = min(bundle_dict[sorted_bundles[-1][0]])
        bundle_dict[sorted_bundles[0][0]].append(min_element)
        bundle_dict[sorted_bundles[-1][0]].remove(min_element)
    else:
        flag_isEfx= True
    
print(bundle_dict)
