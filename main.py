import os
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 迷宫生成相关代码
class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1 for x in range(width)] for y in range(height)]
        self.start = (1, 1)  # 起点坐标
        self.end = (width-2, height-2)  # 终点坐标
        
    def generate(self):
        # 从起点开始生成迷宫
        start_x, start_y = self.start
        self.maze[start_y][start_x] = 0
        self._generate_path(start_x, start_y)
        
        # 确保终点可达
        end_x, end_y = self.end
        self.maze[end_y][end_x] = 0
        # 确保终点周围至少有一条路径
        if self.maze[end_y-1][end_x] == 1 and self.maze[end_y+1][end_x] == 1 and \
           self.maze[end_y][end_x-1] == 1 and self.maze[end_y][end_x+1] == 1:
            # 随机选择一个方向打通
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            dx, dy = random.choice(directions)
            self.maze[end_y + dy][end_x + dx] = 0
        
        return {
            'maze': self.maze,
            'start': self.start,
            'end': self.end
        }
    
    def _generate_path(self, x, y):
        # 四个方向：上、右、下、左
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if (0 < new_x < self.width-1 and 
                0 < new_y < self.height-1 and 
                self.maze[new_y][new_x] == 1):
                
                # 打通路径
                self.maze[new_y][new_x] = 0
                # 打通中间的墙
                self.maze[y + dy//2][x + dx//2] = 0
                
                self._generate_path(new_x, new_y)

@app.route('/')
def index():
    return render_template('maze.html')

@app.route('/maze')
def maze_page():
    return render_template('maze.html')

@app.route('/api/generate_maze', methods=['POST'])
def generate_maze():
    data = request.json
    size = data.get('size', 25)  # 如果没有提供size参数，默认使用25
    size = max(5, min(50, size))  # 限制大小在5-50之间
    generator = MazeGenerator(size, size)
    maze_data = generator.generate()
    return jsonify(maze_data)

if __name__ == '__main__':
    app.run(debug=True)

