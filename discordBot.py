import discord
from discord.utils import get
import random

client = discord.Client()
confirmEjects = ["Yes", "No"]
emergencyMeeting = [0,1,2,3,4,5,6,7,8,9]
emergencyCooldown = [0,5,10,15,20,25,30,35,40,45,50,55,60]
discussionTime = [0,15,30,45,60,75,90,105,120]
votingTime = [0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300]
playerSpeed = [0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0]
crewmateVision = [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0,3.25,3.5,3.75,4.0,4.25,4.5,4.75,5.0]
impostorVision = [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0,3.25,3.5,3.75,4.0,4.25,4.5,4.75,5.0]
killCooldown = [10.0,12.5,15.0,17.5,20.0,22.5,25.0,27.5,30.0,32.5,35.0,37.5,40.0,42.5,45.0,47.5,50.0,52.5,55.0,57.5,60.0]
killDistance = ["Short","Medium","Long"]
visualTasks = ["Yes", "No"]
commonTasks = [0,1,2]
longTasks = [0,1,2,3]
shortTasks = [0,1,2,3,4,5]


@client.event
async def on_ready():
  print('Ready to bot')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.upper() == '!HELLO':
    await message.channel.send('Hello human!')

  if message.content.upper() == '!HELP':
    await message.channel.send('Type !r followed by ANY of the following (cejects, emeeting, ecooldown, dtime, vtime, pspeed, cvision, ivision, kcooldown, kdistance, vtasks, ctasks, ltasks, stasks) USE A COMMA after EACH COMMAND when using MORE THAN ONE command')

  command = ["cejects", "emeeting", "ecooldown", "dtime", "vtime", "pspeed", "cvision", "ivision", "kcooldown", "kdistance", "vtasks", "ctasks", "ltasks", "stasks"]
  if message.content.split()[0].upper() == '!R' and message.content.partition(' ')[2].upper() == "ALL":
    text = " "
    text += 'Confirm Ejects: ' + str(random.choice(confirmEjects)) + " \n"
    text += 'Number of Emergency Meetings: ' + str(random.choice(emergencyMeeting)) + " \n"
    text += 'Emergency Cooldown: ' + str(random.choice(emergencyCooldown)) + " \n"
    text += 'Discussion Time: ' + str(random.choice(discussionTime)) + " \n"
    text += 'Voting Time: ' + str(random.choice(votingTime)) + " \n"
    text += 'Player Speed: ' + str(random.choice(playerSpeed)) + " \n"
    text += 'Crewmate Vision: ' + str(random.choice(crewmateVision)) + " \n"
    text += 'Impostor Vision: ' + str(random.choice(impostorVision)) + " \n"
    text += 'Kill Cooldown: ' + str(random.choice(killCooldown)) + " \n"
    text += 'Kill Distance: ' + str(random.choice(killDistance)) + " \n"
    text += 'Visual Tasks: ' + str(random.choice(visualTasks)) + " \n"
    text += '# of Common Tasks: ' + str(random.choice(commonTasks)) + " \n"
    text += '# of Long Tasks: ' + str(random.choice(longTasks)) + " \n"
    text += '# of Short Tasks: ' + str(random.choice(shortTasks)) + " \n"
    await message.channel.send(text)

  elif message.content.split()[0].upper() == '!R' and any(item in message.content.partition(' ')[2].split(", ") for item in command) is True:
    userInput = message.content.partition(' ')[2].split(", ")
    text = " "
    if 'cejects' in userInput:
        text += 'Confirm Ejects: ' + str(random.choice(confirmEjects)) + " \n"
    if 'emeeting' in userInput:
        text += 'Number of Emergency Meetings: ' + str(random.choice(emergencyMeeting)) + " \n"
    if 'ecooldown' in userInput:
        text += 'Emergency Cooldown: ' + str(random.choice(emergencyCooldown)) + " \n"
    if 'dtime' in userInput:
        text += 'Discussion Time: ' + str(random.choice(discussionTime)) + " \n"
    if 'vtime' in userInput:
        text += 'Voting Time: ' + str(random.choice(votingTime)) + " \n"
    if 'pspeed' in userInput:
        text += 'Player Speed: ' + str(random.choice(playerSpeed)) + " \n"
    if 'cvision' in userInput:
        text += 'Crewmate Vision: ' + str(random.choice(crewmateVision)) + " \n"
    if 'ivision' in userInput:
        text += 'Impostor Vision: ' + str(random.choice(impostorVision)) + " \n"
    if 'kcooldown' in userInput:
        text += 'Kill Cooldown: ' + str(random.choice(killCooldown)) + " \n"
    if 'kdistance' in userInput:
        text += 'Kill Distance: ' + str(random.choice(killDistance)) + " \n"
    if 'vtasks' in userInput:
        text += 'Visual Tasks: ' + str(random.choice(visualTasks)) + " \n"
    if 'ctasks' in userInput:
        text += '# of Common Tasks: ' + str(random.choice(commonTasks)) + " \n"
    if 'ltasks' in userInput:
        text += '# of Long Tasks: ' + str(random.choice(longTasks)) + " \n"
    if 'stasks' in userInput:
        text += '# of Short Tasks: ' + str(random.choice(shortTasks)) + " \n"
    
    await message.channel.send(text)

 







client.run('NzU5OTAzMTIzMTc0MDY0MTQw.X3EQ7g.-Ddl11CxFqH1eVKUMg1lqMrJppk')