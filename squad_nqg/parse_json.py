import json

def extract_titles(input_file, titles_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    with open(titles_file, 'r') as f:
        titles = set(line.strip() for line in f)
    print(titles)

    result = []
    print('lendata',len(data),len(titles))
    for item in data:
        if item.get('title') in titles:
            result.append(item)
    
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)

# 指定输入的 JSON 文件、保存需要读取的 title 的文件以及输出的 JSON 文件
input_json_file = 'test.json'
titles_file = 'doclist-test.txt'
output_json_file = 'test-nqg.json'

# 调用函数进行提取和保存
extract_titles(input_json_file, titles_file, output_json_file)
