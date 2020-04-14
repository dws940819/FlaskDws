<template>
    <h1>
    HelloComponent{{ msg}}
    </h1>
</template>

<script>
export default {
    name:"HelloComponent",
    data() {
        return {
            msg:'热烈欢迎！'
        }
    },
}
</script>

<style>
h1{
    color: red;
}

</style>

