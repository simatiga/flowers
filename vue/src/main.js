import { createApp } from 'vue'
import App from './App.vue'
// import router from './router'
import BootstrapVue3 from 'bootstrap-vue-3'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
// import Router from './router.js'       // 라우터 설정 js를 저장했던 경로를 지정.(여기서는 ./router.js)

// createApp(App).mount('#app')
const app = createApp(App)
app.use(BootstrapVue3)
// app.use(router);
app.mount('#app')
