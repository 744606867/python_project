import os
from docx import Document


def main(LXtype: str, textout: str) -> dict:
    # template_map = {
    #     "部门": "/opt/dify/templates/部门通知.docx",
    #     "公司": "/opt/dify/templates/分公司.docx",
    #     "纪检": "/opt/dify/templates/纪检通知.docx"
    # }
    template_map = {
        "部门": "C:\\Users\\cosmo\\Documents\\WeChat Files\\wxid_jo4wt0db8apa22\\FileStorage\\File\\2024-11\\部门通知.docx",
        "公司": "C:\\Users\\cosmo\\Documents\\WeChat Files\\wxid_jo4wt0db8apa22\\FileStorage\\File\\2024-11\\分公司.docx",
        "纪检": "C:\\Users\\cosmo\\Documents\\WeChat Files\\wxid_jo4wt0db8apa22\\FileStorage\\File\\2024-11\\纪检通知.docx"
    }
    template_path = template_map.get(LXtype)
    print(template_path)
    print(os.path.exists(template_path))
    if not template_path or not os.path.exists(template_path):
        return {'result': '模板未找到'}

    doc = Document(template_path)
    for paragraph in doc.paragraphs:
        if '(outside_content)' in paragraph.text:
            paragraph.text = paragraph.text.replace('(outside_content)', textout)

    result_path = f"C:\\Users\\cosmo\\Documents\\WeChat Files\\wxid_jo4wt0db8apa22\\FileStorage\\File\\2024-11\\result_{LXtype}.docx"
    doc.save(result_path)

    return {'result': result_path}


path = os.path
main("部门", "sss")

