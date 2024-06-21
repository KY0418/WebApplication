<template lang="pug"> 
div.whole
  div.inp_area
    div.border-solid.border-white.rounded-10px.border-5px
      div.title
        p.mb-6.mt-6.ml-6.mr-6.text-3xl.text-yellow-4.font-bold Login for the system
      div.inp_detail
        p.text-white.ml-6.mt-6 User
        div.mt-2 
          input(type="text" v-model="user_name").ml-6
        p.text-white.mt-4.ml-6 PassWord 
        div.mt-2
          input(type="text" v-model="password").ml-6.mb-4
        div.flex.mt-4.inp_footer
          button(@click="SignIn").text-black-4.bg-blue-4.text-sm.ml-4.mb-6.mr-9.border-none.rounded-5px.p-1 signIn 
          button(@click="SignUp").text-black-4.text-sm.ml-4.mb-6.mr-9.bg-green-4.border-none.rounded-5px.p-1 signup

</template>
<style lang="scss" scoped>
.whole{
  display: flex;
  width: 100%;
  min-height:100vh;
  background-color: rgb(18, 44, 73);
  justify-content: center;
  align-items: center;
}

.inp_area{
  border: 2px rgb(204, 204, 67);
  border-radius: 5px;
  flex-shrink: 0;
}

.title{
  border-bottom: solid 3px rgb(196, 171, 34);
}

.inp_detail{
  margin: auto;
}

input{
  width:80%;
  border-radius: 5px;
  border: none;
}

.input:focus{
  border: none;
}

.inp_footer{
  justify-content: right;
}
</style>
<script setup lang="ts">
import { ref } from 'vue';
import { useLoginFuncStore } from '@/stores/login';

const store = useLoginFuncStore()
const user_name = ref('')
const password = ref('')

const SignUp = async() => {
  await store.SignUp(user_name.value,password.value)
}

const SignIn = async()  => {
  await store.SignIn(user_name.value,password.value)
}


</script>