class LoginModule:
    def __init__(self):
        # 模拟用户数据库，实际项目中应该使用真实数据库
        self.users = {
            "admin": "admin123",
            "user1": "user123"
        }
    
    def login(self, username, password):
        """
        用户登录验证
        :param username: 用户名
        :param password: 密码
        :return: 登录结果（布尔值）和消息
        """
        if not username or not password:
            return False, "用户名和密码不能为空"
        
        if username in self.users:
            if self.users[username] == password:
                return True, f"欢迎回来，{username}！"
            else:
                return False, "密码错误"
        else:
            return False, "用户名不存在"
    
    def register(self, username, password):
        """
        用户注册
        :param username: 用户名
        :param password: 密码
        :return: 注册结果（布尔值）和消息
        """
        if not username or not password:
            return False, "用户名和密码不能为空"
        
        if len(username) < 3:
            return False, "用户名长度不能少于3个字符"
        
        if len(password) < 6:
            return False, "密码长度不能少于6个字符"
        
        if username in self.users:
            return False, "用户名已存在"
        
        self.users[username] = password
        return True, f"注册成功，欢迎 {username}！"
    
    def get_all_users(self):
        """
        获取所有用户（用于测试和管理）
        :return: 所有用户名列表
        """
        return list(self.users.keys())


# 测试代码
if __name__ == "__main__":
    login_module = LoginModule()
    
    # 测试登录
    print("测试登录功能：")
    print(login_module.login("admin", "admin123"))  # 正确登录
    print(login_module.login("admin", "wrongpass"))  # 密码错误
    print(login_module.login("nonexistent", "password"))  # 用户不存在
    print(login_module.login("", "password"))  # 空用户名
    print(login_module.login("admin", ""))  # 空密码
    
    # 测试注册
    print("\n测试注册功能：")
    print(login_module.register("newuser", "newpass123"))  # 成功注册
    print(login_module.register("newuser", "newpass123"))  # 用户名已存在
    print(login_module.register("nu", "password"))  # 用户名太短
    print(login_module.register("newuser2", "short"))  # 密码太短
    
    # 测试新用户登录
    print("\n测试新用户登录：")
    print(login_module.login("newuser", "newpass123"))  # 新用户登录成功
    
    # 查看所有用户
    print("\n所有用户：")
    print(login_module.get_all_users())