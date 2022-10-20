from bs4 import BeautifulSoup
import requests
import random
from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
base_url = "https://www.russianfood.com/recipes/bytype/?fid=216"


@dp.message_handler(commands=["start", "help"])
async def get_recipes(message: types.Message):
    await message.answer("Hi!I have so many recipe for u!"
                         "U can choice random recipe""\U0001F600", reply_markup=nav.kb_client)
    await message.delete()


@dp.message_handler()
async def get_recipes(message: types.Message):
    if message.text == "Сhoice recipe":
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.5112.114 YaBrowser/22.9.1.1095 Yowser/2.5 Safari/537.36",
            'accept': "*/*"
        }

        # req = requests.get(url, headers)
        # with open("project.html", "w") as file:
        #     file.write(req.text)
        with open("project.html") as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")
        recipe_title = soup.find_all("div", class_="recipe_l in_seen v2")
        recipe_list = []

        for recipe in recipe_title:
            recipe_article = recipe.find("div", class_="title").find("a").text
            recipe_url = "https://www.russianfood.com/" + recipe.find("div", class_="title").find("a").get("href")
            short_description = recipe.find("div", class_="announce").find("p").text
            recipe_list.append(f"{recipe_article}\n{short_description}\n{recipe_url}")
            random_recipe_list = random.choice(recipe_list)
        await message.answer(random_recipe_list, reply_markup=nav.kb_client2)
        await message.delete()
    elif message.text == "Next, it's not tasty":
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.5112.114 YaBrowser/22.9.1.1095 Yowser/2.5 Safari/537.36",
            'accept': "*/*"
        }

        # req = requests.get(url, headers)
        # with open("project.html", "w") as file:
        #     file.write(req.text)
        with open("project.html") as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")
        recipe_title = soup.find_all("div", class_="recipe_l in_seen v2")
        recipe_list = []

        for recipe in recipe_title:
            recipe_article = recipe.find("div", class_="title").find("a").text
            recipe_url = "https://www.russianfood.com/" + recipe.find("div", class_="title").find("a").get("href")
            short_description = recipe.find("div", class_="announce").find("p").text
            recipe_list.append(f"{recipe_article}\n{short_description}\n{recipe_url}")
            random_recipe_list = random.choice(recipe_list)
        await message.answer(random_recipe_list, reply_markup=nav.kb_client2)
        await message.delete()





if __name__ == "__main__":
    executor.start_polling(dp)
