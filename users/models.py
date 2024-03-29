from django.db import models
from colorfield.fields import ColorField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_at} - {self.updated_at}"


class Give_offer(BaseModel):  # Ariza berish
    text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.id


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} - {self.category}"


class ProductColors(BaseModel):
    name = models.CharField(max_length=50)
    color =ColorField(default="#FFFFFF")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class ProductImages(BaseModel):
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    color = models.ForeignKey(ProductColors, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id} - {self.color}"


class ProductSize(BaseModel):
    size = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.size} - {self.price}"



# from django.db import models
# from model_utils.models import TimeStampedModel
# from django.contrib.postgres.fields import ArrayField
from djmoney.models.fields import MoneyField

class Product(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ForeignKey(ProductImages, on_delete=models.PROTECT)
    color = models.ForeignKey(ProductColors, on_delete=models.PROTECT)
    size = models.ForeignKey(ProductSize, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField()
    product_count = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.category}"


class User(models.Model):
    class GenderType(models.TextChoices):
        MAN = "Erkak", "erkak"
        WOMAN = "Ayol", "ayol"


    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(GenderType, max_length=5)
    born_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.phone_number} - {self.gender}"


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

from admins.models import Center

class ProductClearance(models.Model):  # Mahsulotni rasmiylashtirish

    class CityType(models.TextChoices):
        TASHKENT = "Toshkent", "toshkent"
        SAMARKAND = "Samarqand", "samarqand"
        NAMANGAN = "Namangan", "namangan"
        ANDIJAN = "Andijon", "andijon"
        BUKHARA = "Buxoro", "buxoro"
        NUKUS = "Nukus", "nukus"
        KARSHI = "Qarshi", "qarshi"
        URGANCH = "Urganch", "urganch"
        KOKAN = "Qoʻqon", "qoʻqon"
        CHIRCHIK = "Chirchiq", "chirchiq"
        FERGANA = "Fargʻona", "fargʻona"
        JIZZAKH = "Jizzax", "jizzax"
        TERMIZ = "Termiz", "termiz"
        MARGILAN = "Margʻilon", "margʻilon"
        NAVOI = "Navoiy", "navoiy"
        ANGREN = "Angren", "angren"
        OLMALIK = "Olmaliq", "olmaliq"
        BEKABAD = "Bekobod", "bekobod"
        KHOJAYLI = "Xoʻjayli", "xoʻjayli"
        DENOV = "Denov", "denov"
        SHAKHRIKHON = "Shahrixon", "shahrixon"
        CHUST = "Chust", "chust"
        GOR = "Gʻor", "gʻor"
        ZARAFSHAN = "Zarafshon", "zarafshon"
        KOSON = "Koson", "koson"
        KONGIROT = "Qoʻngʻirot", "qoʻngʻirot"
        TAXIATOSH = "Taxiatosh", "taxiatosh"
        SHAKHRISABZ = "Shahrisabz", "shahrisabz"
        KATTAKORGON = "Kattaqoʻrgʻon", "kattaqoʻrgʻon"
        ASAKA = "Asaka", "asaka"
        XIVA = "Xiva", "xiva"
        GULISTAN = "Guliston", "guliston"
        BERUNI = "Beruniy", "beruniy"
        CHORTOK = "Chortoq", "chortoq"
        TORTKOL = "To'rtkoʻl", "to'rtkoʻl"
        SOX = "	Soʻx", "soʻx"
        URGUT = "Urgut", "urgut"
        KOSONSOY = "Kosonsoy", "kosonsoy"
        KITOB = "Kitob", "kitob"
        YANGIYOL = "Yangiyoʻl", "yangiyoʻl"
        GIJDUVON = "Gʻijduvon", "gʻijduvon"
        KHONKA = "Xonqa", "xonqa"
        OKTOSH = "Oqtosh", "oqtosh"
        CHIMBOY = "Chimboy", "chimboy"
        PARKENT = "Parkent", "parkent"
        OKHANGARON = "Ohangaron", "ohangaron"
        UCHKORGAN = "Uchqo'rgon", "uchqo'rgon"
        KAMASHI = "Qamashi", "qamashi"
        KUVA = "Quva", "quva"
        UCHKUDUK = "Uchquduq", "uchquduq"
        KHONOBOD = "Xonobod", "xonobod"
        YANGIYER = "Yangiyer", "yangiyer"
        KOVASOY = "Quvasoy", "quvasoy"
        MANGI = "Mangʻi", "mangʻi"
        RISHTON = "Rishton", "rishton"
        UYCHI = "Uychi", "uychi"
        NUROTA = "Nurota", "nurota"
        MUBARAK = "Muborak", "muborak"
        ZARBDOR = "Zarbdor", "zarbdor"
        YANGIKORGAN = "Yangiqoʻrgʻon", "yangiqoʻrgʻon"
        SHAYKHALI = "Shayxali", "shayxali"
        TORAKORGAN = "To'rakor'g'on", "to'rakor'g'on"
        ORNATILGAN = "Oʻrnatilgan", "oʻrnatilgan"
        PISKENT = "Piskent", "piskent"
        KIBRAY = "Qibray", "qibray"
        ZAMIN = "Zomin", "zomin"
        ISKANDAR = "Iskandar", "iskandar"
        YOZISH = "Yozish", "yozish"
        SHAVAT = "Shovot", "shovot"
        TAKHTAKOPIR = "Taxtakoʻpir", "taxtakoʻpir"
        JARKORGAN = "Jarqoʻrgʻon", "jarqoʻrgʻon"
        BULUNGUR = "Bulungʻur", "bulungʻur"
        SHAFIRKAN = "Shofirkon", "shofirkon"
        TASHLAK = "Toshloq", "toshloq"
        SIRDARYA = "Sirdaryo", "sirdaryo"
        KHAKKULOBOD = "Haqqulobod", "haqqulobod"
        SALAR = "Salor", "salor"
        BEKTEMIR = "Bektemir", "bektemir"
        SHERABAD = "Sherobod", "sherobod"
        KORGANTEPA = "Qoʻrgʻontepa", "qoʻrgʻontepa"
        YAKKABOG = "Yakkabogʻ", "yakkabogʻ"
        KORASUV = "Qorasuv", "qorasuv"
        GUZOR = "Gʻuzor", "gʻuzor"
        POYTUG = "Poytugʻ", "poytugʻ"
        OLTIARIQ = "Oltiariq", "oltiariq"
        BAYSUN = "Boysun", "boysun"
        SHARCHI = "Shoʻrchi", "shoʻrchi"
        PAKHTAOBOD = "Paxtaobod", "paxtaobod"
        GAGARIN = "Gagarin", "gagarin"
        YANGIRABAD = "Yangirobod", "yangirobod"
        PAYSHANBA = "Payshanba", "payshanba"
        ALMAZAR = "Olmazor", "olmazor"
        GAZALKENT = "Gʻazalkent", "gʻazalkent"
        CHINAZ = "Chinoz", "chinoz"
        BOZ = "Boʻz", "boʻz"
        YANGIABAD = "Yangiobod", "yangiobod"
        GALLAOROL = "Gʻallaorol", "gʻallaorol"
        KARMANA = "Karmana", "karmana"
        SARIOSIYO = "Sariosiyo", "sariosiyo"
        KORAKOL = "Qorakoʻl", "qorakoʻl"
        POP = "Pop", "pop"
        BESHARIK = "Beshariq", "beshariq"
        PAKHTAKOR = "Paxtakor", "paxtakor"
        KIRGULI = "Qirguli", "qirguli"
        YAYPAN = "Yaypan", "yaypan"
        KAZANKETKAN = "Qozonketkan", "qozonketkan"
        JUMA = "Juma", "juma"
        DASHTOBOD = "Dashtobod", "dashtobod"
        TOYTEPA = "Toʻytepa", "toʻytepa"
        CHIROKCHI = "Chiroqchi", "chiroqchi"

    class PaymentType(models.Choices):
        CARD = "Karta orqali", "karta orqali"
        CASH = "Naqd pul", "naqd pul"

    city = models.CharField(CityType, max_length=50)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    center = models.ForeignKey(Center, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    payment_type = models.CharField(PaymentType, max_length=50)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.id
