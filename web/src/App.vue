<template lang="pug">
Header.head
RouterView
</template>
<style lang="scss" scoped>
.head{
  position: fixed;
  z-index: 2;
}
</style>
<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Header from './layouts/Header.vue';
</script>
