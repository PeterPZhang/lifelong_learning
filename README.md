# lifelong_learning
终身学习网
#### 安装教程
```angular2
.
├── README.md
├── front_website
│   └── readme.md
└── learning_website
    ├── __init__.py
    ├── learning_website
    │   ├── __init__.py
    │   ├── apps
    │   │   ├── __init__.py
    │   │   └── hello
    │   │       ├── __init__.py
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── migrations
    │   │       │   └── __init__.py
    │   │       ├── models.py
    │   │       ├── serializers.py
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── libs
    │   │   └── __init__.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   ├── db.cfg
    │   │   ├── dev.py
    │   │   ├── prod.py
    │   │   └── public.py
    │   ├── urls.py
    │   ├── utils
    │   │   ├── __init__.py
    │   │   ├── db_operator.py
    │   │   ├── models.py
    │   │   └── return_status.py
    │   └── wsgi.py
    ├── manage.py
    └── requirements.txt
```
1. 查看django命令：django-admin 即可显示django的可用命令
2. 创建项目命令：django-admin startproject [项目名称] 若没有报错则创建项目成功
3. 查看manage.py常用命令：python manage.py 即可显示manage中的可用命令
4. 启动项目服务器并修改端口：python manage.py runserver 9999 使用9999端口来启动服务器
5. 创建命令为：python manage.py startapp [项目名称]
6. 创建完成后将应用名称添加到settings.py中的INSTALLED_APPS中完成应用的创建
7. 创建数据迁移命令：python manage.py makemigrations [应用名称] 进行数据迁移的准备步骤，输入以下命令完成数据迁移操作
8. 开始数据迁移命令：python manage.py migrate
`注：如果不输入应用名称则默认对django中的所有应用进行数据迁移操作`
9. 数据迁移完成后使用以下命令进行SQL语句查询
命令为：python manage.py sqlmigrate [应用名称] [文件id]
10. 给django创建一个超级用户命令为：python manage.py createsuperuser
11.由于项目层级架构已经重建，

#### 使用说明
1.切换至django根路径下执行 pip install -r requirements.txt 安装相应环境
2. 将django默认架构进行了更改变换，在项目文件目录下新增目录：apps、libs、utils、settings，分别汇总应用、python开发包、第三方包及工具、开发配置文件
3. settings中新增prod.py 和 dev.py 分别用于生产环境和开发环境的配置。在manage.py中进行相应的更改
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_website.settings.dev')
```
4. 在配置文件中新加apps目录的默认搜索路径
```
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```
5. 创建新应用方式变为进入到apps目录下 python3 ../../manage.py startapp [应用名称]
6. 项目现用dev.py配置文件并已开启debug，可以执行命令直接运行服务
7.由于项目结构重构及python动态语言的特点，在IDE显示中部分模块显示报红，但实际运行并无影响。只需要将django项目（后端项目文件夹非git仓库文件夹右键Mark Directory As -- Sources Root 
