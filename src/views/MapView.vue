<template>
  <div class="map-page">
    <div id="map" class="map-box"></div>
  </div>
</template>

<script setup>
import { onMounted, provide } from 'vue';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';
import 'ol/ol.css';

let map = null;
let mapView = null;

onMounted(() => {
  map = new Map({
    target: 'map',
    layers: [
      new TileLayer({
        // 改用高德地图瓦片（国内可稳定访问）
        source: new XYZ({
          url: 'https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
          tilePixelRatio: 1
        })
      })
    ],
    view: new View({
      // 注意：OpenLayers默认使用EPSG:3857投影，但坐标要按[经度, 纬度]顺序写
      center: [106.5715, 29.4892], // 重庆交通大学南岸校区
      zoom: 14,
      projection: 'EPSG:4326' // 直接使用经纬度投影，避免坐标转换问题
    })
  });

  mapView = map.getView();
  provide('mapView', mapView);
});
</script>

<style scoped>
.map-page {
  width: 100%;
  height: 100%;
}
.map-box {
  width: 100%;
  height: 100%;
}
</style>