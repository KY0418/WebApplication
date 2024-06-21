import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useToast } from 'vue-toast-notification'

const BASEURL = import.meta.env.VITE_BASE_URL
const toast = useToast()
const msgList = ['名前を入力してください','パスワードを入力してください','名前とパスワードを入力してください']

export const useLoginFuncStore = defineStore({
  id: 'loginfunc',
  state: () =>({
    data: ref(),
    validationCheck: (name:string,pass:string): boolean => {
      if(name == '' && pass == ''){
        toast.error(`${msgList[2]}`,{
          position:"top"
        })
        return false
      }else if(name == '' ){
        toast.error(`${msgList[0]}`,{
          position:"top"
        })
        return false
      }else if(pass == ''){
        toast.error(`${msgList[1]}`,{
          position:"top"
        })
        return false
      }
      return true
    },
  }),
  actions:{
    async SignUp(name:string,pass:string): Promise<void> {
      if(this.validationCheck(name,pass) == false){
        return
      }
      const response = await axios.post(`${BASEURL}signup`,{
        user_name: name,
        user_pass: pass,
      }).then((response) =>{
        if(response.status == 200){
          toast.success("SignUp Successful",{
            position:"top"
          })
        }
      }).catch((error)=> {
          toast.error(`${error.responsedata.data.detail}`,{
            position:"top"
          })
        })
      },
    async SignIn(name:string,pass:string): Promise<void> {
      const response = await axios.post(`${BASEURL}/signin`,{
        user_name: name,
        user_pass: pass,
      }).then((response) => {
        if(response.status == 200){
          toast.success("Login Successful",{
            position:"top"
          })
        }
      }).catch((error) => {
        toast.error(`${error.responsedata.data.detail}`,{
          position:"top"
        })
      })
    }
    } 

})