table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_data):
    # 各列の最長の文字数を0で初期化
    col_widths = [0] * len(table_data)
    
    # 各列の最大文字数を計算
    for i in range(len(table_data)):
        for item in table_data[i]:
            if len(item) > col_widths[i]:
                col_widths[i] = len(item)
    
    # 行単位で表示
    for row in zip(*table_data):
        print("  ".join(item.rjust(col_widths[i]) for i, item in enumerate(row)))

print_table(table_data)

