const express = require("express");
const controlador = require("./controllers");
const roteador = express.Router();

// Rota para obter usuários
roteador.get("/usuarios", async (req, res) => {
  const usuarios = await controlador.buscarUsuarios();
  res.send(usuarios);
});

// Rota para criar um usuário
roteador.post("/usuarios", async (req, res) => {
  const novoUsuario = req.body.nome;
  const resultado = await controlador.criarUsuario(novoUsuario);
  res.send(resultado);
});

module.exports = roteador;
