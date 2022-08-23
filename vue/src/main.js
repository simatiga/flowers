import { createApp } from 'vue'
import App from './App.vue'
// import router from './router'

// import Router from './router.js'       // 라우터 설정 js를 저장했던 경로를 지정.(여기서는 ./router.js)

// createApp(App).mount('#app')
const app = createApp(App)
// app.use(router);
app.mount('#app')
