import discord, yagmail
from discord.ext.commands import Bot

mailBot = Bot("z!")
icerik = ["Mail Adresi", "Mail Parolası", "Mail Alıcısı", "Mail Konusu", "Mail İçeriği", "Spam Sayısı"]

def mailYolla(mailAdres, mailParola, mailAlici, mailKonu, mailIcerik, mailSayi, sayi):
  sayi = 0
  mail = yagmail.SMTP(mailAdres, mailParola)
  while sayi != int(mailSayi):
    mail.send(
      to = mailAlici,
      subject = mailKonu,
      contents = mailIcerik
    )
    print(int(mailSayi))
    sayi += 1

@mailBot.event
async def on_ready():
  print(f"{mailBot.user.name} olarak giriş yapıldı.")
  await mailBot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{mailBot.command_prefix}mailspam | Spamcınız!"))

@mailBot.command(name="mailspam")
async def _command(ctx):
  sayi = 0
  def kontrol(m):
    return m.author.id == ctx.author.id
  #if os.path.exists("config.txt"):
  for i in icerik:
    embed=discord.Embed(title=" ", description=f"Spam atabilmek için `{i}` verisini girmelisiniz.\nLütfen `{i}` verisini giriniz.")
    embed.set_author(name="MailSpam", icon_url="https://pbs.twimg.com/profile_images/1276328314488213505/U8ofd8Zu_400x400.jpg")
    embed.set_footer(text=f"{i} - ZiksthemW")
    await ctx.send(embed=embed)
    icerik[sayi] = await mailBot.wait_for("message", check=kontrol)
    sayi += 1
  await ctx.send("``Mail gönderimi başlıyor..``")
  mailYolla(icerik[0].content, icerik[1].content, icerik[2].content, icerik[3].content, icerik[4].content, icerik[5].content, sayi)

mailBot.run('TOKEN')
