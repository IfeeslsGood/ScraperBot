## Random recipes Telegram bot
A telegram bot that uses a scraper to send random recipes with a brief description and ingredients that can be selected using the buttons from the site russiyanfood.com.
The user will not know that the bot has bot prepared for him.


## Installed libraries
-  pip install -U aiogram
-  pip install lxml
-  pip install request

## Imports
- from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
- from bs4 import BeautifulSoup
- import requests
- import random
- from aiogram import Bot, types
- from aiogram.dispatcher import Dispatcher
- from aiogram.utils import executor

## Instructions for use 
1. Send message /start
2. Press the "Select Recipe" button
if you didn't like the recipe "next, it's not tasty"


## Enjoy your meal!










