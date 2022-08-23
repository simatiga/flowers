import Vue from 'vue'
import VueRouter, { createRouter, createWebHistory } from 'vue-router'

//  경로에 연결할 컴포넌트 import
import page1 from './views/page1.vue'
import page2 from './views/page2.vue'

// router 사용 설정(필수)
Vue.use(VueRouter)

// export default new Router({
//     mode: 'history',  // hirtory 모드 : 자연스러운 url 기능, 지정하지 않으면 해시(#) 기호로 url 사용.
//     // routes 배열에 매핑 정보가 들어감.
//     routes: [
//         {
//             path: '/',          // 경로
//             name: '',           // 해당 경로의 이름(참고)
//             component: page1    // 이동할 컴포넌트(router-view 영역에 보여줄 컴포넌트를 지정)
//         },
//         {
//             path: './views/page1',
//             component: page1
//         },
//         {
//             path: './views/page2',
//             component: page2
//         },
//     ]
// })

const router = new VueRouter ({
        mode: 'history',  // hirtory 모드 : 자연스러운 url 기능, 지정하지 않으면 해시(#) 기호로 url 사용.
        // routes 배열에 매핑 정보가 들어감.
        routes: [
            {
                path: '/',          // 경로
                name: '',           // 해당 경로의 이름(참고)
                component: page1    // 이동할 컴포넌트(router-view 영역에 보여줄 컴포넌트를 지정)
            },
            {
                path: './views/page1',
                component: page1
            },
            {
                path: './views/page2',
                component: page2
            },
        ]
})

export default router;

// const routes = [
//             {
//                 path: '/',          // 경로
//                 name: '',           // 해당 경로의 이름(참고)
//                 component: page1    // 이동할 컴포넌트(router-view 영역에 보여줄 컴포넌트를 지정)
//             },
//             {
//                 path: './views/page1',
//                 component: page1
//             },
//             {
//                 path: './views/page2',
//                 component: page2
//             },
//         ]

// const router = createRouter({
//     history: createWebHistory(),
//     routes
// })

// export default router