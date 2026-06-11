<template>
  <div id="map-container" style="width: 100%; height: 600px;"></div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

let map = null

onMounted(() => {
  map = L.map('map-container').setView([39.9042, 116.4074], 10)

  // 👇 换成高德地图瓦片地址（国内访问更稳定）
  L.tileLayer('https://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}', {
    attribution: '&copy; <a href="https://ditu.amap.com/">高德地图</a> contributors',
    subdomains: ['1', '2', '3', '4']
  }).addTo(map)
})

const setCenter = (latlng, zoom) => {
  if(map) map.setView(latlng, zoom)
}

const addMarker = (latlng, text) => {
  if(map) L.marker(latlng).addTo(map).bindPopup(text).openPopup()
}

onUnmounted(() => {
  if (map) {
    map.remove()
    map = null
  }
})

defineExpose({
  setCenter,
  addMarker
})
</script>

<style scoped>
#map-container {
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
</style>