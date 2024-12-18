# alanttor模型 连接mysql 可以交互
from vanna.remote import VannaDefault
vn = VannaDefault(model='alanttor', api_key='ee3cd8d2f6a0418faf1e7391a27eff93')

import pandas as pd
import mysql.connector

def run_sql(sql: str) -> pd.DataFrame:
    cnx = mysql.connector.connect(user='root',password='jfk987jfk987',host='localhost',database='vanna_ai')
    cursor = cnx.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    columns = cursor.column_names
    df = pd.DataFrame(result, columns=columns)
    return df

vn.run_sql = run_sql
vn.run_sql_is_set = True

# vn.train(ddl="""
#     CREATE TABLE `users` (
#   `id` int NOT NULL COMMENT '用户ID',
#   `username` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '用户名',
#   `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '电子邮件',
#   `age` int DEFAULT NULL COMMENT '年龄',
#   `gender` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '性别（男/女）',
#   `city` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '城市',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户信息表';
# """)
# vn.train(ddl="""
#     INSERT INTO users (`id`, username, email, age, gender, city) VALUES
#     (1, '张三', 'zhangsan@example.com', 30, '男', '北京'),
#     (2, '李四', 'lisi@example.com', 25, '女', '上海'),
#     (3, '王五', 'wangwu@example.com', 40, '男', '广州'),
#     (4, '赵六', 'zhaoliu@example.com', 35, '女', '深圳'),
#     (5, '小明', 'xiaoming@example.com', 28, '男', '成都'),
#     (6, '小红', 'xiaohong@example.com', 45, '女', '重庆'),
#     (7, '小华', 'xiaohua@example.com', 32, '男', '天津'),
#     (8, '小丽', 'xiaoli@example.com', 27, '女', '南京'),
#     (9, '小李', 'xiaoli2@example.com', 38, '男', '武汉'),
#     (10, '小美', 'xiaomei@example.com', 33, '女', '西安');
# """)
# vn.train(question='users表中有几个用户',sql='SELECT COUNT(*) FROM users;')

allow_llm_to_see_data = True

# first_conversation_sql = vn.ask('users表中有几个用户')
# print(type(first_conversation_sql))

from vanna.flask import VannaFlaskApp
VannaFlaskApp(vn).run()






