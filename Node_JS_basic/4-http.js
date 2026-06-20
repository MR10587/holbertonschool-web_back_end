const app = require('node:http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-type': 'text/plain'});

    res.end('Hello Holberton School!');
});

server.listen(PORT, () => {
  console.log(`Server is successfully listening on http://localhost:${PORT}`);
});

module.exports = app;