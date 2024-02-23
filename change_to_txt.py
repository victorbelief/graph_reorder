# 打开文件
with open("wang/out.wang-amazon", "r") as f:
    # 读取每行数据
    lines = f.readlines()
    # 遍历每行数据
    for i in range(len(lines)):
        # 对每行数据进行分割
        data = lines[i].strip().split()
        # 只保留前两列数据
        data = data[:2]
        data.reverse()
        # 将处理后的数据重新拼接成一行
        new_line = " ".join(data) + "\n"
        # 将处理后的数据写回原文件中，或者写入新的文件中
        with open("wang/wang.txt", "a") as f_new:
            f_new.write(new_line)
