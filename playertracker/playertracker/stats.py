import nflgame



def playerStats():
	game = nflgame.one(2015, 1, "NE", "PIT")
	tom_brady = game.players.name("T.Brady")
	return tom_brady.formatted_stats()
