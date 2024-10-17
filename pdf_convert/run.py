import pdf_utils  # 导入你创建的工具模块
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# 使用 tkinter 来选择文件
def select_files():
    # 隐藏主窗口
    Tk().withdraw()

    # 选择 PDF 文件
    pdf_path = askopenfilename(title="选择 PDF 文件", filetypes=[("PDF 文件", "*.pdf")])
    if not pdf_path:
        print("未选择 PDF 文件")
        return

    # 选择输出 Word 文件保存路径
    output_docx_path = asksaveasfilename(title="保存 Word 文件", defaultextension=".docx",
                                         filetypes=[("Word 文件", "*.docx")])
    if not output_docx_path:
        print("未选择保存路径")
        return

    # 调用工具模块中的方法
    pdf_utils.extract_text_from_pdf(pdf_path, output_docx_path)
    pdf_utils.extract_images_with_ocr(pdf_path, output_docx_path)
    # pdf_utils.render_page_as_image_and_ocr(pdf_path, output_docx_path)

# 运行文件选择
select_files()
