#!/usr/bin/env python3
# -*- coding: utf-8 -
class Time:
        
    def __init__(self, jogadores, nome, gol, pontos, ataque, defesa, escudo):
        self.jogadores = jogadores
        self.nome = nome
        self.gol = gol
        self.pontos = pontos
        self.ataque = ataque
        self.defesa = defesa
        self.escudo = escudo
        
    def calcula_ataque(self):
        ataque = 0
        for i in self.jogadores:
            ataque = ataque + i.ataque
        return ataque
    def calcula_defesa(self):
        defesa = 0
        for i in self.jogadores:
            defesa = defesa + i.defesa
        return defesa
    











