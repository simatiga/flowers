const { defineConfig } = require('@vue/cli-service')
// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin

module.exports = {
    publicPath: '',
    outputDir: './docs',
    lintOnSave:false,
    // configureWebpack: {
    //     plugins: [new BundleAnalyzerPlugin()]
    //   }
}
