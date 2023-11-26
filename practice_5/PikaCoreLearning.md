# Pika内核源码学习

## 学习准备
1. 源码位置: PikaPython/src
2. 使用编辑器: 
    + Source Insight 4.0: 查看Pika内核代码结构、跳转和查看函数调用链功能较为方便
    + VSCode: 查看整个PikaPython工程

## 源码分析

### 运行流程

#### 运行预编译python字节码：
1. `main`函数中调用`pikascript-api`中`pikaScript.c`的`pikaScriptInit`函数
2. `pikaScriptInit`函数调用`PikaObj.c`的`obj_runModule`函数，并通过`obj_linkLibrary`传入字节码
3. `obj_runModule`函数调用`PikaVM.c`的`pikaVM_runByteCode_ex`函数
4. 最终会进入`PikaVM.c`的`__pikaVM_runByteCodeFrameWithState`函数进行处理，而其又通过`pikaVM_runInstructUnit`函数
   处理每个python字节码指令，具体支持字节码指令见文件`__instruction_table.h`

函数调用链如下：
| File | Function |
| ---- | -------- |
| main.c | PikaObj *pikaScriptInit(void) |
| PikaObj.c | int obj_runModule(PikaObj* self, char* module_name) |
| PikaVM.c | pikaVM_runByteCode_ex |
| PikaVM.c | `__pikaVM_runByteCodeFrameWithState` |
| PikaVM.c | pikaVM_runInstructUnit |

#### 运行python源码字符串：
1. 调用`PikaObj.c`的`obj_run`函数，并传入`PikaObj`和python字符串
2. `obj_run`函数调用`PikaVM.c`的`pikaVM_run`函数交给PikaVM处理，在PikaVM中生成字节码

函数调用链如下：
| File | Function |
| ---- | -------- |
| xxx.c | 调用`obj_run`的函数 |
| PikaObj.c | VMParameters* obj_run(PikaObj* self, char* cmd) |
| PikaVM.c | pikaVM_run --> pikaVM_run_ex |
| PikaParser.c | `pika_lines2Bytes`生成字节码 |
| PikaVM.c | `__pikaVM_runByteCodeFrameWithState`运行字节码 |
| PikaVM.c | pikaVM_runInstructUnit |

### 内核结构

#### 核心文件：
| File | 功能 |
| ---- | -------- |
| **PikaObj.c** | 1. 提供构造`PikaObj`的接口 2. 提供运行python和python字节码的接口 |
| **data_xxx.c**, TinyObj.c, BaseObj.c | 为`PikaObj`提供类和对象中数据的支持 |
| **PikaVM.c** | 解析并运行传入的python字节码 |
| **PikaParser.c** | 将python字符串解析为字节码 |
| **PikaCompiler.c** | 提供运行时编译python为字节码的功能，以及文件相关操作，*但程序中直接使用python字节码能够提高效率，故预编译操作可以提前（rust脚本编译或上位机下发前编译* |
| **PikaPlatform.c** | Pika提供的C语言库函数 |
| **pika_config_valid.h** | Pika配置选项头文件 |
| pika_adapter_old_api.h | Pika兼容老版本api头文件 |
| pika_adapter_mpy.h | Pika兼容micropython的api头文件 |
| pika_adapter_rtt.h | Pika兼容RT-Thread的api头文件 |
