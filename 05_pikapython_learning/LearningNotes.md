# PikaPython简介

**发展**: mimiScript --> PikaScript --> PikaPython  
**对比**: MicroPython  
**特性**:
1. 支持裸机，RAM > 4KB
2. 跨平台，可在linux、windows环境运行，方便仿真
3. 代码可读性好

# PikaPython框架

## Pika内核: C语言实现面向对象

### 1. PikaRun脚本运行层
`sys`: 最上层对象，其他对象都继承此对象，子对象可以实现自己的方法。  
`obj_run()`: 脚本运行调用接口，调用方式如下:
```c
obj_run(sys, "reboot()")
obj_run(sys, "device.led.on()")  // 继承关系: sys -- device -- led
/* 字符串为python脚本，可通过MCU串口传入 */
obj_run(sys, uartReciveBuff);
```

### 2. PikaObj对象支持层: 构造类和对象
`PikaObj`: 基类，所有类的源头。  
`New_PikaObj(Args *args)`: PikaObj的构造器函数。  
`obj_setInt(PikaObj* self, char* argPath, int64_t val)`: 为对象定义属性。  
``更多具体接口见``**PikaObj.h**

### 3. dataArgs 动态参数列表

### 4. dataMemory为dataArgs提供动态内存申请和释放