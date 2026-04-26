const express = require('express');
const path = require('path');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const port = process.env.PORT || 8081;

app.use((req, res, next) => {
  console.log('Requested: ' + req.url);
  next();
});

app.use(express.static(path.join(__dirname, 'public')));

app.use(createProxyMiddleware({
  target: 'https://2019.makemepulse.com',
  changeOrigin: true,
}));

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
