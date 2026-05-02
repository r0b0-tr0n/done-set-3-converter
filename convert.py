
# NextUI Done Set 3 Converter
# by r0b0-tr0n

import shutil
import sys
import zipfile
import zlib
from itertools import count
from datetime import datetime
from pathlib import Path
from contextlib import suppress

import py7zr    # pip install py7zr
import requests # pip install requests

from convert_config import SYSTEMS # convert_config.py

TAG = 'v1.0.0'
REPO = 'r0b0-tr0n/done-set-3-converter'
APP = 'Done Set 3 Converter (for NextUI etc.)'
LANG_FOOTER = 'press [ENTER] to exit'

REPO_URL = f'https://github.com/{REPO}'
RELEASE_URL = f'https://api.github.com/repos/{REPO}/releases/latest'

APP_AND_TAG = f'{APP} {TAG}'
HR = f'{"=" * len(APP_AND_TAG)}'
HEADER = f'\n{HR}\n{APP_AND_TAG}\n{HR}\n\n{REPO_URL}\n'
FOOTER_SPACER = f'{" " * ((len(APP_AND_TAG) - len(LANG_FOOTER)) // 2)}'
FOOTER = f'\n{HR}\n{FOOTER_SPACER}{LANG_FOOTER}\n{HR}\n'

IS_EXE = getattr(sys, 'frozen', False)
IS_SCRIPT = not IS_EXE
PATH = Path(sys.executable if IS_EXE else __file__).resolve()
OLD_PATH = PATH.with_suffix(PATH.suffix + '.old')
NEW_PATH = PATH.with_suffix(PATH.suffix + '.new')
DIR = PATH.parent
FILE = PATH.name

log_file = None
proceed = True
systems = []

#*** UTILS *************************************************************

def ask_yes_or_no(prompt='Proceed? (y/n) '):

    while True:
        choice = input(prompt).strip()[0:1].lower()
        if choice == 'y':
            return True
        if choice == 'n':
            return False
        prompt = '(y/n) '

def get_crc32(filepath):

    crc = 0
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            crc = zlib.crc32(chunk, crc)
    return f"{crc & 0xFFFFFFFF:08x}"

def get_latest_release():

    try:
        response = requests.get(RELEASE_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        tag = data.get('tag_name')
        exe_url = next((a['browser_download_url'] for a in data.get('assets', [])
            if a['name'].lower().endswith('.exe')), None)
        return tag, exe_url
    except Exception:
        return None, None

def log(message: str):

    global log_file
    if log_file is None:
        for i in count(1):
            potential_file = DIR / f'log{i}.txt'
            if not potential_file.exists():
                log_file = potential_file
                break
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'{message}\n')

#*** STEPS *************************************************************

def rename_system_dirs():

    global proceed, systems

    log("*** RENAMING SYSTEM DIRS ***\n")

    exists = renamed = errors = missing = 0

    for system in SYSTEMS:
        new_name = system.get("name")
        old_name = system.get("old_name")
        new_dir = DIR / new_name
        old_dir = DIR / old_name

        if new_dir.is_dir():
            log(f"[EXISTS] '{new_name}'")
            systems.append(new_name)
            exists += 1
        elif old_dir.is_dir():
            try:
                old_dir.rename(new_dir)
                log(f"[RENAMED] '{old_name}' -> '{new_name}'")
                systems.append(new_name)
                renamed += 1
            except Exception as e:
                log(f"[ERROR] renaming '{old_name}': {e}")
                errors += 1
        else:
            log(f"[MISSING] '{new_name}', '{old_name}'")
            missing += 1

    log(f"\nExists  : {exists}")
    log(f"Renamed : {renamed}")
    log(f"Missing : {missing}")
    log(f"Errors  : {errors}\n")

    if not systems:
        log("No systems to work with, stopping here...\n")
        proceed = False

def rename_subdirs():

    log("*** RENAMING SUB-DIRS ***\n")

    exists = renamed = errors = missing = 0

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("subdirs")
    ]

    for system in systems_to_process:
        name = system.get("name")
        log(f"{name}")
        system_dir = DIR / name

        for subdir in system.get("subdirs"):
            new_name = subdir.get("name")
            old_name = subdir.get("old_name")
            new_dir = system_dir / new_name
            old_dir = system_dir / old_name

            if new_dir.is_dir():
                log(f"[EXISTS] '{new_name}'")
                exists += 1
            elif old_dir.is_dir():
                try:
                    old_dir.rename(new_dir)
                    log(f"[RENAMED] '{old_name}' -> '{new_name}'")
                    renamed += 1
                except Exception as e:
                    log(f"[ERROR] renaming '{old_name}': {e}")
                    errors += 1
            else:
                log(f"[MISSING] '{new_name}' / '{old_name}'")
                missing += 1

        log("")

    if exists + renamed + missing + errors > 0:
        log(f"Exists  : {exists}")
        log(f"Renamed : {renamed}")
        log(f"Missing : {missing}")
        log(f"Errors  : {errors}\n")

def delete_subdirs():

    log("*** DELETING SUB-DIRS ***\n")

    deleted = errors = 0

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("subdirs_to_delete")
    ]

    for system in systems_to_process:
        system_dir = DIR / system.get("name")

        for subdir in system.get("subdirs_to_delete"):
            target = system_dir / subdir.get("subdir")

            if target.exists() and target.is_dir():
                try:
                    shutil.rmtree(target)
                    log(f"[DELETED] {target.relative_to(DIR)} ({subdir.get('reason')})")
                    deleted += 1
                except Exception as e:
                    log(f"[ERROR] deleting {target.relative_to(DIR)}: {e}")
                    errors += 1

    if deleted + errors > 0:
        log(f"\nDeleted : {deleted}")
        log(f"Errors  : {errors}\n")

def delete_files():

    log("*** DELETING FILES ***\n")

    skipped = deleted = errors = 0

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("files_to_delete")
    ]

    for system in systems_to_process:
        system_dir = DIR / system.get("name")

        for file in system.get("files_to_delete"):
            target = system_dir / file.get("file")
            target_crc = file.get("crc32", "").lower().strip()

            if target.exists() and target.is_file():
                try:
                    should_delete = False
                    if not target_crc:
                        should_delete = True
                    else:
                        file_crc = get_crc32(target)
                        if file_crc == target_crc:
                            should_delete = True
                        else:
                            log(f"[SKIPPED] {target.relative_to(DIR)} (CRC mismatch: {file_crc} != {target_crc})")
                            skipped += 1
                    if should_delete:
                        target.unlink()
                        log(f"[DELETED] {target.relative_to(DIR)} ({file.get('reason')})")
                        deleted += 1
                except Exception as e:
                    log(f"[ERROR] deleting {target.relative_to(DIR)}: {e}")
                    errors += 1

    if skipped + deleted + errors > 0:
        log(f"\nSkipped : {skipped}")
        log(f"Deleted : {deleted}")
        log(f"Errors  : {errors}\n")

def rename_files():

    log("*** RENAMING FILES ***\n")

    skipped = renamed = errors = 0

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("files_to_rename")
    ]

    for system in systems_to_process:
        system_dir = DIR / system.get("name")

        for file in system.get("files_to_rename"):
            target = system_dir / file.get("file")
            target_crc = file.get("crc32", "").lower().strip()

            if target.exists() and target.is_file():
                try:
                    should_rename = False
                    if not target_crc:
                        should_rename = True
                    else:
                        file_crc = get_crc32(target)
                        if file_crc == target_crc:
                            should_rename = True
                        else:
                            log(f"[SKIPPED] {target.relative_to(DIR)} (CRC mismatch: {file_crc} != {target_crc})")
                            skipped += 1
                    if should_rename:
                        new_target = system_dir / file.get("new_file")
                        if new_target.exists():
                            new_target.unlink()
                        target.rename(new_target)
                        log(f"[RENAMED] {target.relative_to(DIR)} -> {new_target.relative_to(DIR)} ({file.get('reason')})")
                        renamed += 1
                except Exception as e:
                    log(f"[ERROR] renaming {target.relative_to(DIR)}: {e}")
                    errors += 1

    if skipped + renamed + errors > 0:
        log(f"\nSkipped : {skipped}")
        log(f"Renamed : {renamed}")
        log(f"Errors  : {errors}\n")

def zip_files():

    log("*** ZIPPING FILES ***\n")

    zipped = errors = 0

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("extensions_to_zip")
    ]

    for system in systems_to_process:
        name = system.get("name")
        system_dir = DIR / name

        for ext in system.get("extensions_to_zip"):
            for file in list(system_dir.rglob(f"*{ext}")):
                clean_name = file.name[: -len(ext)]
                zip_path = file.with_name(f"{clean_name}.zip")
                try:
                    if zip_path.exists():
                        zip_path.unlink()
                    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as new_zip:
                        new_zip.write(file, arcname=file.name)
                    file.unlink()
                    log(f"[ZIPPED] {file.relative_to(DIR)}")
                    zipped += 1
                except Exception as e:
                    log(f"[ERROR] zipping {file.relative_to(DIR)}: {e}")
                    errors += 1

    if zipped + errors > 0:
        log(f"\nZipped : {zipped}")
        log(f"Errors : {errors}\n")

def fix_mrdo():

    log("*** FIXING MR. DO! NAME DISPLAY ***\n")

    skipped = created = errors = 0    

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("fix_mrdo")
    ]

    for system in systems_to_process:
        name = system.get("name")
        system_dir = DIR / name
        if name == "Super Nintendo Entertainment System (SFC)":
            system_dir = system_dir / "0)More Games ---"
        file = system_dir / "map.txt"
        if file.exists():
            log(f"[SKIPPED] {file.relative_to(DIR)} already exists")
            skipped += 1
        else:
            try:
                file.write_text(f"Mr. Do!.zip\tMr. Do!\n")
                log(f"[CREATED] {file.relative_to(DIR)}")
                created += 1
            except Exception as e:
                log(f"[ERROR] creating {file.relative_to(DIR)}: {e}")
                errors += 1

    if skipped + created + errors > 0:
        log(f"\nSkipped : {skipped}")
        log(f"Created : {created}")        
        log(f"Errors  : {errors}\n")

def convert_7zips():

    log("*** CONVERTING 7ZIPS ***\n")

    converted = errors = 0

    systems_to_process = [
        s for s in SYSTEMS
        if s.get("name") in systems
        and s.get("convert_7zips")
    ]

    for system in systems_to_process:
        system_dir = DIR / system.get("name")

        for file in list(system_dir.rglob('*.7z')):
            zip_path = file.with_suffix('.zip')
            temp_extract_dir = file.parent / f"temp_{file.stem}"
            try:
                if zip_path.exists():
                    zip_path.unlink()
                with py7zr.SevenZipFile(file, mode='r') as archive:
                    archive.extractall(path=temp_extract_dir)
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as new_zip:
                    for file_to_zip in temp_extract_dir.rglob('*'):
                        if file_to_zip.is_file():
                            new_zip.write(file_to_zip, file_to_zip.relative_to(temp_extract_dir))
                file.unlink()
                shutil.rmtree(temp_extract_dir)
                converted += 1
                log(f"[CONVERTED] {file.relative_to(DIR)}")
            except Exception as e:
                log(f"[ERROR] converting {file.relative_to(DIR)}: {e}")
                if temp_extract_dir.exists():
                    shutil.rmtree(temp_extract_dir)
                errors += 1

    if converted + errors > 0:
        log(f"\nConverted : {converted}")
        log(f"Errors    : {errors}\n")

#*** CORE **************************************************************

def clean():

    if IS_EXE:
        with suppress(Exception):
            OLD_PATH.unlink(missing_ok=True)

def update():

    global proceed

    if IS_SCRIPT:
        return

    print('Checking for update...', end=' ', flush=True)
    tag, download_url = get_latest_release()
    if not tag or not download_url:
        print('check failed.\n')
        return
    elif tag == TAG:
        print('none found.\n')
        return
    print(f'new: {tag}')
    if not ask_yes_or_no('Update now? (y/n) '):
        print('Skipping update.\n')
        return

    print('Updating...', end='', flush=True)
    try:
        if NEW_PATH.exists():
            NEW_PATH.unlink()
        r = requests.get(download_url, stream=True)
        r.raise_for_status()
        with open(NEW_PATH, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    print('.', end='', flush=True)
        if OLD_PATH.exists():
            OLD_PATH.unlink()
        PATH.rename(OLD_PATH)
        NEW_PATH.rename(PATH)
        print(' done.\nPlease re-run the EXE to use the new version.')
        proceed = False
    except Exception as e:
        print(f' failed: {e}\n')
        if OLD_PATH.exists() and not PATH.exists():
            with suppress(Exception):
                OLD_PATH.rename(PATH)

def convert():

    if not proceed:
        return

    print(f'Ready to convert: {DIR}')
    if not ask_yes_or_no('Proceed with conversion? (y/n) '):
        print("Conversion canceled.")
        return

    print('Converting, please wait...', end='', flush=True)
    log(HEADER)
    log(f"Started at: {datetime.now().isoformat(sep=' ', timespec='seconds')}\n")
    log(f"Directory: {DIR}\n")

    rename_system_dirs()
    if proceed:
        rename_subdirs()
        delete_subdirs()
        delete_files()
        rename_files()
        fix_mrdo()
        zip_files()
        convert_7zips()

    log(f"Finished at: {datetime.now().isoformat(sep=' ', timespec='seconds')}")
    print(f"done.\n\nPlease see {log_file.name} for details.")

if __name__ == "__main__":

    print(HEADER)
    clean()
    update()
    convert()
    input(FOOTER)
