import discord
import responses
import supabase

url = "https://mwhijshweapgwqbdaxtv.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im13aGlqc2h3ZWFwZ3dxYmRheHR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTgyNzQwNjYsImV4cCI6MjAxMzg1MDA2Nn0.I9gDZrtW2CAJq_IaeQ49dXv_jKZOFGSoR46wPl59mhg"
supabase_client = supabase.create_client(url,key)

async def send_message(message, user_message, is_private):
    try: 
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN ='MTE2NjI5MjkzMjM3OTI3OTQxMA.GRLkVV.u5yuEXpGPqUXBFBPv_zYwA0xzcEIdbdycM4Vwk'
    intents =discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents =intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author ==client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] =='!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private =True)
        else:
            await send_message(message, user_message, is_private=False)
    client.run(TOKEN)
