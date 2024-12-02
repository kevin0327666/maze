# 迷宫生成器

这是一个基于 Flask 的在线迷宫生成器，可以生成随机的迷宫并提供可视化界面。

## 功能特点

- 支持自定义迷宫大小（5x5 到 50x50）
- 支持自定义单元格大小（10-40像素）
- 使用深度优先搜索（DFS）算法生成迷宫
- 清晰标识起点（绿色）和终点（红色）
- 实时生成和显示
- 响应式界面设计

## 技术栈

- 后端：Python Flask
- 前端：HTML5, JavaScript
- 可视化：Canvas

## 安装说明

1. 克隆项目到本地：
```bash
git clone https://github.com/kevin0327666/maze.git
cd maze
```

2. 创建并激活虚拟环境（可选）：
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 运行方法

1. 启动服务器：
```bash
python main.py
```

2. 在浏览器中访问：
```
http://localhost:5000
```

## 使用说明

1. 调整迷宫参数：
   - 使用"迷宫大小"输入框设置迷宫的网格数（5-50）
   - 使用"单元格大小"输入框设置每个单元格的像素大小（10-40）

2. 生成迷宫：
   - 点击"生成新迷宫"按钮生成新的迷宫
   - 每次修改参数后会自动重新生成迷宫

3. 迷宫说明：
   - 绿色方块：起点
   - 红色方块：终点
   - 黑色方块：墙
   - 白色方块：通道

## 注意事项

- 建议使用现代浏览器（Chrome、Firefox、Edge等）访问
- 迷宫大小会影响生成速度，较大的迷宫可能需要更多时间生成
- 确保 5000 端口未被其他程序占用

## 开发者

- Kevin

## 许可证

MIT License