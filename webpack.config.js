const path = require('path');
const webpack = require('webpack');
const {VueLoaderPlugin} = require('vue-loader');

const entry = {
    'static/js/index': './ts/index.ts',
};

module.exports = {
    mode: 'development',
    entry,
    output: {
        filename: '[name].js',
        path: `${__dirname}`
    },

    plugins: [
        new webpack.ProgressPlugin(),
        new VueLoaderPlugin(),
    ],
    module: {
        rules: [
            {test: /\.txt$/, use: 'raw-loader'},
            {test: /\.svg$/, use: 'url-loader'},
            {test: /\.vue$/, use: 'vue-loader'},
            {
                test: /\.(ts|tsx)$/,
                loader: 'ts-loader',
                options: {
                    appendTsSuffixTo: [/\.vue$/],
                    configFile: path.resolve(__dirname, 'tsconfig.json')
                }
            },
            {test: /\.pug$/, use: 'pug-plain-loader'},
            {
                test: /\.less$/, use: ['vue-style-loader', 'css-loader', 'less-loader'],
            },
            {
                test: /\.css$/, use: ['vue-style-loader', 'css-loader'],
            }
        ]
    },

    devServer: {
        open: true
    },
    cache: true,

    resolve: {
        extensions: [".vue", ".js", ".ts"],
        alias: {
            "@ts": path.resolve(__dirname, 'ts'),
            "vue$": "vue/dist/vue.esm.js"
        }
    }
};