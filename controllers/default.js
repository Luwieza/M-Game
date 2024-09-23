const Pty = require('node-pty');
const fs = require('fs');

exports.install = function () {
    // Set up route and WebSocket
    ROUTE('/');
    WEBSOCKET('/', socket, ['raw']);
};

function socket() {
    // No automatic encoding/decoding, and auto-destroy WebSocket on close
    this.encodedecode = false;
    this.autodestroy();

    this.on('open', function (client) {
        console.log('Client connected');

        // Spawn terminal
        client.tty = Pty.spawn('python3', ['run.py'], {
            name: 'xterm-color',
            cols: 80,
            rows: 24,
            cwd: process.env.PWD, // Set working directory
            env: process.env // Inherit environment variables
        });

        // Listen for data from the terminal and send it to the client
        client.tty.on('data', function (data) {
            client.send(data); // Send terminal output to WebSocket client
        });

        // Handle terminal exit
        client.tty.on('exit', function (code, signal) {
            client.tty = null;
            client.close(); // Close the WebSocket connection
            console.log(`Terminal process exited with code ${code} and signal ${signal}`);
        });

        // Handle incoming messages (from WebSocket client)
        client.on('message', function (msg) {
            if (client.tty) {
                client.tty.write(msg); // Pass WebSocket input to the terminal
            }
        });

        // Handle WebSocket close event
        client.on('close', function () {
            if (client.tty) {
                client.tty.kill(); // Kill the terminal process when the WebSocket is closed
                console.log('Terminal process killed');
            }
        });

        // Error handling
        client.tty.on('error', function (err) {
            console.error('Terminal error:', err);
        });
    });
}
