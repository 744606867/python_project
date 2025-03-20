from nacos.client import NacosClient

# Nacos 服务器信息
NACOS_SERVER_ADDRESSES = "192.168.0.195:5040"
NAMESPACE = "cosmosource"  # 如果使用的是默认命名空间，则为空字符串

# 服务信息
SERVICE_NAME = "python_service"
IP = "127.0.0.1"
PORT = 5001
USERNAME = "admin"
PASSWORD = "admin@123qwe12"  # 注意替换为你的密码
# 创建 Nacos 客户端
client = NacosClient(NACOS_SERVER_ADDRESSES, namespace=NAMESPACE,username = USERNAME,password=PASSWORD)
# 注册服务
client.add_naming_instance(SERVICE_NAME, IP, PORT)
config = client.get_config('common.properties', 'DEFAULT_GROUP')
# 将配置转换为字典
config_dict = {}

for line in config.splitlines():
    # 跳过注释行
    if line.strip().startswith('#') or not line.strip():
        continue
    # 分割键值对
    key_value = line.split('=', 1)
    if len(key_value) == 2:
        key, value = key_value
        config_dict[key.strip()] = value.strip()

# 输出字典
print(config_dict['cosmosource.cloudy.address'])

