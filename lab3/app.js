const express = require('express');
const path = require('path');
const app = express();


app.use(express.static(path.join(__dirname, 'public')));

app.use(express.urlencoded({ extended: true }));

app.get('/hola', (req, res) => {
    res.send('El servidor responde correctamente');
});

app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000');
});

app.use(express.urlencoded({ extended: true }));

app.post('/guardar', (req, res) => {
console.log(req.body);
res.send('Datos recibidos');
});