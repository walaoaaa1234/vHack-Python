#!/usr/bin/python2.7
# -*- coding: utf-8

from console import Console
from update import Update
from botnet import Botnet
from random import randrange, uniform
import time
import json
import config
import ddos
from player import Player

class run:

    def __init__(self):
        """
        Pull all variables from config.py file.
        """
        self.player = Player()
        self.database = config.database
        self.Max_point_tournament = config.Max_point_tournament
        self.BotNet_update = config.BotNet_update
        self.joinTournament = config.joinTournament
        self.tournament_potator = config.tournament_potator
        self.booster = config.booster
        self.Use_netcoins = config.Use_netcoins
        self.attacks_normal = config.attacks_normal
        self.maxanti_normal = config.maxanti_normal
        self.active_cluster_protection = config.active_cluster_protection
        self.mode = config.mode
        self.wait_load = config.wait_load
        self.c = Console(self.player.username, self.player.password)
        self.u = Update(self.player.username, self.player.password)
        self.b = Botnet(self.player)
        self.ddos = ddos.Ddos()
        self.init()

    def init(self):
        while True:
            self.ddos.run_ddos()
            if self.BotNet_update:
                self.b.upgradebotnet()
            # attack botnet
            self.b.attack()
            if self.joinTournament and self.c.getTournament():
                self.mode = "Potator"
                print "** Force Mode to 'Potator' for Tournament **"
            # task = self.u.doTasks(self.wait_load)
            if self.booster:
                try:
                    # usebooster = self.u.getTasks()
                    usebooster = None
                    json_data = json.loads(usebooster)
                    while len(json_data["data"]) > 1:
                        if int(json_data["boost"]) > 5:
                            self.u.useBooster()
                            print "Using booster on rest " + str(int(json_data["boost"]) - 1)
                        # UPDATE Value
                        else:
                            print "you have < 5 boost."
                            break
                        # usebooster = self.u.getTasks()
                        usebooster = None
                        json_data = json.loads(usebooster)
                except Exception as e:
                    print "Connection Error try again...{0}".format(e)
                    pass
            if self.Use_netcoins:
                time.sleep(2)
                if self.player.netcoins > 1:
                    self.u.finishAll()
                    self.player.refreshinfo()  # update player info
                    print "I used Netcoins for finish all task."
            # attack players
            self.c.attack(self)

r = run()
