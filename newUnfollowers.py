def compare_and_update_lists(old_file="oldNonFollowers.txt", new_file="newNonFollowers.txt"):
    # 1. Alte Liste lesen und als Set speichern
    with open(old_file, "r", encoding="utf-8") as f:
        old_list = set(line.strip() for line in f if line.strip())

    # 2. Neue Liste lesen und als Set speichern
    with open(new_file, "r", encoding="utf-8") as f:
        new_list = set(line.strip() for line in f if line.strip())

    # 3. Differenz bilden (was ist in neuer Liste, aber nicht in alter?)
    difference = new_list - old_list

    # 4. Neue Einträge ausgeben
    print("Neu hinzugekommene Accounts:")
    for item in difference:
        print(item)
    
    # 5. Alte Liste überschreiben mit der aktuellen neuen Liste
    with open(old_file, "w", encoding="utf-8") as f:
        for item in new_list:
            f.write(item + "\n")
    
    # 6. Neue Liste leeren
    with open(new_file, "w", encoding="utf-8"):
        pass  # Einfach nichts reinschreiben = Datei leeren


if __name__ == "__main__":
    compare_and_update_lists("oldNonFollowers.txt", "newNonFollowers.txt")