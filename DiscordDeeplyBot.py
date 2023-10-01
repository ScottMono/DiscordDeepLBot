# import deepl
import deepl

import discord

# importing os and dotenv to load up the deepl auth key I have stored in my .env file
import os
from dotenv import load_dotenv

# import logging
import logging

# use the load_dotenv function to load the .env file
load_dotenv()

# populate AUTH_KEY and BOT_TOKEN with the values from our .env file
AUTH_KEY = os.getenv("AUTH_KEY")
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# create a translator instance
translator = deepl.Translator(AUTH_KEY)

# setup intents to read message content
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = discord.Client(intents=intents)

# event for when the bot is ready


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# event for when a message is sent. Hook into the message and check values then react accordingly


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await translation_help(message)

    await guild_shit(message)

# starting point/testing for role assignment based upon random shit. Will eventually swap to when a user joins


async def guild_shit(message):
    if message.content.startswith('!guild'):
        guild_roles = message.guild.roles
        for role in guild_roles:
            if role.name == 'test':
                await message.author.add_roles(role, reason="Triggered by bot command", atomic=True)
                break

        # await message.channel.send(guild_roles)


async def translation_help(message):
    if message.content.startswith('!help'):
        await message.channel.send('Want to translate a message? Simple react to it with on of the following flag '
                                   'emojis: :flag_bg:, :flag_cz:, :flag_dk:, :flag_de:, :flag_gr:, :flag_gb:, '
                                   ':flag_us:, :flag_es:, :flag_ee:, :flag_fi:, :flag_fr:, :flag_hu:, :flag_id:, '
                                   ':flag_it:, :flag_jp:, :flag_kr:, :flag_lt:, :flag_lv:, :flag_no:, :flag_nl:, '
                                   ':flag_pl:, :flag_pt:, :flag_br:, :flag_ro:, :flag_ru:, :flag_sk:, :flag_si:, '
                                   ':flag_se:, :flag_tr:, :flag_ua:, :flag_cn:')


@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    await translate_emoji_flag(emoji, reaction)


async def translate_emoji_flag(emoji, reaction):
    if emoji is not None:
        translated_message = None
        match emoji:
            case "🇧🇬":
                translated_message = translate_message(reaction.message, "BG")
            case "🇨🇿":
                translated_message = translate_message(reaction.message, "CS")
            case "🇩🇰":
                translated_message = translate_message(reaction.message, "DA")
            case "🇩🇪":
                translated_message = translate_message(reaction.message, "DE")
            case "🇬🇷":
                translated_message = translate_message(reaction.message, "EL")
            case "🇬🇧":
                translated_message = translate_message(reaction.message, "EN")
            case "🇺🇸":
                translated_message = translate_message(reaction.message, "EN-US")
            case "🇪🇸":
                translated_message = translate_message(reaction.message, "ES")
            case "🇪🇪":
                translated_message = translate_message(reaction.message, "ET")
            case "🇫🇮":
                translated_message = translate_message(reaction.message, "FI")
            case "🇫🇷":
                translated_message = translate_message(reaction.message, "FR")
            case "🇭🇺":
                translated_message = translate_message(reaction.message, "HU")
            case "🇮🇩":
                translated_message = translate_message(reaction.message, "ID")
            case "🇮🇹":
                translated_message = translate_message(reaction.message, "IT")
            case "🇯🇵":
                translated_message = translate_message(reaction.message, "JP")
            case "🇰🇷":
                translated_message = translate_message(reaction.message, "KO")
            case "🇱🇹":
                translated_message = translate_message(reaction.message, "LT")
            case "🇱🇻":
                translated_message = translate_message(reaction.message, "LV")
            case "🇳🇴":
                translated_message = translate_message(reaction.message, "NB")
            case "🇳🇱":
                translated_message = translate_message(reaction.message, "NL")
            case "🇵🇱":
                translated_message = translate_message(reaction.message, "PL")
            case "🇵🇹":
                translated_message = translate_message(reaction.message, "PT")
            case "🇧🇷":
                translated_message = translate_message(reaction.message, "PT-BR")
            case "🇷🇴":
                translated_message = translate_message(reaction.message, "RO")
            case "🇷🇺":
                translated_message = translate_message(reaction.message, "RU")
            case "🇸🇰":
                translated_message = translate_message(reaction.message, "SK")
            case "🇸🇮":
                translated_message = translate_message(reaction.message, "SL")
            case "🇸🇪":
                translated_message = translate_message(reaction.message, "SV")
            case "🇹🇷":
                translated_message = translate_message(reaction.message, "TR")
            case "🇺🇦":
                translated_message = translate_message(reaction.message, "UK")
            case "🇨🇳":
                translated_message = translate_message(reaction.message, "ZH")
            case _:
                return

        if translated_message is not None:
            await reaction.message.channel.send(translated_message)

# translate a message


def translate_message(message, target_language):
    return translator.translate_text(message.content, target_lang=target_language)


# assign a logger handler and then run our discord bot client
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)
