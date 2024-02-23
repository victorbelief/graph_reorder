def sort_edgelist(edgelist_file):
    """
    对 edgelist 文件中的每行按照 start_node 的邻居数量和 end_node 的大小进行排序
    """

    # 使用字典存储节点的邻居数量和边信息
    node_degrees = {}
    edges = []

    # 从文件中读取边信息，统计每个节点的邻居数量和存储边信息
    with open(edgelist_file, 'r') as f:
        for line in f:
            start_node, end_node = map(int, line.strip().split())

            # 统计 start_node 的邻居数量
            if start_node not in node_degrees:
                node_degrees[start_node] = 0
            node_degrees[start_node] += 1

            # 将边信息保存到列表
            edges.append((start_node, end_node))

    # 对边信息进行排序，首先按照 start_node 的邻居数量进行降序排序，然后按照 start_node 和 end_node 的大小进行排序
    sorted_edges = sorted(edges, key=lambda x: (-node_degrees[x[0]], x[0], x[1]))

    return sorted_edges

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

edgelist_file = "lg/lg_sorted.txt"
output_file = "lg/lg_updated.txt"

# 进行排序
sorted_edges = sort_edgelist(edgelist_file)
unique_edges = remove_duplicate_edges(sorted_edges)

# 将排序后的边写入输出文件
with open(output_file, 'w') as f_out:
    for edge in unique_edges:
        f_out.write(f"{edge[0]} {edge[1]}\n")
