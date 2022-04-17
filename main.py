# -*- coding: utf-8 -*-

import os
import logging
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Discord import Discord
from TwitchChannelPointsMiner.classes.Settings import Priority, Events, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Bet import Strategy, BetSettings, Condition, OutcomeKeys, FilterCondition, DelayMode
from TwitchChannelPointsMiner.classes.entities.Streamer import StreamerSettings

try: # if on relpit
    from keep_alive import keep_alive
    keep_alive()
except:
  pass


twitch_miner = TwitchChannelPointsMiner(
    username=os.environ['username'],
    password=os.environ['password'],
    claim_drops_startup=False,
    priority=[
        Priority.STREAK,
        Priority.DROPS,
        Priority.ORDER
    ],
    logger_settings=LoggerSettings(
        save=False,
        console_level=logging.INFO,
        emoji=True,
        less=True,
        colored=True,
        discord=Discord(
            webhook_api="https://discord.com/api/webhooks/964606817558749214/54grQTqZBjQo4iltOhOBVZx4CRzlFqlx1irDLsByFLF2GlwRuKeOg-kmddFZEdOuIP1u",
            events=[Events.STREAMER_ONLINE, Events.STREAMER_OFFLINE, Events.GAIN_FOR_CLAIM, Events.DROP_CLAIM, Events.GAIN_FOR_WATCH_STREAK, Events.JOIN_RAID, Events.BET_START,
                    Events.BET_GENERAL, Events.BET_WIN, Events.BET_FAILED, Events.BET_FILTERS, Events.BET_REFUND, Events.BET_LOSE]
        )
    ),
    streamer_settings=StreamerSettings(
        make_predictions=True,
        follow_raid=True,
        claim_drops=True,
        watch_streak=True,
        chat=ChatPresence.ONLINE,
        bet=BetSettings(
            strategy=Strategy.HIGH_ODDS,
            percentage=2,
            max_points=50000,
            delay=0.8,
            delay_mode=DelayMode.PERCENTAGE,
        )
    )
)


twitch_miner.mine(
    ['VALORANT'],
    followers=True,
    followers_order=FollowersOrder.ASC
)
