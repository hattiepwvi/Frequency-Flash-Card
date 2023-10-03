import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file, open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in txt_file:
            # 使用空格分割每一行的内容
            data = line.strip().split(' ')
            # 将分割后的内容写入csv文件
            csv_writer.writerow(data)

# 指定输入和输出文件的路径
input_file = 'input.txt'
output_file = 'output.csv'

# 调用函数将txt文件转换为csv文件
txt_to_csv(input_file, output_file)