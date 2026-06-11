<template>
  <div class="app-container">
    <!-- 顶部导航栏 -->
    <header class="header">
      <h1 class="title">GIS 实验应用框架</h1>
      <div class="header-actions">
        <button class="header-btn">图层管理</button>
        <button class="header-btn">空间分析</button>
        <button class="header-btn">工具</button>
      </div>
    </header>

    <div class="main-content">
      <!-- 左侧边栏 -->
      <aside class="sidebar">
        <div class="sidebar-section">
          <h3>图层列表</h3>
          <div class="layer-item">
            <input type="checkbox" checked /> 基础底图
          </div>
          <div class="layer-item">
            <input type="checkbox" /> 道路图层
          </div>
          <div class="layer-item">
            <input type="checkbox" /> POI 点图层
          </div>
        </div>
        <div class="sidebar-section">
          <h3>地图工具</h3>
          <button class="tool-btn" @click="zoomIn">放大</button>
          <button class="tool-btn" @click="zoomOut">缩小</button>
          <button class="tool-btn" @click="resetCenter">定位</button>
        </div>
      </aside>

      <!-- 地图主区域 -->
      <main class="map-container">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import { inject } from 'vue';

const mapView = inject('mapView', null);

// 地图放大
const zoomIn = () => {
  if (mapView) {
    mapView.animate({ zoom: mapView.getZoom() + 1, duration: 250 });
  }
};

// 地图缩小
const zoomOut = () => {
  if (mapView) {
    mapView.animate({ zoom: mapView.getZoom() - 1, duration: 250 });
  }
};

// 重置定位到 重庆交通大学
const resetCenter = () => {
  if (mapView) {
    mapView.animate({
      center: [106.5715, 29.4892],
      zoom: 14,
      duration: 500
    });
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  height: 60px;
  background-color: #2c3e50;
  color: white;
}
.header-actions {
  display: flex;
  gap: 10px;
}
.header-btn {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  background-color: #34495e;
  color: white;
  cursor: pointer;
}
.main-content {
  display: flex;
  flex: 1;
  overflow: hidden;
}
.sidebar {
  width: 240px;
  background-color: #ecf0f1;
  padding: 15px;
  overflow-y: auto;
}
.sidebar-section {
  margin-bottom: 20px;
}
.layer-item {
  margin: 8px 0;
}
.tool-btn {
  display: block;
  width: 100%;
  margin: 5px 0;
  padding: 8px;
  border: none;
  border-radius: 4px;
  background-color: #3498db;
  color: white;
  cursor: pointer;
}
.map-container {
  flex: 1;
  background-color: #bdc3c7;
}
</style>