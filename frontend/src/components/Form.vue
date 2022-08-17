<template>
  <div class="container">Форма обратной связи</div>
  <div class="col-md-8 p-5">
    <div v-if="errors">
    <div class="alert alert-danger" v-for="error in errors" v-bind:key="error.id">
      {{ error }}</div></div>
    <div class="col-md-6">
    <input type="text" v-model="email" placeholder="email" class="form-control"/></div>
    <div class="col-md-6">
      <input type="text" v-model="phone" placeholder="phone" class="form-control"/></div>
    <div class="col-md-6"><textarea v-model="message" placeholder="Сообщение" class="form-control"/></div>
    <div class="col-md-6">
      <button @click="submitData" class="btn btn-primary">Отправить</button></div>
    </div>
  <div v-if="items">
    <div class="card mb-3 mt-1" v-for="item in items" :key="item.id">
      <div class="card-body">
          <p>Email: {{item.email}} </p>
          <p>Номер телефона: {{item.phone}}</p>
          <p>Сообщение: {{item.message}}</p>
        <div class="col-md-6">
          <button @click="deleteItem(item.id)" class="btn btn-danger">Удалить</button>
        </div>
      </div>
      </div>
    </div>
</template>

<script>
import {api} from "@/helpers/api";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Form',
  data() {
    return {
      items: [],
      email: null,
      phone: null,
      message: null,
      errors: []
    }
  },
  mounted() {
    this.updateItems()
  },
  methods: {
    submitData(){
      api.post(
          'form/',
          {'email': this.email, 'phone': this.phone, 'message': this.message}
      ).then(this.updateItems).catch(function (e) {
        console.log(e)
      })
    },
    updateItems(){
      api.get('form/').then(response => {
        this.items = response.data
          }
      ).catch(e => {
        console.log(e)
      })
    },
    deleteItem(item_id){
      api.delete('form/' + item_id).then(this.updateItems)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin-block: 10pt;
}
</style>
