import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)
token = "MTE2NjI5MjkzMjM3OTI3OTQxMA.GF4lvW.Fjnmn4-e-n5-W0WUiA6JvMMMiMzZS384BYHIws"

@bot.event
async def on_ready():
    print("Online")
user_id ="512593710631092224"
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    
    if  message.guild.id == 850020691775979610 and message.author.id==user_id:  
       
        if message.channel.name == '1':
           
            if "WEC club" in message.content in message.content:
                response = ""

                if "convenor" in message.content.lower():
                    response = "The convenor of WEC club is Pranav RS."


                if "sig" in message.content.lower():
                    response ="which SIG you want to know about?"
                    if "algorithm" in message.content.lower():
                        response = "We are a group of coding enthusiasts whose aim is to promote Competitive Programming culture at NITK. As part of this mission, we conduct many workshops and contests related to CP. We also conduct sessions like Codebuddy as a bridge between junior-senior. This year we are starting a new mentorship program as part of the SIG to help students in the field of coding skills required to crack interviews for internships and placements"
                    elif "gdsc" in message.content.lower():
                        response = "We focus on helping students bridge the gap between theory and practice in software development. Students grow their knowledge in a peer-to-peer learning environment while building solutions to existing problems and helping the communities around through various projects and events. We have tried our hands on backend, frontend, mobile development and are now venturing into game development as well"
                    elif "intelligence" in message.content.lower():
                        response = "We focus on understanding human intelligence and applying it to machines for the benefit of humanity. We explore the domains of Machine Learning (ML) and Artificial Intelligence (AI), focusing on both research and applications. We research topics in ML theory, Deep Learning, Reinforcement Learning, Data Science, etc. and their applications in simulated and real worlds. We are also interested in competitive ML, primarily participating in Kaggle contests and applying ML techniques for software products"
                    elif "system" in message.content.lower():
                        response ="We are group of motivated, passionate students who are interested in exploring the various avenues of computer systems . The Systems and Security SIG deals with a broad range of domains including Networks and Distributed Systems, Blockchains, Security, OS, DBMS and Architecture. We are enthusiastic about exploring large open source projects like the Linux kernel. Whether you're interested in Capture the Flag (CTF) security challenges or understanding how large systems like Netflix work, Systems and Security SIG is your go-to group at NITK"

                    

                

                if response:
                    await message.channel.send(response)

    await bot.process_commands(message)

bot.run(token)
