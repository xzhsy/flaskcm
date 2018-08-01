#引入系统设置部分
from WebProject.setting import REPOSITORY_SETTINGS_Han
from WebProject.models.factory import create_repository

# 所有路由文件共用的仓库代理
repository = create_repository(REPOSITORY_SETTINGS_Han)

# 导入路由处理集合
from WebProject.route import basic
from WebProject.route import manager
from WebProject.route import user
from WebProject.route import redis
from WebProject.route.utils import xlsRoute
from WebProject.route.utils import upload
from WebProject.route.api import xlsApi
