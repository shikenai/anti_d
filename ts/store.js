import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        count:5,
        selected_id: -1,
        selected_group:"",
        selected_width: -1,
        selected_height: -1,
        changing_id: -1,
        selected_text: "",
    },
    getters:{
        doubleCount: state => state.count * 2,
        tripleCount: state => state.count * 3,
    },
    mutations:{
        increment(state, number){
            state.count += number
        },
        changeSelectId(state, number){
            state.selected_id = number
        },
        changeSelectedGroup(state, group){
            state.selected_group = group
        },
        changeSelectedWidth(state, width){
            state.selected_width = width
        },
        changeSelectedHeight(state, height){
            state.selected_height = height
        },
        inputWidth(state, width){
            state.selected_width = width
        },
        changeSelectedText(state, text){
            state.selected_text = text
        }
    },
    actions:{
        increment(context, number){
            context.commit('increment', number);
        }
    }
})