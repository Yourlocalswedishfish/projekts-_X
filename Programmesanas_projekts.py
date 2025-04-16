import json
import sys
from datetime import datetime

grafiks_fails = "dienas_grafiks.json"


def ievadit_lietotaju():
    vards = input("Kā tevi sauc? (Vārds): ")
    uzvards = input("Uzvārds: ")
    vecums = input("Cik tev ir gadi? ")

    if not vards.isalpha() or not uzvards.isalpha() or not vecums.isdigit():
        print("Nepareizi ievadīti dati.")
        sys.exit()

    return {
        "vards": vards,
        "uzvards": uzvards,
        "vecums": int(vecums)
    }


def ievadit_dienas_grafiku():
    izvele = input("Vai vēlies ievadīt grafiku vienai dienai vai visai nedēļai? (diena/nedēļa): ").lower()
    if izvele not in ["diena", "nedēļa"]:
        print("Nepareizi ievadīti dati.")
        sys.exit()

    dienu_saraksts = ["pirmdiena", "otrdiena", "trešdiena", "ceturtdiena", "piektdiena", "sestdiena", "svētdiena"]
    grafiks = {}

    if izvele == "diena":
        diena = input("Kurai dienai vēlies izveidot grafiku? (piem. pirmdiena): ").lower()
        if diena not in dienu_saraksts:
            print("Nepareizi ievadīti dati.")
            sys.exit()
        grafiks[diena] = ievadit_dienas_kartibu(diena)
    else:
        for diena in dienu_saraksts:
            print(f"\nIevadīsim grafiku: {diena.capitalize()}")
            grafiks[diena] = ievadit_dienas_kartibu(diena)

    return grafiks

def ievadit_dienas_kartibu(diena):
    print(f"Ievadi {diena} dienas kārtību (piemēram: Skola 8:00-14:00, Brīvs 14:00-16:00, Mācības 16:00-18:00):")
    kartiba = input()
    return kartiba


def izveidot_macibu_planu(lietotajs, grafiks):
    print("\nIzveidoju mācību laika plānu...")

    macibu_plans = {}
    for diena, kartiba in grafiks.items():
        if "brīvs" in kartiba.lower():
            macibu_plans[diena] = "Ieteikums: Mācīties 1-2h laikā, kad esi brīvs."
        elif "mācības" in kartiba.lower():
            macibu_plans[diena] = "Mācības jau ieplānotas."
        else:
            macibu_plans[diena] = "Nav brīva laika mācībām. Ieteikums: Pārskatīt dienas plānu."

    saglabat_json_faila(lietotajs, grafiks, macibu_plans)

def saglabat_json_faila(lietotajs, grafiks, macibu_plans):
    dati = {
        "lietotajs": lietotajs,
        "grafiks": grafiks,
        "macibu_plans": macibu_plans,
        "izveidots": datetime.now().isoformat()
    }

    with open(grafiks_fails, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)
    print(f"\nDati saglabāti failā: {grafiks_fails}")


if __name__ == "__main__":
    lietotajs = ievadit_lietotaju()
    grafiks = ievadit_dienas_grafiku()
    izveidot_macibu_planu(lietotajs, grafiks)