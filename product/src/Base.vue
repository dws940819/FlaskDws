<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <Slide/>
    
    <Title/>
    <Prati/>
    
  </div>
</template>

<script>
import Title from './Title'
import Slide from './Slide'
import Prati from './Prati'
export default{
  data(){
    return{
      msg:'Vue单文件作业'
    };
  },
  components:{
    Title,
    Slide,
    Prati,
  }
};

</script>

<style scoped>
*{
  margin: 0 auto;
}
h1{
  color: rgb(20, 139, 207);
}

</style>
