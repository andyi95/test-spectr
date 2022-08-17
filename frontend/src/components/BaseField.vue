<template>
<div class="col-md-6 mt-2">
  <input type="text" :placeholder="placeholder" class="form-control">
</div>
</template>

<script>
export default {
  name: "BaseField",
  props: {
    placeholder: String,
  }
}
</script>

<style scoped>

</style>
