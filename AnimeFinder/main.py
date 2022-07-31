from Anime.anime import Anime
import os

from Anime.constants import BASE_FOLDER
with Anime() as bot:
    if not os.path.exists(os.path.join(BASE_FOLDER,'data')):
        os.makedirs('./data')
    bot.landingPage()
    bot.AZList()

    input('continue?\n')