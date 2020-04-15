<template>
  <div>
    <div id='dd'>
      <div id="d1">
        <h1>{{ msg }}</h1>
        <div>
          <ul>
            <li v-for="(d, a) in da" :key="a">{{ d.text }}</li>
          </ul>
        </div>
      </div>
    </div>

    <div id="d2">
      <h1>{{mss}}</h1>
      <div>
          <ul>
            <li v-for="(d, a) in de" :key="a">{{ d.text }}</li>
          </ul>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "全部产品",
      mss: "最新消息",
      da: [{ text: "斗破苍穹" }, { text: "斗罗大陆" }, { text: "凡人修仙传" }],
      de: [{ text: "亏成首富从游戏开始" }, { text: "我师兄实在太稳健了" }, { text: "诡秘之主" }]
    };
  }
};
</script>

<style>
#dd{
    width: 300px;
    height: 80px;
    background-color: #fff;
}
h1 {
  size: 10px;
  color: beige;
}
#d1 {
  width: 300px;
  height: 60px;
  background-color: green;
}
#d2 {
  margin-top: 260px;
  width: 300px;
  height: 60px;
  background-color: green;
}
ul {
  border: 1px solid black;
  margin-top: 10px;
}
ul li {
  list-style: none;
}
</style>

