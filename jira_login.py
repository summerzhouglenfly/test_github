import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin

def login_jira(base_url, username, password):
    """
    尝试登录 Jira 并验证登录是否成功
    """
    # 拼接认证接口（Jira 常用 API 路径）
    auth_url = urljoin(base_url, "/rest/auth/1/session")
    
    try:
        # 使用 Basic Authentication 发送请求
        response = requests.post(
            auth_url,
            auth=HTTPBasicAuth(username, password),
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        # 根据状态码判断登录结果
        if response.status_code == 200:
            return "成功"
        elif response.status_code == 401:
            return "错误原因：用户名或密码错误"
        else:
            return f"错误原因：HTTP {response.status_code} - {response.text}"
    
    except requests.exceptions.ConnectionError:
        return "错误原因：无法连接到服务器，请检查网络或URL是否正确"
    except requests.exceptions.Timeout:
        return "错误原因：请求超时"
    except Exception as e:
        return f"错误原因：{str(e)}"

if __name__ == "__main__":
    url = "https://jira.glenfly.com"
    user = "SummerZhou"
    pwd = "glfgpuhw"
    
    result = login_jira(url, user, pwd)
    print(result)
