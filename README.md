# Code Conversion Tool - File Processor

## Project Overview
This tool is designed to efficiently process `.py` and `.java` files, converting their content into text format for saving. It supports single-file processing and batch processing for folders, featuring a user-friendly interface and flexible output settings.

### Key Features
- **Multilingual Support**: Switch between English and Chinese interfaces.
- **File and Folder Processing**: Seamlessly handle single or multiple files.
- **Structured Output**: Preserve folder structure when saving processed content.

---

## Requirements
- **Python**: Version >= 3.7  
- **Libraries**:
  - Standard libraries: `os`, `tkinter`, `filedialog`, `messagebox`

---

## Quick Start

1. Clone the repository and navigate to the directory:
   ```bash
   git clone https://github.com/quitedob/readcode.git
   cd readcode
   ```

2. Run the scripts:
   ```bash
   python readpython.py  # For processing Python files
   python readjava.py    # For processing Java files
   ```

---

## Usage Instructions

1. Launch the application.
2. Select your preferred language.
3. Choose an operation based on your needs:
   - **Process a Single File**: Select a `.py` or `.java` file.
   - **Process a Folder**: Select a folder containing multiple files to generate text outputs in bulk.
4. Optional: Specify a custom save directory.
5. Confirm results or check the logs.

---

## File Structure
```
readcode/
├── readpython.py       # Python file processing script
├── readjava.py         # Java file processing script
├── README.md           # Documentation
├── LICENSE             # License agreement
```

---

### Custom Features
You can extend the script to support additional file types or languages (e.g., YAML, JSON).

### Declaration
This project and its related code are for learning and research purposes only. The use of third-party libraries and tools involved in the project must comply with their respective license agreements. The author shall not be liable for any losses or legal liabilities arising from the use of this project.

