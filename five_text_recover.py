import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_label_files(label_dir):
    for filename in os.listdir(label_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(label_dir, filename)
            with open(file_path, 'r') as file:
                line = file.readline().strip()
                values = line.split()
                new_values = values[:5]
                new_line = " ".join(new_values)

            with open(file_path, 'w') as file:
                file.write(new_line)

            # 打印文件信息到控制台
            print(f"处理文件: {filename}")


def select_directory():
    label_directory = filedialog.askdirectory()
    if label_directory:
        process_label_files(label_directory)
        messagebox.showinfo("完成", "标签文件处理完成！")

root = tk.Tk()
root.title("标签文件处理器")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="选择标签目录", command=select_directory)
select_button.pack(pady=5)

root.mainloop()