const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: 'localhost',
    port: 4000,
    allowedHosts: [
        'frontend',
        'localhost',
        'spectr.dev.andyi95.com'
    ]
  }
})
