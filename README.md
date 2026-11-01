# Python 小项目集

一个学生管理系统，加三个小脚本。全部使用 Python 标准库，无第三方依赖。

## 项目

### 1. 学生管理系统 · `student_management/`

命令行程序，面向对象实现，支持增 / 删 / 改 / 查，数据持久化到文本文件。

- 分三层：`Student`（实体）、`StudentMS`（业务 + 存储）、`MainProgram`（界面）
- 数据保存在运行时生成的 `stu.txt`

```bash
cd student_management
python main.py
```

菜单：

```
1. 添加学生   2. 修改学生   3. 删除学生
4. 查询学生   5. 显示全部   0. 退出系统
```

### 2. 抽卡模拟器 · `scripts/模拟抽卡手游修bug后.py`

终端版抽卡模拟（原石 + 抽卡券 + 保底机制）。

- 原石 / 抽卡券资源管理
- 小保底、大保底计数
- 抽卡历史记录

```bash
python "scripts/模拟抽卡手游修bug后.py"
```

### 3. 闰年检测 · `scripts/判断是否为闰年.py`

输入年份，判断是否为闰年。输入 `9999` 退出。

```bash
python "scripts/判断是否为闰年.py"
```

### 4. 字符串编码 · `scripts/小脚本.py`

把英文字母转换成 ASCII 序号（a=1, b=2 …），并支持解码还原。

```bash
python scripts/小脚本.py
```

## 环境

- Python 3.10+
- 无第三方依赖

## 目录结构

```text
python-projects/
├── student_management/
│   ├── main.py             菜单与主循环
│   ├── studentms.py        业务逻辑 + 文件读写
│   └── student.py          学生实体
└── scripts/
    ├── 模拟抽卡手游修bug后.py
    ├── 判断是否为闰年.py
    └── 小脚本.py
```

## 说明

个人学习项目，代码以练习为主，不追求工程规范。
