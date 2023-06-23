from datetime import datetime
datetime.fromtimestamp



def comprehensions():
    list = [i for i in range(1000000)]



def generator():
    my_list =[]
    for i in range(0,1000000):
        my_list.append(i)

for_times = []
comprehensions_times = []
n=100

for i in range(0,n):
    start = datetime.now().timestamp()
    generator()
    end = datetime.now().timestamp()
    time_delta = end - start
    for_times.append(time_delta)

    start = datetime.now().timestamp()
    comprehensions()
    end = datetime.now().timestamp()
    time_delta = end - start
    comprehensions_times.append(time_delta)

result_for = sum(for_times)/n
result_compreh = sum(comprehensions_times)/n
print(result_for)
print(result_compreh)
