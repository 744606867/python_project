import requests

# GitHub API 地址（返回仓库的文件树）
repo_url = "https://api.github.com/repos/jackfrued/Python-Core-50-Courses/git/trees/master?recursive=1"
base_url = "https://github.com/jackfrued/Python-Core-50-Courses/blob/master/"
# 发送请求
response = requests.get(repo_url)
md_files = []
# 检查请求是否成功
if response.status_code == 200:
    data = response.json()

    # 遍历所有文件，筛选出 .md 文件
    md_files = [file['path'] for file in data['tree'] if file['path'].endswith('.md')]

    # 打印出所有 .md 文件的路径
    for file in md_files:
        text = requests.get(base_url + file).content
        with open(file,'wb') as  file:
            file.write(text)
