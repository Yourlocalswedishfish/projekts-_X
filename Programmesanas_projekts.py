import json
import sys

grafiks_fails = "dienas_grafiks.json"


def ievadit_lietotaju(): #Prasa lietotāja vārdu, uzvārdu un vecumu.
    vards = input("Kāds ir tavs vārds: ")
    uzvards = input("Kāds ir tavs uzvārds: ")
    vecums = input("Cik tev ir pilni gadi? ")

    return {
        "vards": vards,
        "uzvards": uzvards,
        "vecums": int(vecums)
    }


def ievadit_dienas_grafiku(): #Prasa lietotājam kādu grafiku veidos, dienas vai nedēļas grafiku.
    izvele = input("Vai vēlies ievadīt grafiku vienai dienai vai visai nedēļai? (Raksti diena, nedēļa): ").lower()
    if izvele not in ["diena", "nedēļa"]:
        print("Nepareizi ievadīti dati.")
        sys.exit()

    dienu_saraksts = ["pirmdiena", "otrdiena", "trešdiena", "ceturtdiena", "piektdiena", "sestdiena", "svētdiena"]
    grafiks = {}

    if izvele == "diena":
        diena = input("Kurai dienai vēlies izveidot grafiku? (piemēram: pirmdiena): ").lower()#Piedāvā lietotājam kurai dienai vēlās izveidot grafiku.
        if diena not in dienu_saraksts:
            print("Nepareizi ievadīti dati.")
            sys.exit()
        grafiks[diena] = ievadit_dienas_kartibu(diena)
    else:
        for diena in dienu_saraksts:
            print(f"\nIevadīsim grafiku: {diena.capitalize()}")
            grafiks[diena] = ievadit_dienas_kartibu(diena)

    return grafiks

def ievadit_dienas_kartibu(diena): #Prasa lietotājam lai ievada dienas kārtību konkrētajai dienai kuru izvēlējās cilvēks.
    print(f"Ievadi {diena} dienas kārtību (piemēram: Skola 8:00-14:00, Brīvs 14:00-16:00, Mācības 16:00-18:00):")
    kartiba = input()
    return kartiba


def izveidot_macibu_planu(lietotajs, grafiks): #iesaka lietotājam kurā brīdī un kad atrast laiku mācībām.
    print("\nIzveidoju mācību laika plānu...")

    macibu_plans = {}
    for diena, kartiba in grafiks.items(): #Atgriež
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
    }

    with open(grafiks_fails, "w", encoding="utf-8") as f: #parnes visus datus uz json failu.
        json.dump(dati, f, indent=4, ensure_ascii=False)
    print(f"\nDati saglabāti failā: {grafiks_fails}")


if __name__ == "__main__":
    lietotajs = ievadit_lietotaju()
    grafiks = ievadit_dienas_grafiku()
    izveidot_macibu_planu(lietotajs, grafiks)