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
        return None


def ping_servers(data):
    """
    对多个服务器进行连通性测试，并返回延迟时间和城市对应关系。
    """
    results = []
    for address, city in zip(data['addresses'], data['cities']):
        delay = ping_server(address)
        if delay is not None and delay != 2000.0:
            result = f"{city} ({address}) - 平均延迟: {delay} ms"
        else:
            result = f"{city} ({address}) - 失败超时！"
        results.append(result)
    return results


# 执行连通性测试并输出结果
print('请稍候，至多需要'+str(len(data['addresses'])*2*4) +'s')
ping_results = ping_servers(data)
for result in ping_results:
    print(result)
