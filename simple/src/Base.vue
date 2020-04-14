<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <div class="app-header">
      <Header/>
    </div>   
    <div class="app-content"><Content/></div>   
    <div class="app-footer"><Footer/></div>  
    <HelloComponent/>
  </div>
</template>

<script>
import HelloComponent from './HelloComponent'
import Header from './components/Header'
import Footer from './components/Footer'
import Content from './components/Content'
export default{
  data(){
    return{
      msg:'基础模板'
    };
  },
  components:{
    HelloComponent,
    Header,
    Footer,
    Content
  }
};

</script>

<style scoped>
h1{
  color: blue;
}

</style>
