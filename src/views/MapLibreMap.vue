<template>
  <div class="map-container">
    <div id="maplibre-map"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

onMounted(() => {
  const map = new maplibregl.Map({
    container: 'maplibre-map',
    style: {
      version: 8,
      sources: {
        'amap': {
          type: 'raster',
          tiles: [
            'https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}'
          ],
          tileSize: 256,
          attribution: '&copy; 高德地图'
        }
      },
      layers: [
        {
          id: 'amap-tiles',
          type: 'raster',
          source: 'amap',
          minzoom: 0,
          maxzoom: 18
        }
      ]
    },
    center: [106.5715, 29.4892], // 重庆交通大学南岸校区
    zoom: 15
  });

  map.on('load', () => {
    console.log('✅ 高德地图瓦片加载成功');
    // 添加中心标记点
    new maplibregl.Marker()
      .setLngLat([106.5715, 29.4892])
      .addTo(map);
  });

  map.on('error', (e) => {
    console.error('❌ 地图加载错误:', e);
  });
});
</script>

<style scoped>
.map-container {
  width: 100%;
  height: calc(100vh - 60px);
  position: relative;
}

#maplibre-map {
  width: 100%;
  height: 100%;
}
</style>