import os

data_dir = '/home/chinlin/Documents/dlpifp/data'
output_file = '/home/chinlin/Documents/dlpifp/processed_data.txt'

# 关键词字典
keyword_dict = {
    'data_0': 'bug',
    'data_1': 'caking',
    'data_2': 'hair',
    'data_3': 'piece',
    'data_4': 'rust'
}

# 存储处理后的数据
processed_data = []

# 遍历文件列表，对每个文件进行处理
for file_name in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file_name)
    if os.path.isfile(file_path):
        keyword = keyword_dict.get(file_name.split('.')[0])

        # 读取原始文件数据
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 处理每一行数据
        for line in lines:
            line = line.strip()
            if '\t' in line:
                sentence, keyword = line.split('\t')
                processed_sentence = sentence + "请提供我解决方案。"
                processed_data.append(processed_sentence + '\t' + keyword)

# 将处理后的数据写入文件
with open(output_file, 'w', encoding='utf-8') as file:
    for line in processed_data:
        file.write(line + '\n')
