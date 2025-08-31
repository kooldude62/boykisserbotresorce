import random
import pyautogui
import pyperclip
import keyboard
import time

e = False

# === Link sets ===
boykisser_links = [
    "https://media.tenor.com/SFsmQdwxd8YAAAAM/boykisser-dance.gif",
    "https://i.redd.it/cthtoaqc1j4c1.gif",
    "https://tenor.com/view/chipichipi-boykisser-boykisser-chipichipi-chipichipichapachapa-gif-10758258345566257",
    "https://i.makeagif.com/media/2-21-2024/I18IzD.gif",
    "https://images.steamusercontent.com/ugc/2021594683282390144/55C652934F16E63EFE4A3194F3F2DA2B434AA6F6/?imw=637&imh=358&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=true",
    "https://tenor.com/view/boy-kisser-cute-dance-gregoria-gif-3795838309085519849",
    "https://tenor.com/view/smooth-brain-kitty-boykisser-gif-8234569603800668383",
    "https://tenor.com/view/boykisser-lick-gif-15652678395230238828",
    "https://tenor.com/view/boy-kisser-dance-gif-9252880389624249129",
    "https://tenor.com/view/cheese-burger-yum-boykisser-stare-gif-16619032980437678008",
    "https://tenor.com/view/boykisser-gif-6999847418031861810",
    "https://tenor.com/view/boykisser-gif-8193399318768818300",
    "https://tenor.com/view/boy-kisser-boykisser-gif-7421460624716631752",
    "https://tenor.com/view/boykisser-you-like-kissing-boys-don%27t-you-cat-lowpoly-3d-gif-9960745507421464646",
    "https://tenor.com/view/darkkolaa-blush-silly-cat-shy-love-gif-8011999271766564486",
    "https://tenor.com/view/me-when-i-get-you-boykisser-gif-15629861713642818650",
    "https://tenor.com/view/boykisser-gif-11014045691818866686",
    "https://tenor.com/view/boykisser-gif-12267843187304617853",
    "https://tenor.com/view/mauzimice-mauzymice-mauzy-mice-boykisser-cute-gif-16690839224429433467",
    "https://tenor.com/view/shy-gif-27191515",
    "https://tenor.com/view/happy-kisser-girlkisser-gif-15192169698232153093",
    "https://tenor.com/view/boykisser-sparkle-eyes-wow-gif-602186094440905284",
    "https://tenor.com/view/pat-headpat-pet-good-boy-good-girl-gif-6540666935796842807",
    "https://tenor.com/view/n-no-boykisser-tail-gif-7038898079225597620",
    "https://tenor.com/view/dance-with-me-boykisser-boy-kisser-caramelldansen-meow-gif-2293616212106288374",
    "https://tenor.com/view/happy-boykisser-smile-gif-18088020230772935461",
    "https://tenor.com/view/boykisser-kiss-kiss-gif-kissing-smooch-gif-14255811052713401590",
    "https://tenor.com/view/boykisser-gif-8527141002887319110",
    "https://tenor.com/view/boy-kisser-shy-blushing-gif-7763375073443922909",
    "https://tenor.com/view/boykisser-kissingboys-i-found-i-found-boys-i-found-boys-to-kiss-gif-7752772126703083663",
]

other_links = [
    "https://cdn.discordapp.com/attachments/1277397196634984584/1294396052937511054/niug.gif",
    "https://cdn.discordapp.com/attachments/1375931205970559006/1376351077099901009/togif.gif",
    "https://cdn.discordapp.com/attachments/966910195617894500/1237831065834618962/HOT_SINGLE_FUZZY_DRAGONS_IN_YOUR_AREA.gif",
    "https://cdn.discordapp.com/attachments/1217548176895246347/1295570704200105994/giflooped.gif",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu2StLTiYD4yaA9BSPyyY7-1Hp6zMbBN7bhg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYetb33xhj06OBJzJSh4cc71Nbcf9JWcwoa-SXJX5cnw&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxApwZTsuh33u50xbKNvVAfpfS-xr3xV6NNMilhniY8A&s=10",
    "https://cdn.discordapp.com/attachments/1266159110638801069/1266600686150357118/copy_C52343A1-58B8-4785-8ECA-BC7E11BF7D4B.gif",
    "https://wimg.rule34.xxx//images/2595/9c287148a49212d8ff464fce0838f98e.png?14505857",
    "https://wimg.rule34.xxx//images/2471/0b05486885bdeac39569c9f80a5577a7.jpeg",
    "https://wimg.rule34.xxx//images/2155/b2a7b706174d0cf277023ffe820bbdf990493ca6.jpg",
    "https://wimg.rule34.xxx//images/1745/7e322a030f1795acf2cfa641c897141d.png?12701542",
    "https://wimg.rule34.xxx//images/2705/88ac910d3dbc5c782b9d921e7bf32524.gif?14019846",
    "https://wimg.rule34.xxx//images/1350/e3fe4bb727a262475982a59748fa30d3.jpeg",
    "https://wimg.rule34.xxx//images/2313/07fbcb8cbeffdb04bba07b544d033ae6f1d2b83f.jpg?11974078",
    "https://wimg.rule34.xxx//images/2313/07fbcb8cbeffdb04bba07b544d033ae6f1d2b83f.jpg?11974078",
]

carrot_link = [
    "https://cdn.discordapp.com/attachments/1304816521348124752/1305682263446519919/Carrot.gif?ex=68b4e0de&is=68b38f5e&hm=b60c447177b3a345bfb85c125b36aa1780b06c6f6df21fe0db63c718194ba9f6&"
]

print("=== [Boykisser Bot Menu] ===")
print("1 - Spam Boykisser GIFs!")
print("2 - Spam NSFW/Rule 34 [18+ WARNING]")
print("3 - carrot")
choice = input("Choose (1/2/3): ").strip()

if choice == "1":
    links = boykisser_links
elif choice == "2":
    links = other_links
elif choice == "3":
    links = carrot_link
else:
    print("Invalid choice. Defaulting to Boykisser GIFs.")
    links = boykisser_links

print("Press SPACE to start sending, P to quit.")

while True:
    if keyboard.is_pressed("p"):
        print("Stopped.")
        break
    
    if keyboard.is_pressed("space"):
        e = True
    
    if e:
        link = random.choice(links)
        pyperclip.copy(link)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        print(f"Sent: {link}")
        time.sleep(0.3)
