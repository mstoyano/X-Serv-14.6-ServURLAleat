#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random


class random_url(webapp.webApp):

    def process(self, parsedRequest):

        Num_Aleatorio = str(random.randint(0, 10000000))
        return("200 OK", "<html><body>Hola. <a href="
               + Num_Aleatorio + "> Dame otra</a></p></h1>" +
               "</body></html>")

if __name__ == "__main__":
    server = random_url("localhost", 1234)
