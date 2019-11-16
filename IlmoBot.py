import discord
from discord.ext import commands
from selenium import webdriver


client = commands.Bot(command_prefix = ">", case_insensitive=True)
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name=">help", type=3))
    print("Bot is ready.")


@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title = "Help", colour = discord.Colour.gold())
    embed.set_footer(
        text = "Ilmoita bugeista jos jaksat | Akatixxc#2452 | https://github.com/Akatixxc/IlmoBot", 
        icon_url ="https://cdn.discordapp.com/avatars/144805468458582016/33cda21905ed505a2c46a15be7c76b29.png?size=128"
        )
    embed.add_field(name = ">ilmo", value = "Näyttää tämänhetkiset avoimet ilmoitukset")
    embed.add_field(name = ">________", value = "Joskus saatan jaksaa tehdä lisää mutta ei nyt kuitenkaan")
    await ctx.author.send(embed = embed)


@client.command()
async def ilmo(ctx):
    embed = discord.Embed(title = "Haetaan tapahtumia!", colour = discord.Colour.gold())
    message = await ctx.send(embed = embed)

    driver.delete_all_cookies()
    driver.implicitly_wait(5)
    driver.get("https://digit.fi/ilmo")
    ilmo = driver.find_element_by_css_selector("ul.menu-list").text.split("\n")
    
    embed = discord.Embed(colour = discord.Colour.gold())
    embed.set_author(name = "Tapahtumat", 
        url = "https://digit.fi/ilmo", 
        icon_url = "https://cdn.discordapp.com/icons/346708564628471808/10d4b771cc25ddb0fde7d6844205edc6.png?size=128"
    )

    for i in range(0, len(ilmo), 2):
        event_name = ilmo[i]
        link_to_ilmo = driver.find_element_by_partial_link_text(event_name)
        link_to_ilmo.click()
        pvm = driver.find_element_by_css_selector("span.is-inline-block").text.split("\n")[1]
        participators = driver.find_element_by_css_selector("small.has-text-grey-light").text

        embed.add_field(
            name = pvm, 
            value = f"{event_name} \n Osallistujat: {participators} [[link]({driver.current_url})]"
            )
    
    message = await message.edit(embed = embed)


def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-minimized")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\\Tiedostot\\chromedriver_win32\\chromedriver.exe")

executor_url = driver.command_executor._url
session_id = driver.session_id

driver2 = create_driver_session(session_id, executor_url)

client.run(open("KEY.txt", "r").read())