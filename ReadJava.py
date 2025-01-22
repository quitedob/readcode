import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# 定义语言资源
languages = {
    'en': {
        'title': 'Java File Processor',
        'select_language': 'Select Language',
        'select_output': 'Select Output Folder Adress',
        'select_file': 'Select a Java File',
        'select_folder': 'Select a Folder Containing Java Files',
        'operation_completed': 'Operation completed successfully.',
        'error': 'An error occurred:',
        'folder_structure': 'Folder Structure',
    },
    'zh': {
        'title': 'Java 文件处理器',
        'select_language': '选择语言',
        'select_output': '选择输出文件夹地址',
        'select_file': '选择一个 Java 文件',
        'select_folder': '选择包含 Java 文件的文件夹',
        'operation_completed': '操作成功完成。',
        'error': '发生错误：',
        'folder_structure': '文件夹结构',
    }
}

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.language = 'en'  # 默认语言为英文
        self.output_path = os.path.join(os.path.expanduser('~'), 'Desktop')  # 默认输出路径为桌面
        self.title(languages[self.language]['title'])
        self.geometry('400x300')
        self.create_widgets()

    def create_widgets(self):
        # 语言选择
        self.lang_label = ttk.Label(self, text=languages[self.language]['select_language'])
        self.lang_label.pack(pady=5)

        self.lang_combobox = ttk.Combobox(self, values=['English', '中文'], state='readonly')
        self.lang_combobox.current(0 if self.language == 'en' else 1)
        self.lang_combobox.pack(pady=5)
        self.lang_combobox.bind('<<ComboboxSelected>>', self.change_language)

        # 修改输出路径
        self.output_button = ttk.Button(self, text=languages[self.language]['select_output'], command=self.select_output_folder)
        self.output_button.pack(pady=10)

        # 文件选择按钮
        self.file_button = ttk.Button(self, text=languages[self.language]['select_file'], command=self.select_file)
        self.file_button.pack(pady=5)

        # 文件夹选择按钮
        self.folder_button = ttk.Button(self, text=languages[self.language]['select_folder'], command=self.select_folder)
        self.folder_button.pack(pady=5)

    def change_language(self, event):
        selected_lang = self.lang_combobox.get()
        self.language = 'en' if selected_lang == 'English' else 'zh'
        self.update_texts()

    def update_texts(self):
        self.title(languages[self.language]['title'])
        self.lang_label.config(text=languages[self.language]['select_language'])
        self.output_button.config(text=languages[self.language]['select_output'])
        self.file_button.config(text=languages[self.language]['select_file'])
        self.folder_button.config(text=languages[self.language]['select_folder'])

    def select_output_folder(self):
        folder_path = filedialog.askdirectory(title=languages[self.language]['select_output'])
        if folder_path:
            self.output_path = folder_path
            messagebox.showinfo(languages[self.language]['select_output'], folder_path)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title=languages[self.language]['select_file'],
            filetypes=[('Java files', '*.java')]
        )
        if file_path:
            self.process_single_file(file_path)

    def select_folder(self):
        folder_path = filedialog.askdirectory(title=languages[self.language]['select_folder'])
        if folder_path:
            self.process_folder(folder_path)

    def process_single_file(self, file_path):
        combined_content = f"File: {os.path.basename(file_path)}\n\n"
        file_content = self.read_file_content(file_path)
        if file_content:
            combined_content += file_content
        self.save_to_output('single_java_file.txt', combined_content)
        messagebox.showinfo(languages[self.language]['operation_completed'], self.output_path)

    def process_folder(self, folder_path):
        # 获取所有子文件夹及其 .java 文件
        java_files_dict = self.get_java_files(folder_path)

        # 创建总文件夹
        main_folder_name = os.path.basename(folder_path)
        main_save_path = os.path.join(self.output_path, main_folder_name)

        # 保存文件夹结构
        folder_structure = self.generate_folder_structure(folder_path)
        self.save_to_path(main_save_path, "folder_structure.txt", folder_structure)

        # 遍历每个子文件夹，保存其 .java 文件内容到对应的 .txt 文件
        for subfolder, java_files in java_files_dict.items():
            combined_content = []
            for java_file in java_files:
                combined_content.append(f"File: {os.path.basename(java_file)}\n\n")
                file_content = self.read_file_content(java_file)
                if file_content:
                    combined_content.append(file_content)
                    combined_content.append('\n\n')  # 文件内容后换行
            subfolder_name = os.path.basename(subfolder)
            self.save_to_path(main_save_path, f"{subfolder_name}.txt", ''.join(combined_content))

        messagebox.showinfo(languages[self.language]['operation_completed'], self.output_path)

    def get_java_files(self, folder_path):
        java_files_dict = {}
        for root, _, files in os.walk(folder_path):
            java_files = [os.path.join(root, file) for file in files if file.endswith('.java')]
            if java_files:
                java_files_dict[root] = java_files
        return java_files_dict

    def generate_folder_structure(self, folder_path, indent=""):
        structure = ""
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                structure += f"{indent}[Folder] {item}\n"
                structure += self.generate_folder_structure(item_path, indent + "  ")
            else:
                structure += f"{indent}[File] {item}\n"
        return structure

    def read_file_content(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            messagebox.showerror(languages[self.language]['error'], str(e))
            return None

    def save_to_path(self, save_path, file_name, content):
        try:
            os.makedirs(save_path, exist_ok=True)
            full_path = os.path.join(save_path, file_name)
            with open(full_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"文件已保存到: {full_path}")
        except Exception as e:
            messagebox.showerror(languages[self.language]['error'], str(e))

if __name__ == '__main__':
    app = Application()
    app.mainloop()
