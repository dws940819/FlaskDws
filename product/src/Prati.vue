<template>
    <div>
        <div id="xq1">
            <h3>{{ msg }}</h3>
            <div>
          <ul>
            <li v-for="(d, a) in da" :key="a">{{ d.text }}</li>
          </ul>
        </div>
        </div>

        <div id='xq2'>
            <h3 id='h33'>{{ mss }}</h3>
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
      msg: "作者简介",
      mss: "最新影视剧",
      da: [{ text: "天蚕土豆" }, { text: "唐家三少" }, { text: "妄语" }],
      de: [{ text: "择天记" }, { text: "步步惊心" }, { text: "诛仙" }]
    };
  }
};
</script>


<style scoped>
#xq1{
    float: right;
    margin-top: 0;
    margin-right: 600px;
    width: 300px;
    height: 160px;
    background-color: rgb(61, 168, 136);
}
#xq2{
    float: right;
    margin-top: 20px;
    margin-right: 600px;
    width: 300px;
    height: 160px;
    background-color: rgb(61, 168, 136);
}
</style>

