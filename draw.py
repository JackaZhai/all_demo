import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
file_path = r'C:\Users\JackZhai\PycharmProjects\all_demo\results.csv'
df = pd.read_csv(file_path)

# Plot the data
print(df.head())
# columns_to_plot = [
#     'train/box_om', 'train/cls_om', 'train/dfl_om',
#     'train/box_oo', 'train/cls_oo', 'train/dfl_oo',
#     'metrics/precision(B)', 'metrics/recall(B)',
#     'metrics/mAP50(B)', 'metrics/mAP50-95(B)',
#     'val/box_om', 'val/cls_om', 'val/dfl_om',
#     'val/box_oo', 'val/cls_oo', 'val/dfl_oo',
#     'lr/pg0', 'lr/pg1', 'lr/pg2'
# ]

#创建轴
plt.figure(figsize=(20, 10))
plt.plot(df['epoch'], df['train/box_om'], label='train/box_om')
plt.plot(df['epoch'], df['metrics/mAP50(B)'], label='metrics/mAP50(B)')

# for column in columns_to_plot:
#     if column in df.columns:
#         plt.plot(df['epoch'], df[column], label=column)
#
#         plt.title('Training Metrics')
#         plt.xlabel('Epoch')
#         plt.ylabel('Value')
#         plt.legend(loc='upper right')

plt.title('Training Metrics')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.legend(loc='upper right')
plt.show()