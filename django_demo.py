import os
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import path

# 获取当前文件所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 模拟数据库数据
POSTS = [
    {'id': 1, 'title': 'Django 简介', 'content': 'Django 是一个高级 Python Web 框架，鼓励快速开发和简洁、实用的设计。它由经验丰富的开发者构建，解决了 Web 开发的大部分麻烦，因此你可以专注于编写应用，而无需重新发明轮子。'},
    {'id': 2, 'title': 'VS Code 调试技巧', 'content': '使用 launch.json 可以方便地调试 Python 代码。VS Code 的调试器非常强大，支持断点、变量查看、调用堆栈等功能。记得选择正确的 Python 解释器。'},
    {'id': 3, 'title': 'Python 虚拟环境', 'content': '虚拟环境可以隔离项目依赖，避免不同项目之间的包版本冲突。推荐使用 venv 模块创建虚拟环境，并在 VS Code 中激活它。'},
]

# 最小化配置
if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY='django-insecure-demo-key-12345',
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=['*'],
        # 数据库配置
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'djangodemo',      # 数据库名称，请确保在 Postgres 中创建了此数据库
                'USER': 'postgres',        # 数据库用户名
                'PASSWORD': 'password',    # 数据库密码，请修改为你自己的密码
                'HOST': 'localhost',
                'PORT': '5432',
            }
        },
        # 安装的应用
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ],
        # 中间件
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }],
        STATIC_URL='/static/',
        LOGIN_REDIRECT_URL='/',  # 登录成功后跳转到首页
    )

# 初始化 Django
import django
django.setup()

# 必须在 django.setup() 之后导入视图
from django.contrib.auth.views import LoginView, LogoutView

# 视图函数
def hello(request):
    context = {
        'title': '文章列表',
        'message': '欢迎来到 Django Demo 博客',
        'posts': POSTS
    }
    return render(request, 'index.html', context)

def post_detail(request, post_id):
    # 查找对应 ID 的文章
    post = next((p for p in POSTS if p['id'] == post_id), None)
    if post is None:
        raise Http404("文章不存在")
    
    return render(request, 'detail.html', {'post': post})

# URL 路由
urlpatterns = [
    path('', hello, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]

# 运行服务器
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import sys
    # 如果没有参数，默认运行 runserver
    if len(sys.argv) == 1:
        sys.argv += ['runserver', '8000']
    execute_from_command_line(sys.argv)
