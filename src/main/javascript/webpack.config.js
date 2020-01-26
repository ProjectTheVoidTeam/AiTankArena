module.exports = {
    entry: "./src/index.ts",
    output: {
        path: __dirname + '/dist',
        filename: "main.js"
    },
    resolve: {
        extensions: [".tsx", ".ts", ".js", ".json"]
    },
    module: {
        rules: [
            // all files with a '.ts' or '.tsx' extension will be handled by 'ts-loader'
            {test: /\.ts$/, use: ["ts-loader"], exclude: /node_modules/}
        ]
    }
}
