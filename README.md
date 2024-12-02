# DAG可视化管理系统

这是一个基于Flask的DAG（有向无环图）可视化和管理系统，允许用户通过Web界面创建、编辑和管理DAG图。

## 功能特点

- 可视化DAG图的创建和编辑
- 实时环检测，防止创建循环依赖
- RESTful API支持
- 支持边的添加和删除
- 直观的Web界面

## 技术栈

- 后端：Python Flask
- 前端：HTML, JavaScript
- API：RESTful

## 安装说明

1. 克隆项目到本地：
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 运行方法

1. 启动Flask服务器：
```bash
python main.py
```

2. 在浏览器中访问：
```
http://localhost:5000
```

## API接口说明

### 获取DAG数据
- 端点：`GET /api/dag`
- 返回：当前DAG的节点和边数据

### 更新DAG数据
- 端点：`POST /api/dag`
- 功能：更新整个DAG图
- 请求体：包含nodes和edges的JSON数据
- 说明：会自动进行环检测，如存在环则返回错误

### 删除边
- 端点：`DELETE /api/dag/edge`
- 功能：删除指定的边
- ��求体：包含source和target的JSON数据

## 注意事项

- 系统会自动检测并防止创建带有环的图
- 所有的更改都会实时保存
- 运行时请确保5000端口未被占用 