// To Start server Enter 'node createServer.js' in the terminal

// Importing and declaring http variable
const http = require('http')

// Declaring Server variable
const server = http.createServer((req, res) => {
    console.log(`request made: ${req.url}`)
    res.writeHead(200, {'Content-Type': 'text/plain'})
    res.end('Hello World')
});

// Server is set to listen on port 9000
server.listen(9000, '127.0.0.1', console.log('Now Listening on port 9000'))