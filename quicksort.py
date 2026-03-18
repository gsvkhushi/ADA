import random
import time
import matplotlib.pyplot as plt

# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


n_list = [5000, 10000, 15000, 20000, 25000]
sort_time = []
for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    quick_sort(l)
    e_t = time.time()
    sort_time.append(e_t - s_t)
print("Input sizes:", n_list)
print("Sorting times:", sort_time)

# Plot Graph
plt.plot(n_list,sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Quick Sort Time Complexity")
plt.grid(True)
plt.show()

# Input sizes: [5000, 10000, 15000, 20000, 25000]
# Sorting times: [0.012873172760009766, 0.0366976261138916, 0.06611156463623047, 0.1148386001586914, 0.16009807586669922]