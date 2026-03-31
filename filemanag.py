import os
import shutil

# 1. Настройка рабочей директории
WORK_DIR = os.path.join(os.getcwd(), "workdir")
os.makedirs(WORK_DIR, exist_ok=True)

# 2. Функции файлового менеджера
def create_file(filename):
    path = os.path.join(WORK_DIR, filename)
    if os.path.exists(path):
        print("Файл уже существует")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write("")
    print(f"Файл {filename} создан.")


def read_file(filename):
    path = os.path.join(WORK_DIR, filename)
    if not os.path.exists(path):
        print("Файл не найден")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\nСодержимое {filename}:\n{content}\n")


def write_file(filename, content):
    path = os.path.join(WORK_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Файл {filename} записан.")


def delete_file(filename):
    path = os.path.join(WORK_DIR, filename)
    if os.path.exists(path):
        os.remove(path)
        print(f"Файл {filename} удалён.")
    else:
        print("Файл не найден.")


def create_directory(dirname):
    path = os.path.join(WORK_DIR, dirname)
    if os.path.exists(path):
        print("Папка уже существует")
        return
    os.makedirs(path)
    print(f"Папка {dirname} создана.")


def delete_directory(dirname):
    path = os.path.join(WORK_DIR, dirname)
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Папка {dirname} удалена.")
    else:
        print("Папка не найдена.")


def list_files():
    print(f"\nСодержимое рабочей директории ({WORK_DIR}):")
    for root, dirs, files in os.walk(WORK_DIR):
        for d in dirs:
            print(f"[DIR] {os.path.relpath(os.path.join(root, d), WORK_DIR)}")
        for f in files:
            print(f"[FILE] {os.path.relpath(os.path.join(root, f), WORK_DIR)}")
    print()


def rename_file(old_name, new_name):
    old_path = os.path.join(WORK_DIR, old_name)
    new_path = os.path.join(WORK_DIR, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"{old_name} переименован в {new_name}")
    else:
        print("Файл/папка не найден.")


def copy_file(src_name, dest_name):
    src_path = os.path.join(WORK_DIR, src_name)
    dest_path = os.path.join(WORK_DIR, dest_name)
    if os.path.exists(src_path):
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        else:
            shutil.copy2(src_path, dest_path)
        print(f"{src_name} скопирован в {dest_name}")
    else:
        print("Источник не найден.")


def move_file(src_name, dest_name):
    src_path = os.path.join(WORK_DIR, src_name)
    dest_path = os.path.join(WORK_DIR, dest_name)
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(f"{src_name} перемещён в {dest_name}")
    else:
        print("Источник не найден.")


# 3. Архивация / разархивация
def archive_file_or_folder(name, archive_name):
    path = os.path.join(WORK_DIR, name)
    archive_path = os.path.join(WORK_DIR, archive_name)
    if not os.path.exists(path):
        print("Файл/папка не найдена")
        return
    # Архивируем в zip
    if os.path.isdir(path):
        shutil.make_archive(archive_path, 'zip', path)
    else:
        # Для файла создаём архив с одним файлом
        shutil.make_archive(archive_path, 'zip', root_dir=WORK_DIR, base_dir=name)
    print(f"{name} заархивирован в {archive_name}.zip")


def extract_archive(archive_name):
    archive_path = os.path.join(WORK_DIR, archive_name)
    if not os.path.exists(archive_path):
        print("Архив не найден")
        return
    shutil.unpack_archive(archive_path, WORK_DIR)
    print(f"{archive_name} разархивирован в рабочую директорию")


# 4. Пользовательский интерфейс
def menu():
    print("\n=== Мини-Файловый Менеджер ===")
    print("1. Создать файл")
    print("2. Прочитать файл")
    print("3. Записать файл")
    print("4. Удалить файл")
    print("5. Создать папку")
    print("6. Удалить папку")
    print("7. Показать содержимое")
    print("8. Переименовать файл/папку")
    print("9. Копировать файл/папку")
    print("10. Переместить файл/папку")
    print("11. Архивировать файл/папку")
    print("12. Разархивировать архив")
    print("0. Выход")


def main():
    while True:
        menu()
        choice = input("Выберите команду: ").strip()
        if choice == "1":
            create_file(input("Имя файла: "))
        elif choice == "2":
            read_file(input("Имя файла: "))
        elif choice == "3":
            write_file(input("Имя файла: "), input("Содержимое: "))
        elif choice == "4":
            delete_file(input("Имя файла: "))
        elif choice == "5":
            create_directory(input("Имя папки: "))
        elif choice == "6":
            delete_directory(input("Имя папки: "))
        elif choice == "7":
            list_files()
        elif choice == "8":
            rename_file(input("Старое имя: "), input("Новое имя: "))
        elif choice == "9":
            copy_file(input("Имя исходного файла/папки: "), input("Имя нового файла/папки: "))
        elif choice == "10":
            move_file(input("Имя исходного файла/папки: "), input("Имя нового файла/папки: "))
        elif choice == "11":
            archive_file_or_folder(input("Имя файла/папки для архивации: "), input("Имя архива (без .zip): "))
        elif choice == "12":
            extract_archive(input("Имя архива (.zip): "))
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверная команда.")


if __name__ == "__main__":
    main()