<template>
  <div class="black-bg" v-if="modalWinOpen==true">
      <div class="white-bg">
          <h4>상세 페이미임</h4>
          <p>상세 페이지 내용</p>
        <button @click="modalWinOpen = false">닫기</button>
      </div>
  </div>

  <div class="menu">
      <!-- <a>Home</a>
      <a>Products</a>
      <a>About</a>  -->
      <a v-for="a in 메뉴들" :key="a">{{a}}</a>
      <!-- <a v-for="(a, i) in 메뉴들" :key="a">{{i}}. {{a}}</a> -->
  </div>
  <div>
      원룸샵m
  </div>
  <!-- <div>
      <img :src=원룸들[0].image class="room-img">
      <h4 :style="스타일" @click="modalWinOpen=true">{{원룸들[0].title}}</h4>
      <p>{{원룸들[0].price}}원</p>
  </div>
  <div>
      <img :src=원룸들[1].image class="room-img">
      <h4 :style="스타일" @click="modalWinOpen=true">{{원룸들[1].title}}</h4>
      <p>{{원룸들[1].price}}원</p>
  </div> -->
  <div v-for="(a,i) in 원룸들" :key="i">
      <img :src=원룸들[i].image class="room-img">
      <h4 :style="스타일" @click="modalWinOpen=true">{{원룸들[i].title}}</h4>
      <p>{{원룸들[i].price}}원</p>
  </div>

</template>

<script>
import data from './data/oneroom.js';


export default {
  name: 'App',
  data() {
    return {
      // data 보관함. (중요 변수들 여기 다 만들어놓으면 됨)
      // object 자료형으로.
      // {자료이름 : 자료내용}
        products : ['역삼동원룸', '천호동원룸', '마포구원룸'],
        prices : [13, 23, 29],
        메뉴들 : ['Home', 'Shop', 'About'],
        신고수 : [0, 0, 0],
        modalWinOpen : false,
        원룸들 : data,
    }
  },

  methods: {
    increase(i){
      this.신고수[i]++;
    }
  },
  
  components: {
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu{
  background: darkslateblue;
  padding:15px;
  border-radius:5px;
}

.menu a {
  color: white;
  padding: 10px;
}

.room-img {
  width: 60%;
  margin-top: 40px;
}

.black-bg {
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}

.white-bg {
  width: 100%; 
  background: white;
  border-radius: 8px;
  padding: 20px;
}
</style>
