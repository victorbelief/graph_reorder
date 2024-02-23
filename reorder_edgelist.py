from collections import OrderedDict

# 初始化一个有序字典用于记录已读取的 start_node
start_nodes_dict = OrderedDict()
edges = []
# 读取 edgelist 文件的每一行
with open('lg/lg_updated.txt', 'r') as file:
    for line in file:
        # 去除行尾的换行符并按空格分割 start_node 和 end_node
        start_node, end_node = line.strip().split(' ')
        edges.append((int(start_node), int(end_node)))
        # 如果 start_node 不在字典中，将其添加到字典中，并记录其出现的顺序
        if start_node not in start_nodes_dict:
            start_nodes_dict[start_node] = None
# 将字典的键（即 start_node）转换为列表
start_nodes_list = list(start_nodes_dict.keys())
num_list = list(map(int, start_nodes_list))
num_list.sort()
start_list = list(map(str, num_list))
my_dict = dict(zip(start_nodes_list,start_list))
# 打开待处理的文件，以读写模式打开
with open('lg/lg_reordered.txt', 'w') as f:
    # 使用 zip 函数将两个列表合并
    for edge in edges:
        # 按行写入数据到文件
        f.write('{} {}\n'.format(my_dict.get(str(edge[0])), edge[1]))




