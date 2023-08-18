import random

import plotly.express as px
import pandas as pd
import csv


def FCFS(s, q):  # First Come, First Serve
    result_list = [s]
    for i in q:
        result_list.append(i)
    # print("FCFS Result List:", result_list)
    return result_list


def SSTF(s, q):  # Shortest Seek Time First
    values = [[s, False]]
    for current in q:
        values.append([current, False])
    print(values)

    order = []
    for head in values:
        head[1] = True
        temp = []
        for current in values:
            if current[1] is False:
                temp.append([abs(head[0] - current[0]), False])
            else:
                temp.append([abs(head[0] - current[0]), True])
        min_value = 9999999
        for value in temp:
            if value[1] is False and value[0] < min_value:
                min_value = value[0]
        index1 = temp[min_value][0]
        order.append(values[index1])
    # print("SSTF Result List:", order)
    return order


def scan(s, q, min_range, max_range):
    result_list = [s]

    for x in range(s, max_range + 1):
        if x in q or x == max_range:
            result_list.append(x)
    for x in range(s - 1, min_range - 1, -1):
        if x in q or x == min_range:
            result_list.append(x)
    # print("Scan Result List:", result_list)
    return result_list


def c_scan(s, q, min_range, max_range):
    result_list = [s]

    for x in range(s, max_range + 1):
        if x in q or x == max_range:
            result_list.append(x)
    for x in range(min_range, s - 1):
        if x in q or x == min_range:
            result_list.append(x)
    # print("C-Scan Result List:", result_list)
    return result_list


def c_look(s, q):
    result_list = [53]
    for current in range(s, max(q) + 1):
        if current in q:
            result_list.append(current)
    for current in range(min(q), s - 1):
        if current in q:
            result_list.append(current)
    # print("C-Look Result List:", result_list)
    return result_list


def visualize_DSA(start, input_data):
    data = [['Index', 'Position', 'Color']]
    FCFS_data = FCFS(start, input_data)
    scan_data = scan(start, input_data, 0, 200)
    c_scan_data = c_scan(start, input_data, 0, 200)
    c_look_data = c_look(start, input_data)
    for i in range(len(FCFS_data)):
        data.append([i+1, FCFS_data[i], 'FCFS'])
    # for i in range(len(SSTF_data)):
    #     data.append([i+1, SSTF_data[i], '2'])
    for i in range(len(scan_data)):
        data.append([i+1, scan_data[i], 'Scan'])
    for i in range(len(c_scan_data)):
        data.append([i+1, c_scan_data[i], 'C-Scan'])
    for i in range(len(c_look_data)):
        data.append([i+1, c_look_data[i], 'C-Look'])

    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    data = pd.read_csv("data.csv")
    fig = px.line(data, y='Position', x='Index', color='Color')
    fig.show()


def visualize_cycles(start, input_data):
    data = [['Disk Scheduling Alg', '# of Cycles', 'Color']]

    FCFS_data = FCFS(start, input_data)
    scan_data = scan(start, input_data, 0, 200)
    c_scan_data = c_scan(start, input_data, 0, 200)
    c_look_data = c_look(start, input_data)

    FCFS_cycles = 0
    for index in range(len(FCFS_data) - 1):
        FCFS_cycles += abs(FCFS_data[index] - FCFS_data[index + 1])
    print("FCFS Cycles", FCFS_cycles)

    scan_cycles = 0
    for index in range(len(scan_data) - 1):
        scan_cycles += abs(scan_data[index] - scan_data[index + 1])
    print("Scan Cycles", scan_cycles)

    cscan_cycles = 0
    for index in range(len(c_scan_data) - 1):
        cscan_cycles += abs(c_scan_data[index] - c_scan_data[index + 1])
    print("C Scan Cycles", cscan_cycles)

    clook_cycles = 0
    for index in range(len(c_look_data) - 1):
        clook_cycles += abs(c_look_data[index] - c_look_data[index + 1])
    print("C Look Cycles", clook_cycles)

    data.append([1, FCFS_cycles, 'FCFS'])
    data.append([2, scan_cycles, 'Scan'])
    data.append([3, cscan_cycles, 'C-Scan'])
    data.append([4, clook_cycles, 'C-Look'])

    with open('data2.csv', 'w', encoding='UTF8', newline='') as g:
        writer = csv.writer(g)
        writer.writerows(data)

    data2 = pd.read_csv("data2.csv")
    fig2 = px.bar(data2, y='# of Cycles', x='Disk Scheduling Alg', color='Color')
    fig2.show()


if __name__ == '__main__':
    values = []
    for i in range(10):
        values.append(random.randint(0, 200))

    start = random.randint(0, 200)

    print("Start:", start)
    print("Data:", values)

    visualize_DSA(start, values)
    visualize_cycles(start, values)
    # queue = [98, 183, 37, 122, 14, 124, 65, 67]
    # start = 53
    # data = [['Index', 'Position', 'Color']]
    # data2 = [['Disk Scheduling Alg', '# of Cycles', 'Color']]
    # FCFS_data = FCFS(start, queue)
    # SSTF_data = SSTF(start, queue)
    # scan_data = scan(start, queue, 0, 200)
    # c_scan_data = c_scan(start, queue, 0, 200)
    # c_look_data = c_look(start, queue)
    # for i in range(len(FCFS_data)):
    #     data.append([i+1, FCFS_data[i], 'FCFS'])
    # for i in range(len(SSTF_data)):
    #     data.append([i+1, SSTF_data[i], '2'])
    # for i in range(len(scan_data)):
    #     data.append([i+1, scan_data[i], 'Scan'])
    # for i in range(len(c_scan_data)):
    #     data.append([i+1, c_scan_data[i], 'C-Scan'])
    # for i in range(len(c_look_data)):
    #     data.append([i+1, c_look_data[i], 'C-Look'])

    # FCFS_cycles = 0
    # for index in range(len(FCFS_data) - 1):
    #     FCFS_cycles += abs(FCFS_data[index] - FCFS_data[index + 1])
    # print("FCFS Cycles", FCFS_cycles)
    #
    # scan_cycles = 0
    # for index in range(len(scan_data) - 1):
    #     scan_cycles += abs(scan_data[index] - scan_data[index + 1])
    # print("Scan Cycles", scan_cycles)
    #
    # cscan_cycles = 0
    # for index in range(len(c_scan_data) - 1):
    #     cscan_cycles += abs(c_scan_data[index] - c_scan_data[index + 1])
    # print("C Scan Cycles", cscan_cycles)
    #
    # clook_cycles = 0
    # for index in range(len(c_look_data) - 1):
    #     clook_cycles += abs(c_look_data[index] - c_look_data[index + 1])
    # print("C Look Cycles", clook_cycles)
    #
    # with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(data)
    #
    # data = pd.read_csv("data.csv")
    # fig = px.line(data, y='Position', x='Index', color='Color')
    # fig.show()

    # data2.append([1, FCFS_cycles, 'FCFS'])
    # data2.append([2, scan_cycles, 'Scan'])
    # data2.append([3, cscan_cycles, 'C-Scan'])
    # data2.append([4, clook_cycles, 'C-Look'])
    #
    # with open('data2.csv', 'w', encoding='UTF8', newline='') as g:
    #     writer = csv.writer(g)
    #     writer.writerows(data2)
    #
    # data2 = pd.read_csv("data2.csv")
    # fig2 = px.bar(data2, y='# of Cycles', x='Disk Scheduling Alg', color='Color')
    # fig2.show()
