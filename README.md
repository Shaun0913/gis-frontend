# Vue3 + Leaflet 地图演示项目
基于 Vue3 + script setup + Leaflet 实现 Web 地图功能。

## 技术栈
- Vue 3 + Vite
- Leaflet 地图框架

## 功能介绍
1. 地图初始化，使用国内高德瓦片服务
2. 支持外部切换地图中心点
3. 支持添加点位标记与弹窗
4. 组件完整销毁，防止内存泄漏

## 运行方式
1. 安装依赖
pnpm install

2. 启动项目
pnpm run dev

## 优化点
- 使用 ref 绑定容器，避免ID冲突
- 增加参数校验与异常捕获
- 完善地图销毁逻辑