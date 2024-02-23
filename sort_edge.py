def sort_edges(edges):
    """
    对边列表进行排序，首先按照<source_node>从小到大排序，
    当<source_node>相等时，再按照<target_node>从小到大排序。
    """
    edges.sort(key=lambda x: (x[0], x[1]))
    return edges

def remove_duplicate_edges(edges):
    """
    去除重复边，即<source_node>和<target_node>值相同的两行中的一行。
    """
    unique_edges = []
    seen_edges = set()
    for edge in edges:
        # 将边表示为元组，并将元组转换为不可变哈希值
        edge_key = (edge[0], edge[1])
        # 如果该边没有出现过，则加入unique_edges列表，并将其添加到seen_edges集合中
        if edge_key not in seen_edges:
            unique_edges.append(edge)
            seen_edges.add(edge_key)
    return unique_edges

def read_edgelist(filename):
    """
    从edgelist文件中读取图数据，返回节点数、边数和边列表。
    """
    edges = []
    nodes = set()
    with open(filename, 'r') as file:
        for line in file:
            if(line.strip().split()[0]=="%"):
                continue
            source = line.strip().split()[0]
            target = line.strip().split()[1]
            edges.append((int(source), int(target)))
            '''
            nodes.add(int(source))
            nodes.add(int(target))
    num_nodes = max(nodes) + 1
    num_edges = len(edges)
    '''
    #return num_nodes, num_edges, edges
    return edges

def write_sorted_edgelist(filename, edges):
    """
    将排序后的边列表写入文件。
    """
    with open(filename, 'w') as file:
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]}\n")



# 读取edgelist文件
filename = 'lg/out.livejournal-groupmemberships'
#num_nodes, num_edges, edges = read_edgelist(filename)
edges = read_edgelist(filename)


# 对边进行排序
sorted_edges = sort_edges(edges)
print("sort done")


# 去除重复边
unique_edges = remove_duplicate_edges(edges)
print("unique done")



# 将结果写入文件
write_sorted_edgelist('lg/lg_sorted.txt', unique_edges)
print("write done")




