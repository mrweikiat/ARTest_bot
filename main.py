import telebot
import time

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
stringHelp = 'Hi I am ARTesterBot! I can help you take your ART test, simply press /start to begin.'


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Hello! Do you have Covid? Let’s find out!\n' + 'To start testing, press /test.\n' + 'To get help, press /help.')


# sending message to the bot after input
@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, 'Make sure you have a new ART test with you,' +
                     'and make sure that you have washed your hands.' +
                     'Once you are ready, click on /disclaimer to get started with the testing.')


# disclaimer before doing art test
@bot.message_handler(commands=['disclaimer'])
def disclaimer(message):
    bot.send_message(message.chat.id, 'Do not attempt the ART test if\n' +
                     '1) You have a nosebleed for the past 24hrs\n' +
                     '2) Nasal surgery in the last 4 weeks\n' +
                     '3) Facial Injury in the last weeks\n' +
                     'Once you are sure, click or type /Step1 to proceed.')


# Step 1
@bot.message_handler(commands=['Step1'])
def test(message):
    bot.send_message(message.chat.id, 'Please clean your hands before starting the test. Click on /Step2 to proceed.')


# Step 2
@bot.message_handler(commands=['Step2'])
def test(message):
    bot.send_message(message.chat.id, 'Before starting the test, please take out' +
                     'one swab stick, one reagent tube and one cartridge.' +
                     'Loosen the cap of the reagent tube and take out the' +
                     'cartridge from its packaging. Click on /Step3 to proceed.')


# Step 3
@bot.message_handler(commands=['Step3'])
def test(message):
   bot.send_message(message.chat.id, 'Remove swab stick from package. Click on /Step4 to proceed.')


# Step 4
@bot.message_handler(commands=['Step4'])
def test(message):
   bot.send_message(message.chat.id, 'Insert the swab stick into the nostril (~2.5cm).' +
                    'Twirl the stick 5 times and leave it in for 5 seconds. Click on /Step5 to proceed.')


# Step 5
@bot.message_handler(commands=['Step5'])
def test(message):
   bot.send_message(message.chat.id, 'Repeat for the other nostril with the same swab. Click on /Step6 to proceed.')


# Step 6
@bot.message_handler(commands=['Step6'])
def test(message):
   bot.send_message(message.chat.id, 'Squeeze the reagent tube when extracting the swab.  Click on /Step7 to proceed.')


# Step 7
@bot.message_handler(commands=['Step7'])
def test(message):
   bot.send_message(message.chat.id, 'Squeeze the reagent tube when extracting the swab.  Click on /Step8 to proceed.')


# Step 8
@bot.message_handler(commands=['Step8'])
def test(message):
    bot.send_message(message.chat.id, 'Close the cap of the reagent tube firmly.' +
                     'You should hear a “click” sound. Click on /Step9 to proceed.')


# Step 9
@bot.message_handler(commands=['Step9'])
def test(message):
   bot.send_message(message.chat.id, 'Use your finger to gently tap the side of the tube a few times.' +
                    'This helps to mix the solution. Click on /Step10 to proceed.')


# Step 10
@bot.message_handler(commands=['Step10'])
def test(message):
   bot.send_message(message.chat.id, 'Place 3 drops onto the sample well of the test cartridge.' +
                    'Click on /Step11 to proceed.')


# Step 11
@bot.message_handler(commands=['Step11'])
def test(message):
    bot.send_message(message.chat.id, 'Wait for 15 mins before checking the results on the test cartridge.' +
                     'Please keep the cartridge on flat ground for the whole duration. The timer will start now.')
    for x in range(1, 16):
        time.sleep(60)
        msg = str(x) + "minute(s) have passed."
        bot.send_message(message.chat.id, msg)
    bot.send_message(message.chat.id, 'Click on /Step12 to proceed.')


text = 'https://www.covid.gov.sg/'


# Step 12
@bot.message_handler(commands=['Step12'])
def test(message):
    bot.send_message(message.chat.id, 'Read the results on the test cartridge.' +
                     'If you see a line appearing at both the “C” and the “T” position,' +
                     'this indicates a positive test. \n' +
                     'Sorry you got Covid! Here’s more information ' + text + "\n"
                     'If you see a line appearing at only the “C” position, this indicates a negative test. \n' +
                     'Click on /Step13 to proceed. \n' +
                     'If you see a line appearing at only the “T” position,' +
                     'the test is invalid. Please repeat the test on another test kit.\n' +
                     'Click on /Step1 to retake the test.')


# Step 13
@bot.message_handler(commands=['Step13'])
def test(message):
    bot.send_message(message.chat.id, 'Dispose all used swab sticks, reagent tube and test cartridge.' +
                     'Click on /Step14 to proceed.')


# Step 14
@bot.message_handler(commands=['Step14'])
def test(message):
    bot.send_message(message.chat.id, 'Clean your hands after the test. See you again on your next ART Test! :D')


# command help to show all available commands
@bot.message_handler(commands=['help'])
def helping(message):
    bot.send_message(message.chat.id, stringHelp)


bot.polling()
