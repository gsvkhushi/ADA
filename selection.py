import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
            
n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []
for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    selection_sort(l)
    e_t = time.time()
    sort_time.append(e_t - s_t)
print("Input sizes:", n_list)
print("Sorting times:", sort_time)

#plotting the graph
plt.plot(n_list,sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("selection sort: Time Complexity Analysis")
plt.grid(True)
plt.show()

# Input sizes: [5000, 6000, 7000, 8000, 9000, 10000]
# Sorting times: [0.3334519863128662, 0.46233177185058594, 0.6845037937164307, 0.8631541728973389, 1.109205722808838, 1.3857176303863525]
