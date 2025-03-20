import base64
import urllib.parse

def encode_base64(url):
    """对URL进行Base64编码"""
    url_bytes = url.encode('utf-8')  # 将URL转换为字节串
    base64_bytes = base64.b64encode(url_bytes)  # Base64编码
    return base64_bytes.decode('utf-8')  # 返回Base64编码后的字符串

def encodeURIComponent(url):
    """对URL进行URL编码"""
    return urllib.parse.quote(url, safe='')

def create_open_url(preview_url):
    """生成打开的URL"""
    # 对preview_url进行Base64编码
    base64_encoded_url = encode_base64(preview_url)
    # 对Base64编码后的URL进行URL编码
    encoded_url = encodeURIComponent(base64_encoded_url)
    # 构造最终的URL
    return f'http://192.168.0.115:38012/preview/onlinePreview?url={encoded_url}'

# 示例用法
preview_url = "http://192.168.0.241/doc/bmtz.docx"  # 你要编码的URL
result_url = create_open_url(preview_url)

if __name__ == '__main__':
    print(result_url)


