from pythonping import ping

data = {
    'addresses': ['198.23.49.100', '198.23.228.15', '192.3.165.30', '107.173.164.160', '192.210.207.88',
                  '192.3.81.8', '192.3.253.2', '204.13.154.3'],
    'cities': ['Dallas', 'Chicago', 'New Jersey', 'Atlanta', 'San Jose', 'New York', 'Seattle', 'Los Angeles']
}

def ping_server(address):
    """
    使用pythonping库测试服务器连通性，并返回延迟时间。
    """
    try:
        response_list = ping(address, count=4, timeout=2)  # 发送4个ping请求，超时时间为2秒
        delay = response_list.rtt_avg_ms  # 获取平均延迟时间
        return delay
    except Exception:
        return float('inf')  # 设置失败的结果为正无穷大

def ping_servers(data):
    """
    对多个服务器进行连通性测试，并返回延迟时间和城市对应关系，按延迟时间排序。
    """
    results = []
    for address, city in zip(data['addresses'], data['cities']):
        delay = ping_server(address)
        results.append((city, address, delay))

    # 对结果进行排序，延迟时间从小到大，失败的结果放在最后
    results = sorted(results, key=lambda x: (x[2] is None, x[2]))

    # 生成结果字符串
    result_strings = []
    for result in results:
        city, address, delay = result
        if delay is not None:
            result_string = f"{city} ({address}) - Delay: {delay} ms"
        else:
            result_string = f"{city} ({address}) - Unreachable"
        result_strings.append(result_string)
    return result_strings

# 执行连通性测试并输出排序后的结果
ping_results = ping_servers(data)
for result in ping_results:
    print(result)
