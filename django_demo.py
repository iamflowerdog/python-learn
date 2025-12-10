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
settings.configure(
    DEBUG=True,
    SECRET_KEY='django-insecure-demo-key-12345',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }],
)

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
    path('', hello),
    path('post/<int:post_id>/', post_detail),
]

# 运行服务器
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    import sys
    sys.argv = ['django_demo.py', 'runserver', '8000']
    execute_from_command_line(sys.argv)
