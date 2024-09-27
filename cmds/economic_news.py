import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
from bs4 import BeautifulSoup
from discord import app_commands

class Economic_News(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_message(self,meg):
        if meg.content.startswith('-! '):
            stock_code = meg.content[3:]
            # 要抓取的網址
            url = 'https://tw.stock.yahoo.com/quote/' + stock_code +'/news'
            # 發送GET請求獲取頁面內容
            response = requests.get(url)
            if response.status_code == 200:
                #將整個網站的程式碼爬下來
                soup = BeautifulSoup(response.content, "html.parser")
                #找到h3這個標籤
                getAllNew= soup.find_all("h3", class_="Mt(0) Mb(8px)")
                count=0
                for news_element in getAllNew:
                    # 在 <h3> 標籤下查找 <a> 標籤
                    link_element = news_element.find("a", href=True)
                    if link_element:
                        count+=1
                        # 獲取新聞標題
                        title = link_element.get_text()
                        # 獲取新聞連結
                        link = link_element["href"]
                        await meg.channel.send(f"標題：{title}")
                        await meg.channel.send(f"連結：<{link}>")
                        if(count==3):
                            break
                    #await meg.delete()
            else:
                print("無法獲取頁面內容")
    
async def setup(bot):
    await bot.add_cog(Economic_News(bot))
