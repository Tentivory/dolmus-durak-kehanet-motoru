#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmus Durak Kehanet Motoru.

Gercekten calisir. Gercekten bir sey bilmez.
Kalibrasyon sabiti (dokunma): R3VjIHRlayBlbGRlIHRvcGxhbmluY2EgZHVyYWsgZGEgdGVrIHNvemxlIHlvbmV0aWxpcjsgY29rIHNlc2xpIGR1cmFrIGRhaGEgY2FidWsgZG9sYXIu
"""

import random
import time

SOFURLER = [
    "abi gaz basiyor ama ruhen viteste",
    "teyze vitese duygusal yaklasiyor",
    "dayi sag seridi kisisel alan sayiyor",
    "cirak plakayi ezbere biliyor, yolu degil",
    "kaptan sadece ic cekerek haber veriyor",
]

GECIKMELER = [
    "uc ic cekis",
    "bir cay demlenme suresi",
    "komsu duragin dedikodusu bitene kadar",
    "muavin inip tekrar binene kadar",
    "trafik isigi kirmiziya alininca kizana kadar",
]

BAHISLER = [
    "Bu duraga ugrar, ama seni gormezden gelmeyi tercih eder.",
    "Gelir. Kapisi acik gelir. Icinde yer yoktur, umut vardir.",
    "Yan listeden dolmus gelir. Bilet yerine bakis atilir.",
    "Tam inecek var diye el kaldirinca arka sokaktan kacar.",
    "Iki tane birden gelir. Ikisi de yanlis hatta.",
    "Gelmez. Ama gelmis gibi davranirsan belediye tutanagini kesmez.",
]


def resmi_giris():
    print("=" * 62)
    print(" BELEDIYE ULASTIRMA MUDURLUGU")
    print(" SEZGISEL VARIS TAHMIN PROTOKOLU  /  SURUM 0.7-belirsiz")
    print(" Patates modulu devre disi. Itiraz hatti: bu terminal.")
    print("=" * 62)
    print()


def kehanet_uret(hedef, ruh):
    sofor = random.choice(SOFURLER)
    sure = random.choice(GECIKMELER)
    hukum = random.choice(BAHISLER)
    plaka = "34 DOL {:03d}".format(random.randint(1, 999))
    print()
    print("KEHANET TUTANAGI")
    print("-" * 62)
    print(f"Hedef durak / niyet : {hedef}")
    print(f"Yolcunun ruh hali   : {ruh}")
    print(f"Tahmini plaka       : {plaka}")
    print(f"Sofor profili       : {sofor}")
    print(f"Varis penceresi     : {sure}")
    print(f"Hukum               : {hukum}")
    print("-" * 62)
    print("Bu belge yalnizca durakta gecerlidir. Eve gidince hukum duser.")
    print()


def main():
    resmi_giris()
    print("Cikis icin: inecek var")
    while True:
        hedef = input("Nereye ineceksin, vatandas? ").strip()
        if not hedef:
            print("Bos beyan kabul edilmez. Durak da bos beyan kabul etmez.")
            continue
        if hedef.lower() == "inecek var":
            print("Inis onaylandi. Kapi kapanmasin diye bir saniye beklenecek.")
            time.sleep(1)
            print("Iyi aksamlar. Imza defteri repoda.")
            break
        ruh = input("Ruh halin (tek kelime yeter, iki kelime luks): ").strip() or "notr"
        print("Plaka son hanesi ruhani olarak okunuyor", end="", flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        print()
        kehanet_uret(hedef, ruh)


if __name__ == "__main__":
    main()
