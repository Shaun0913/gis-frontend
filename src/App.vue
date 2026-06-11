<template>
  <div class="app">
    <header class="header">
      <div class="title">GIS前端应用框架</div>
      <nav class="nav">
        <router-link to="/">首页</router-link>
        <router-link to="/map">OpenLayers地图</router-link>
        <router-link to="/leaflet">Leaflet地图</router-link>
        <router-link to="/maplibre">MapLibre地图</router-link>
      </nav>
    </header>
    <main class="main">
      <router-view />
    </main>
  </div>
</template>

<script setup>
// 这里只保留空的script setup即可，不用写任何代码
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  padding: 0 30px;
  background-color: #2459aa;
  color: #fff;
}

.title {
  font-size: 18px;
  font-weight: bold;
}

.nav a {
  color: #fff;
  margin: 0 15px;
  font-size: 16px;
  text-decoration: none;
}

.nav a.router-link-active {
  border-bottom: 2px solid #fff;
  padding-bottom: 5px;
}

.main {
  height: calc(100vh - 60px);
}
</style>