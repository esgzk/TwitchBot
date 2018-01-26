import config
import urllib.request
import json
from time import sleep


def mess(sock, message):
	sock.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, message).encode("utf-8"))


def ban(sock, user):
	mess(sock, ".ban {}".format(user))


def timeout(sock, user, second=500):
	mess(sock, ".timeout {}".format(user, second))


def fill0plist():
	while True:
		try:
			url = "https://tmi.twitch.tv/group/user/esgzk/chatters"
			req = urllib.request.Request(url)
			res = urllib.request.urlopen(req).read()
			if res.find("502 bad gateway") == -1:
				config.oplist.clear()
				data = json.loads(res)
				for r in data["chatters"]["moderators"]:
					config.oplist[r] = "mod"
				for r in data["chatters"]["global_mods"]:
					config.oplist[r] = "global_mod"
				for r in data["chatters"]["admins"]:
					config.oplist[r] = "admin"
				for r in data["chatters"]["staff"]:
					config.oplist[r] = "staff"
		except:
			"Do nothing..."
		sleep(5)


