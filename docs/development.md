# 开发文档

## 环境要求
- Python 3.11.6
- pip (最新版本)
- virtualenv 或 venv

## 开发环境设置
1. 创建虚拟环境
   ```bash
   python3 -m venv IP_venv
   ```

2. 激活虚拟环境
   ```bash
   # macOS/Linux
   source IP_venv/bin/activate
   # Windows
   .\IP_venv\Scripts\activate
   ```

3. 安装开发依赖
   ```bash
   pip install -r requirements.txt
   # 或
   pip install -e ".[dev]"
   ```

## 项目结构说明
- `src/core/file_utils.py`: 提供文件操作相关的核心功能
- `src/main.py`: 程序主入口
- `tests/`: 包含所有测试用例
- `examples/`: 包含示例代码

## 开发指南

### 开发流程
1. 代码风格
   - 遵循 PEP 8 规范
   - 使用有意义的变量名和函数名
   - 添加适当的注释和文档字符串

2. 测试驱动开发
   - 先写测试，后写实现
   - 运行测试：`pytest tests/`
   - 确保测试覆盖率

3. Git 工作流
   - 创建功能分支进行开发
   - 提交前进行代码审查
   - 保持提交信息清晰明确

## 版本历史

### v0.1.0 (开发中)
- 初始项目结构搭建
- 基础文件创建

## TODO 列表
- [ ] 完善项目文档
- [ ] 添加核心功能模块
- [ ] 编写单元测试
- [ ] 配置 CI/CD 流程

## 问题追踪
在这里记录开发过程中遇到的问题和解决方案。

## API 文档
在这里添加项目 API 的详细说明。 