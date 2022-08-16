import { createApp } from 'vue'
import {BootstrapVue3} from "bootstrap-vue-3";
import App from './App.vue'

const app = createApp(App)
app.use(BootstrapVue3)
app.mount('#app')
