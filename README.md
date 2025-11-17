# rosmaster\_lib

A Python library for controlling Rosmaster series robots, supporting motor control, sensor data reading, servo operations, and more.

## 概述

`rosmaster_lib` 提供简洁的接口，通过串口通信与 Rosmaster 系列机器人（如 X3、X3-Plus、X1、R2 等型号）交互。该库封装了底层通信协议，让开发者无需关注硬件细节，专注于高层机器人控制逻辑。

## 安装指南（Installation）


### 本地安装（开发 / 离线场景）

下载源码后，进入项目根目录执行：


```
cd rosmaster_lib  # 进入包含 setup.py 的目录

pip install .
```

### 依赖库（Dependencies）

核心依赖为串口通信库，自动安装：

```
pip install pyserial  # 若安装失败，手动执行此命令
```

## 快速开始（Quick Start）

以下示例演示基础控制功能，适用于大多数 Rosmaster 机器人型号。

> Note: You need a robot (e.g., Rosmaster-X3) from Yahboom to test the lib. 




## 核心功能说明（Core Features）

### 1. 初始化参数（Initialization Parameters）

| 参数名        | 类型    | 默认值   | 说明                         |
| ---------- | ----- | ----- | -------------------------- |
| `com`      | str   | 无     | 串口设备路径（必须指定）               |
| `car_type` | int   | 1     | 机器人型号（1=X3，2=X3-Plus，3=X1） |
| `delay`    | float | 0.002 | 指令发送延迟（避免串口拥堵）             |
| `debug`    | bool  | False | 开启调试日志（打印发送 / 接收的原始数据）     |

### 2. 设备控制（Device Control）

| 方法名                                      | 说明                                 |
| ---------------------------------------- | ---------------------------------- |
| `create_receive_threading()`             | 开启数据接收线程（读取传感器数据必需）                |
| `set_auto_report_state(enable, forever)` | 开启 / 关闭自动数据上报（`forever=True` 持续上报） |
| `set_beep(on_time)`                      | 控制蜂鸣器（0 = 关闭，1 = 常响，≥10 = 定时）      |

### 3. 舵机控制（Servo Control）

| 方法名                                 | 说明                            |
| ----------------------------------- | ----------------------------- |
| `set_pwm_servo(servo_id, angle)`    | 控制单个 PWM 舵机（ID：1-4，角度：0-180°） |
| `set_pwm_servo_all(s1, s2, s3, s4)` | 同时控制 4 路 PWM 舵机（s1-s4 为角度）    |
| `set_uart_servo(servo_id, angle)`   | 控制 UART 舵机（更高精度，ID：1-254）     |

### 4. 运动控制（Motion Control）

| 方法名                         | 说明                               |
| --------------------------- | -------------------------------- |
| `car_run(speed, angle)`     | 简化运动控制（速度：-100\~100，角度：-90\~90°） |
| `set_motor(m1, m2, m3, m4)` | 单独控制 4 个电机（速度：-100\~100）         |
| `set_motion(vx, vy, vz)`    | 三维速度控制（vx：前后，vy：左右，vz：旋转）        |

### 5. 传感器数据读取（Sensor Data）

| 方法名                     | 返回值说明                                           |
| ----------------------- | ----------------------------------------------- |
| `get_imu_att()`         | 姿态角字典：`{"roll": 0.0, "pitch": 0.0, "yaw": 0.0}` |
| `get_battery_voltage()` | 电池电压（单位：V）                                      |
| `get_encoder()`         | 4 个电机编码器计数：`(m1, m2, m3, m4)`                   |
| `get_mpu_raw()`         | MPU9250 原始数据（加速度、陀螺仪、磁力计）                       |

### 6. RGB 灯控制（RGB LED Control）

| 方法名                                   | 说明                                     |
| ------------------------------------- | -------------------------------------- |
| `set_colorful_lamps(led_id, r, g, b)` | 控制单个 LED（ID：0-13，0xFF = 所有灯；RGB：0-255） |
| `set_rgb_effect(effect, speed)`       | 设置 LED 特效（effect：0-7，speed：1-10）       |

## 注意事项（Notes）

1. **串口权限问题**：

* Linux/macOS 系统需赋予串口权限：

```
sudo chmod 777 /dev/ttyUSB0  # 替换为你的串口路径
```

* 若权限不足，可将用户添加到 `dialout` 组（永久生效）：

```
sudo usermod -aG dialout \$USER
```

1. **串口路径查找**：

* Linux：`ls /dev/ttyUSB*` 或 `ls /dev/ttyTHS*`

* Windows：设备管理器 → 端口（COM）

* macOS：`ls /dev/tty.usbserial*`

1. **使用规范**：

* 调用控制指令前，必须先执行 `create_receive_threading()`

* 电机速度和舵机角度超出范围时，库会自动截断到安全值

* 长时间不使用时，调用 `del rm` 释放串口资源

1. **兼容性**：

* 支持 Python 3.7+

* 兼容 Rosmaster 固件 V3.3.9 及以上版本

## 版本历史（Version History）

* v0.1.0：初始版本，支持核心功能（电机、舵机、传感器、LED）

* v0.1.1：新增 UART 舵机支持，修复串口通信稳定性问题

* v0.1.2：优化传感器数据读取延迟，新增多型号机器人适配

## 许可证（License）

MIT License（详见 LICENSE 文件）

## 问题反馈与贡献（Issues & Contributions）

* 报告 Bug 或需求：[GitHub Issues](https://github.com/DaojiePENG/rosmaster_lib/issues)

* 欢迎提交 Pull Request 完善功能

## 联系方式（Contact）

若有技术问题，可通过以下方式联系：

* GitHub：[Daojie PENG](https://github.com/DaojiePENG)

* Email：Daojie.PENG@qq.com

## 鸣谢（Thanks）

[亚博智能科技有限公司](https://www.yahboom.com/)