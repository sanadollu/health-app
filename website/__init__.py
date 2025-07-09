from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
DB_NAME = "database.db"

from .models import Doktor, Hasta, Islem, Sehir, Otel
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = 'ashko kuhsko'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    with app.app_context():
        admin = Hasta(sigorta_no='admin', isim_soyisim='admin',
                      sifre=generate_password_hash("1234", method='pbkdf2:sha256'))
        db.session.add(admin)
        sehir1 = Sehir(adı='antalya')
        db.session.add(sehir1)
        sehir2 = Sehir(adı='istanbul')
        db.session.add(sehir2)
        sehir3 = Sehir(adı='izmir')
        db.session.add(sehir3)
        db.session.commit()

        islem1 = Islem(isim='estetik_cerrahi')
        islem2 = Islem(isim='goz_hastaliklari')
        islem3 = Islem(isim='agiz_dis_sagligi')
        islem4 = Islem(isim='akupunktur')
        db.session.add(islem1)
        db.session.add(islem2)
        db.session.add(islem3)
        db.session.add(islem4)

        db.session.commit()

        doktor1 = Doktor(isim_soyisim="Taner Ölmez", telno="05367728096", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-81b7de06-af33-437a-8370-456e0590011f.jpg",
                         hastane="Memorial Ataşehir Hastanesi", ucret=410, oy=4.3, oy_sayisi=12, dep_id=islem2.id, sehir_id=sehir2.id)
        doktor2 = Doktor(isim_soyisim="Onur Tuna", telno="05324581229", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-e1014a04-5aa1-4586-9ee6-191fc726942a.jpg",
                         hastane="Özel Levent Hastanesi", ucret=1520, oy=4.7, oy_sayisi=20, dep_id=islem1.id, sehir_id=sehir2.id)
        doktor3 = Doktor(isim_soyisim="Sinem Ünsal", telno="05352016589", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-a1bab0b4-0e3a-450c-bc92-03991d8fef46.jpg",
                         hastane="Medicana International İstanbul Hastanesi", ucret=635, oy=3.2, oy_sayisi=6, dep_id=islem3.id, sehir_id=sehir2.id)
        doktor4 = Doktor(isim_soyisim="Kim Seokjin", telno="05542051265", foto="https://img.wattpad.com/story_parts/1012137758/images/165c24790f0c205e551823402763.jpg",
                         hastane="İstinye Liv Hospital", ucret=780, oy=4.8, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir2.id)
        doktor5 = Doktor(isim_soyisim="Seda Bakan", telno="05326532525", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-914-act-image-562718c4-70f4-4ec7-bfa3-2271cc73f172.jpg",
                         hastane="Özel Güngören Hastanesi", ucret=410, oy=4.1, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir3.id)
        doktor6 = Doktor(isim_soyisim="Kim Taehyung", telno="05356821515", foto="https://i.pinimg.com/originals/df/ef/81/dfef8114fe75efba2dea10ab074cbc55.jpg",
                         hastane="Medicana International Izmir Hastanesi", ucret=1180, oy=4.0, oy_sayisi=32, dep_id=islem1.id, sehir_id=sehir3.id)
        doktor7 = Doktor(isim_soyisim="Fırat Altunmeşe", telno="05421520361", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-a1e56cce-6ed8-4540-84a6-b99a985b8742.jpg",
                         hastane="Özel Egepol Hastanesi", ucret=580, oy=3.1, oy_sayisi=7, dep_id=islem1.id, sehir_id=sehir3.id)
        doktor8 = Doktor(isim_soyisim="Hakan Kurtaş", telno="05246352164", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-915-act-image-45d1b77a-25f6-4ee8-8373-f25ff151b33a.jpg",
                         hastane="Myvia Genç Yaşam", ucret=200, oy=3.7, oy_sayisi=3, dep_id=islem3.id, sehir_id=sehir3.id)
        doktor9 = Doktor(isim_soyisim="Doctor Strange", telno="05212031425", foto="https://i.pinimg.com/originals/83/1f/01/831f015888b5a0cd588e89b865ed12d0.jpg",
                         hastane="Antalya Yaşam Hastanesi", ucret=2400, oy=4.5, oy_sayisi=150, dep_id=islem4.id, sehir_id=sehir1.id)
        doktor10 = Doktor(isim_soyisim="Jeon Jungkook", telno="05301253645", foto="https://img.wattpad.com/63c9eb54070cfaafac6445871a8a3a4efb964de8/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3457426a7153394b6f73656453673d3d2d313039353535323832352e313638656636323033373663313164303130333437313839363436322e6a7067?s=fit&w=720&h=720",
                          hastane="Rich Hospital", ucret=1220, oy=5, oy_sayisi=20, dep_id=islem1.id, sehir_id=sehir1.id)
        doktor11 = Doktor(isim_soyisim="Hayal Köseoğlu", telno="05354521656", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-24ae5dc5-54c0-4d0d-a7dc-6cd19c32e8b3.jpg",
                          hastane="Özel Olimpos Hastanesi", ucret=540, oy=3.9, oy_sayisi=13, dep_id=islem3.id, sehir_id=sehir1.id)
        doktor12 = Doktor(isim_soyisim="Adil Erinç", telno="05548541252", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-4d7bbb7f-0b0b-4fc7-a768-7f28f98e9e31.jpg",
                          hastane="Medical Park Antalya", ucret=230, oy=4.3, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir1.id)
        
        doktor13 = Doktor(isim_soyisim="Bihter Dinçel", telno="05548541252", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-09f40534-d041-4434-aee3-5603e775638c.jpg",
                          hastane="Medical Park Antalya", ucret=2200, oy=4.5, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir1.id)
        doktor14 = Doktor(isim_soyisim="Korhan Herduran", telno="05689524625", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-8fa378a5-44da-4b22-9c9e-8e02bc017f57.jpg",
                          hastane="Özel Olimpos Hastanesi", ucret=1298, oy=3.3, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir1.id)
        doktor15 = Doktor(isim_soyisim="Merve Bulut", telno="05254587744", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-916-act-image-ebe02aa3-9e1e-4e9e-b447-e46695cb97ca.jpg",
                          hastane="Antalya Yaşam Hastanesi", ucret=1025, oy=4.2, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir1.id)
        doktor16 = Doktor(isim_soyisim="Serkan Keskin", telno="05985263524", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-996-act-image-2032ebcc-36d3-4695-b720-bf76750a7f58.jpg",
                          hastane="Özel Olimpos Hastanesi", ucret=850, oy=3.4, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir1.id)
        doktor17 = Doktor(isim_soyisim="Murat Aygen", telno="05248563154", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-764-act-image-3fb11e1d-17ba-49d1-b41a-ac504323b84e.jpg",
                          hastane="Rich Hospital", ucret=400, oy=4.3, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir1.id)
        doktor18 = Doktor(isim_soyisim="Hazal Türesan", telno="05547852011", foto="https://tejedd76pluu.merlincdn.net/resize/700x932//Programlar/Mucize-Doktor/Oyuncular/Mucize-Doktor-act-image-43825733-b9f6-48c2-820f-3542447a092c.jpg",
                          hastane="Antalya Yaşam Hastanesi", ucret=215, oy=4.5, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir1.id)
        doktor19 = Doktor(isim_soyisim="Timuçin Esen", telno="05785424510", foto="https://i.kanald.com.tr/i/kanald/100/200x286/5dee379926789936f889fe83",
                          hastane="Rich Hospital", ucret=120, oy=2.3, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir1.id)
        doktor20 = Doktor(isim_soyisim="Okan Yalabalik", telno="05895412265", foto="https://i.kanald.com.tr/i/kanald/100/200x286/5dee383c7470f73380af33b1",
                          hastane="Medical Park Antalya", ucret=68, oy=4.3, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir1.id)
        doktor21 = Doktor(isim_soyisim="Ebru Özkan", telno="05478514999", foto="https://i.kanald.com.tr/i/kanald/100/200x286/5dee38a0e94fb72dec23a022",
                          hastane="Antalya Yaşam Hastanesi", ucret=255, oy=4.4, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir1.id)
        doktor22 = Doktor(isim_soyisim="Kaan Yildirim", telno="05012541102", foto="https://i.kanald.com.tr/i/kanald/100/200x286/5dee390f7470f73380af33b7",
                          hastane="Rich Hospital", ucret=620, oy=4.4, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir1.id)
        doktor23 = Doktor(isim_soyisim="Aytaç Şaşmaz", telno="05652135252", foto="https://i.kanald.com.tr/i/kanald/100/200x286/5dee396d61361f223cb27438",
                          hastane="Medical Park Antalya", ucret=730, oy=4.8, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir1.id)
        doktor24 = Doktor(isim_soyisim="Damla Colbay", telno="05525525252", foto="https://i.kanald.com.tr/i/kanald/100/200x286/5dee39da26789936f889fe88",
                          hastane="Özel Olimpos Hastanesi", ucret=500, oy=3.3, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir1.id)

        doktor25 = Doktor(isim_soyisim="Gamze Topuz", telno="05623214520", foto="https://img-s1.onedio.com/id-596d30b57e6e266c1cebd3e0/rev-0/w-620/f-jpg/s-05b1a5940bc3a966b38c63edde56b88788fa23fc.jpg",
                          hastane="Memorial Ataşehir Hastanesi", ucret=200, oy=2.3, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir2.id)
        doktor26 = Doktor(isim_soyisim="Aysun Kayaci", telno="05478596857", foto="https://i.cnnturk.com/i/cnnturk/75/0x555/54857220f97adb1aa472e5fa",
                          hastane="Medicana International İstanbul Hastanesi", ucret=230, oy=4.3, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir2.id)
        doktor27 = Doktor(isim_soyisim="Devrim Nas", telno="05102536989", foto="https://i2.cnnturk.com/i/cnnturk/75/600x0/54857220f97adb1aa472e5ec",
                          hastane="İstinye Liv Hospital", ucret=650, oy=4.8, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir2.id)
        doktor28 = Doktor(isim_soyisim="Melike Guner", telno="05555555555", foto="https://pbs.twimg.com/profile_images/378800000323476514/55b198099cd68e3e91cc3c527ec15246_400x400.jpeg",
                          hastane="Özel Levent Hastanesi", ucret=850, oy=4.8, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir2.id)
        doktor29 = Doktor(isim_soyisim="Kutsi", telno="05451206565", foto="https://i4.hurimg.com/i/hurriyet/75/0x0/5efd779545d2a04258b8f1bc.jpg",
                          hastane="Medicana International İstanbul Hastanesi", ucret=420, oy=4.3, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir2.id)
        doktor30 = Doktor(isim_soyisim="Bekir Aksoy", telno="05589521302", foto="https://i4.hurimg.com/i/hurriyet/75/0x0/5efd779545d2a04258b8f1b8.jpg",
                          hastane="Memorial Ataşehir Hastanesi", ucret=520, oy=4.3, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir2.id)
        doktor31 = Doktor(isim_soyisim="Yesim Bozoglu", telno="05685942513", foto="https://i4.hurimg.com/i/hurriyet/75/0x0/5efd779645d2a04258b8f1c8.jpg",
                          hastane="Özel Levent Hastanesi", ucret=360, oy=2.1, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir2.id)
        doktor32 = Doktor(isim_soyisim="Mehmet Aslan", telno="02568952103", foto="https://i4.hurimg.com/i/hurriyet/75/0x0/5efd779745d2a04258b8f1d4.jpg",
                          hastane="İstinye Liv Hospital", ucret=150, oy=3.2, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir2.id)
        doktor33 = Doktor(isim_soyisim="Hugh Laurie", telno="05896563259", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/01-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/8d0d985c9ce4e6409082a8cbbe5f59348a8bc6ed/img.jpeg",
                          hastane="Memorial Ataşehir Hastanesi", ucret=1020, oy=4.3, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir2.id)
        doktor34 = Doktor(isim_soyisim="Jennifer Morrison", telno="05874521545", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/08-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/98ecd2870a6937e7c43b325494ccf554a34e508d/img.jpeg",
                          hastane="Özel Levent Hastanesi", ucret=780, oy=4.1, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir2.id)
        doktor35 = Doktor(isim_soyisim="Omar Epps", telno="05985632485", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/10-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/35c45b8b34d6e646190603ffb9987a47f132f179/img.jpeg",
                          hastane="Medicana International İstanbul Hastanesi", ucret=900, oy=4.4, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir2.id)
        doktor36 = Doktor(isim_soyisim="Jesse Spencer", telno="05254871001", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/12-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/03dc3a72c436f602b979bf10440affd4e227f56b/img.jpeg",
                          hastane="İstinye Liv Hospital", ucret=600, oy=4.3, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir2.id)


        doktor37 = Doktor(isim_soyisim="Olivia Wilde", telno="05562010068", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/14-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/4d590bbac3d6bc103d68f0881ed817595e985afe/img.jpeg",
                          hastane="Özel Güngören Hastanesi", ucret=1230, oy=4.3, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir3.id)
        doktor38 = Doktor(isim_soyisim="Amber Tamblyn", telno="05985263147", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/22-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/fcc681d8fc9fbb5fac69c84dee32c9c50da747e0/img.jpeg",
                          hastane="Myvia Genç Yaşam", ucret=330, oy=1.8, oy_sayisi=10, dep_id=islem1.id, sehir_id=sehir3.id)
        doktor39 = Doktor(isim_soyisim="Charlyne Yi", telno="05111111111", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/24-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/430d5430fb75a1359df2d94673d6df643529ec7d/img.jpeg",
                          hastane="Medicana International Izmir Hastanesi", ucret=120, oy=1.2, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir3.id)
        doktor40 = Doktor(isim_soyisim="Anne Dudek", telno="05896324517", foto="https://static.sky.it/images_static/cinema/tv-show/2020/04/15/house-cast-ieri-oggi/26-dr-house-cast-prima-e-dopo-getty.jpg.transform/gallery-vertical-desktop-2x/423b7562bfc2196d60666ccb966d40253ffd451f/img.jpeg",
                          hastane="Myvia Genç Yaşam", ucret=210, oy=4.3, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir3.id)
        doktor41 = Doktor(isim_soyisim="Zack Braff", telno="05985642103", foto="https://imageresizer.static9.net.au/zSKjHBGBTluyjlBhleizlsRX8Gg=/0x207:1982x2189/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2Fdbf5570e-a91e-4185-b5fd-472c369f5620",
                          hastane="Özel Egepol Hastanesi", ucret=125, oy=2.9, oy_sayisi=10, dep_id=islem2.id, sehir_id=sehir3.id)
        doktor42 = Doktor(isim_soyisim="Donald Faison", telno="05569859966", foto="https://imageresizer.static9.net.au/geGoVJeMmVOtyTxYonFh-7XuQX8=/0x509:1982x2491/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2Fb3203555-be09-4a52-859a-69886271a076",
                          hastane="Özel Güngören Hastanesi", ucret=215, oy=4.3, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir3.id)
        doktor43 = Doktor(isim_soyisim="Sarah Chalke", telno="05888888888", foto="https://imageresizer.static9.net.au/Ih79kUdartXH_5jTW73T-slfn_E=/0x126:1982x2108/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2F431e640a-7961-4e2f-9f42-73d92e3ac63b",
                          hastane="Medicana International Izmir Hastanesi", ucret=320, oy=4.8, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir3.id)
        doktor44 = Doktor(isim_soyisim="John McGinley", telno="05202546321", foto="https://imageresizer.static9.net.au/gXYSja6eGTH5KqIdBkIznkflTOI=/0x153:1995x2148/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2F17df88e7-8f94-4dc4-a20f-059acfd251f0",
                          hastane="Özel Egepol Hastanesi", ucret=220, oy=3.5, oy_sayisi=10, dep_id=islem3.id, sehir_id=sehir3.id)
        doktor45 = Doktor(isim_soyisim="Ken Jenkins", telno="05892563000", foto="https://imageresizer.static9.net.au/4IWf1zDKhsmNllyhwe7RZWC-AXo=/0x180:1995x2175/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2Fc7ad5130-9568-4019-a4db-d50c29a36fa9",
                          hastane="Özel Güngören Hastanesi", ucret=720, oy=3.8, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir3.id)
        doktor46 = Doktor(isim_soyisim="Judy Reyes", telno="05548487521", foto="https://imageresizer.static9.net.au/N1n3VpBYZwlS3lQo3ZVyGZMQ7XU=/0x240:1982x2222/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2F2b730206-e1b3-4480-bae2-948cd25eea11",
                          hastane="Medicana International Izmir Hastanesi", ucret=860, oy=4.3, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir3.id)
        doktor47 = Doktor(isim_soyisim="Neil Flynn", telno="05846301254", foto="https://imageresizer.static9.net.au/TROuKBcSxpF4iRadzkCphvsJyqw=/0x102:2032x2134/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2F5c066973-939e-4801-bd19-80d975e3a437",
                          hastane="Özel Egepol Hastanesi", ucret=940, oy=4.8, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir3.id)
        doktor48 = Doktor(isim_soyisim="Sam Llyod", telno="05985336520", foto="https://imageresizer.static9.net.au/hHRA96XpQEg9Q_IQlCWXUue-Z3E=/106x182:1594x1671/1200x0/https%3A%2F%2Fprod.static9.net.au%2Ffs%2F17d6be5f-195e-4026-ac4c-18ea5b27e163",
                          hastane="Myvia Genç Yaşam", ucret=680, oy=4.9, oy_sayisi=10, dep_id=islem4.id, sehir_id=sehir3.id)
                          
        
        db.session.add(doktor1)
        db.session.add(doktor2)
        db.session.add(doktor3)
        db.session.add(doktor4)
        db.session.add(doktor5)
        db.session.add(doktor6)
        db.session.add(doktor7)
        db.session.add(doktor8)
        db.session.add(doktor9)
        db.session.add(doktor10)
        db.session.add(doktor11)
        db.session.add(doktor12)
        db.session.add(doktor13)
        db.session.add(doktor14)
        db.session.add(doktor15)
        db.session.add(doktor16)
        db.session.add(doktor17)
        db.session.add(doktor18)
        db.session.add(doktor19)
        db.session.add(doktor20)
        db.session.add(doktor21)
        db.session.add(doktor22)
        db.session.add(doktor23)
        db.session.add(doktor24)
        db.session.add(doktor25)
        db.session.add(doktor26)
        db.session.add(doktor27)
        db.session.add(doktor28)
        db.session.add(doktor29)
        db.session.add(doktor30)
        db.session.add(doktor31)
        db.session.add(doktor32)
        db.session.add(doktor33)
        db.session.add(doktor34)
        db.session.add(doktor35)
        db.session.add(doktor36)
        db.session.add(doktor37)
        db.session.add(doktor38)
        db.session.add(doktor39)
        db.session.add(doktor40)
        db.session.add(doktor41)
        db.session.add(doktor42)
        db.session.add(doktor43)
        db.session.add(doktor44)
        db.session.add(doktor45)
        db.session.add(doktor46)
        db.session.add(doktor47)
        db.session.add(doktor48)

        otel1 = Otel(isim="Hotel Su Aqualand", yildiz_sayisi=5,toplam_yildiz = 15, ucret=4243, foto="https://cdnturint.touristica.com.tr/otel-resimleri/v1.00/sunis-hotel-su/375x375/sunis-hotel-genel-(13)_136609.JPG", telno="02422490700", sehir_id=sehir1.id)
        otel2 = Otel(isim="Ramada Plaza Antalya", yildiz_sayisi=5,toplam_yildiz = 12, ucret=3060, foto="https://imgcy.trivago.com/c_lfill,d_dummy.jpeg,e_sharpen:60,f_auto,h_360,q_auto,w_360/itemimages/37/71/37711_v8.jpeg", telno="02422491111", sehir_id=sehir1.id)
        otel3 = Otel(isim="Prenses Sealine Beach Hotel", yildiz_sayisi=3,toplam_yildiz = 24, ucret=547, foto="https://lh3.googleusercontent.com/p/AF1QipOJEZQNC7hKbFNb4LAUZ5ia5LgpgiujJrvo2I3-=s1360-w1360-h1020-rw", telno="05342188422", sehir_id=sehir1.id)
        otel4 = Otel(isim="LemonPark House", yildiz_sayisi=4,toplam_yildiz = 13, ucret=2499, foto="https://images.odamax.com/img/1024x768/odamax/image/upload/ZmlsZU5hbWU9cGhvdG81ODA1NDkzNTI0Nzk0MjkxOTYz_20210525114515.jpg", telno="02422590874", sehir_id=sehir1.id)
        otel5 = Otel(isim="Doubletree By Hilton Hotel", yildiz_sayisi=5,toplam_yildiz = 15, ucret=3420, foto="https://ak-d.tripcdn.com/images/220i1g000001hd0g10182_Z_1100_824_R5_Q70_D.jpg", telno="02129999600", sehir_id=sehir2.id)
        otel6 = Otel(isim="Ramada Plaza By Wyndham", yildiz_sayisi=5,toplam_yildiz = 11, ucret=4060, foto="https://lh3.googleusercontent.com/proxy/OmvQ38bM_e5atReuSf8Sdat_70QCZB_N2iccXi33PjGSbsgRaOuudPpfu82Kz1dQFqp9QEQEujhD0UKfuxcNsNNA1pwwXimXIBICSbIdEu63kqTrIOyGytw3e96l8mSfyzG53bnVP9AcqQPNBeHKbfBQ3WI=s1360-w1360-h1020-rw", telno="02123154444", sehir_id=sehir2.id)
        otel7 = Otel(isim="Park Dedeman Bostanci", yildiz_sayisi=4,toplam_yildiz = 9, ucret=1770, foto="https://imgkit.otelz.com/turkey/istanbul/atasehir/parkdedemanbostancihotel0d3eceb4.jpg", telno="02162514500", sehir_id=sehir2.id)
        otel8 = Otel(isim="Four Points By Sheraton Istanbul", yildiz_sayisi=4,toplam_yildiz = 14, ucret=3266, foto="https://www.otimsan.com/dosyalar/2020/02/427A954E-F41A-4B45-ACE7-A79490259199.jpeg", telno="02123217171", sehir_id=sehir2.id)
        otel9 = Otel(isim="Best Western Plus Hotel", yildiz_sayisi=4,toplam_yildiz = 17, ucret=3410, foto="https://cdng.jollytur.com/files/cms/media/hotel/a5ce5235-1c76-4063-bf4b-bd41f5795fbf.jpg", telno="02324891500", sehir_id=sehir3.id)
        otel10 = Otel(isim="Swissotel Buyuk Efes", yildiz_sayisi=5,toplam_yildiz = 11, ucret=5874, foto="https://a.travel-assets.com/ugc/hotel-reviews/90AACBCBF37BB908BA4EF93E761A0B897795093F1667202197506.jpg?resize=360:*", telno="02324140000", sehir_id=sehir3.id)
        otel11 = Otel(isim="Izmir Marriott Hotel", yildiz_sayisi=3,toplam_yildiz = 10, ucret=1532, foto="https://sealthedealtravels.com/wp-content/uploads/2022/06/20220505_173928-1024x1024.jpg?ezimgfmt=ngcb8/notWebP", telno="02324970000", sehir_id=sehir3.id)
        otel12 = Otel(isim="Anemon Ege", yildiz_sayisi=4,toplam_yildiz = 15, ucret=1408, foto="https://www.anemonhotels.com/images/oteller/malatya_00366.jpg.thumb.jpg", telno="02323734862", sehir_id=sehir3.id)

        db.session.add(otel1)
        db.session.add(otel2)
        db.session.add(otel3)
        db.session.add(otel4)
        db.session.add(otel5)
        db.session.add(otel6)
        db.session.add(otel7)
        db.session.add(otel8)
        db.session.add(otel9)
        db.session.add(otel10)
        db.session.add(otel11)
        db.session.add(otel12)

        db.session.commit()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # where to go when not logged in
    login_manager.init_app(app)

    # telling flask which user we are looking for
    @login_manager.user_loader
    def load_user(id):
        return Hasta.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
