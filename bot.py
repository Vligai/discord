# bot.py
import os
import random
import matplotlib.pyplot as plt 
import mplfinance 
import pandas as pd 
from datetime import date, datetime, time, timedelta
import dateutil.relativedelta
import pandas_datareader.data as web
import matplotlib.dates as mpdates 
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands


logging.basicConfig(filename='example.log')
bot = commands.Bot(command_prefix='$')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
channel = client.get_channel(12324234183172)


def stonks(sym):
    try:
        plt.style.use('dark_background') 
        today = datetime.today() 
        past_date = today - dateutil.relativedelta.relativedelta(months=3)
        df = web.DataReader(sym, 'yahoo', past_date, today).reset_index()
        print(df)
        df.set_index('Date', inplace=True, drop=False)

        df = df[['Date', 'Open', 'High',  
                 'Low', 'Close', 'Adj Close', 'Volume']] 

        df['Date'] = pd.to_datetime(df['Date']) 
        df['Date'] = df['Date'].map(mpdates.date2num) 
        mplfinance.plot(df, type='candle',title=sym.upper() + " "+str(past_date.strftime("%b %Y")) + " to "  + str(today.strftime("%b %Y")) , volume=True,  savefig='.\send_stock\\' + sym + '.png') 
    except Exception as e:
        return e

@bot.command()
async def gdata(ctx, sym):
    try:
        logging.info('Getting Data')
        plt.style.use('dark_background') 
        today = datetime.today() 
        past_date = today - dateutil.relativedelta.relativedelta(months=3)
        df = web.DataReader(sym, 'yahoo', past_date, today).reset_index()
        logging.info('df')
        df.set_index('Date', inplace=True, drop=False)

        df = df[['Date', 'Open', 'High',  
                 'Low', 'Close', 'Adj Close', 'Volume']] 

        df['Date'] = pd.to_datetime(df['Date']) 
        df['Date'] = df['Date'].map(mpdates.date2num) 
        mplfinance.plot(df, type='candle',title=sym.upper() + " "+str(past_date.strftime("%b %Y")) + " to "  + str(today.strftime("%b %Y")) , volume=True,  savefig='.\send_stock\\' + sym + '.png') 
    except Exception as e:
        logging.error(e)
        await ctx.send("Unable to find recent data for " + sym +". Please verify if the spelling is correct." )
        return e

    await ctx.send(file=discord.File('.\send_stock\\' + sym + '.png'))


@bot.command()
async def penelope(ctx, test):
    await ctx.send('You passed {}'.format(test))
    queen_images = ["img\pen1.png", "img\pen2.png", "img\pen3.png"]
    queen_quotes = [
        (
            "You corporate fucking prick I did not become a doctor just to suck the devil's dick"
            "Bingpot!"
        ),
        "Well I don't want to eat the rich, I'd have to eat my heroes first",
        (
            "But Ted Bundy was just never that fuckin’ bright"
            "He was just sorta charismatic and white, alright?"
        ),
    ]
    

bot.run(TOKEN)
