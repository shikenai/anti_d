import Vue from "vue";
import mybutton from './components/mybutton.vue';
import mainindex from './components/mainindex.vue';
import store from './store.js'
window.onload = () => {
    const v = new Vue({
        store: store,
        components:{
            'mainindex': mainindex,
            'mybutton': mybutton
        },
        data:{
            message: 'hello'
        },
        methods: {
            // location_change(ixy){
            //     console.log('main.ts')
            //     console.log(ixy)
            // }
        },
        delimiters: ["[[", "]]"]
    }).$mount('#root')
}