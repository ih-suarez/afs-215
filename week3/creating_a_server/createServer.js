const http = require('http')

const server = http.createServer((req, res) => {
    console.log(`request made: ${req.url}`)
    res.writeHead(200, {'Content-Type': 'text/plain'})
    res.end('Hello World')
});

server.listen(9000, '127.0.0.1', console.log('Now Listening on port 9000'))