import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams["axes.unicode_minus"]=False


# 读取动物信息表
df = pd.read_csv('./data/animal.csv', encoding='gbk')

# 1）按照动物的速度从高到低进行排序，并输出最高速度，最低速度和平均速度
df_sorted = df.sort_values(by='speed', ascending=False)
max_speed = df_sorted['speed'].max()
min_speed = df_sorted['speed'].min()
average_speed = df_sorted['speed'].mean()

print(f"最高速度: {max_speed} km/h")
print(f"最低速度: {min_speed} km/h")
print(f"平均速度: {average_speed:.2f} km/h")

# 2）统计计算出所有动物中大于平均速度的数量
above_average_count = df[df['speed'] > average_speed].shape[0]
print(f"大于平均速度的动物数量: {above_average_count}")

# 3）可视化展示数据，让用户能够直观的看出动物奔跑速度间的差异
plt.figure(figsize=(10, 6))
plt.bar(df_sorted['name'], df_sorted['speed'], color='skyblue')
plt.title('动物奔跑速度')
plt.xlabel('动物名称')
plt.ylabel('奔跑速度 (km/h)')
plt.xticks(rotation=45)
plt.axhline(y=average_speed, color='r', linestyle='--', label='平均速度')
plt.legend()
plt.show()

 