<template>
  <div>
    <h1 style="text-align: center; margin: 20px 0;">Leaflet地图示例</h1>
    <!-- 组件标签和文件名对应 -->
    <MapLeaflet ref="mapRef" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// 导入名和 components 下文件名完全一致
import MapLeaflet from '../components/MapLeaflet.vue'

const mapRef = ref(null)

onMounted(() => {
  mapRef.value?.setCenter([39.9042, 116.4074], 12)
  mapRef.value?.addMarker([39.9042, 116.4074], '北京')
})
</script>