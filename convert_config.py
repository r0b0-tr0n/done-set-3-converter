SYSTEMS = [
    {
        "name": "Atari 2600 (A2600)",
        "old_name": "ATARI",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (Atari 2600)",
            },
            {
                "name": "1)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (Atari 2600)",
            },
            {
                "name": "2)Prototypes ---",
                "old_name": "Prototype (Atari 2600)",
            },
        ],
        "files_to_delete": [
            {
                "file": "Mr. Do!.zip",
                "reason": "mislabeled, alt. dump of Mr. Do!'s Castle",
                "crc32": "41FE1F26",
            },
        ],
        "fix_mrdo": True,
    },
    {
        "name": "Colecovision (COLECO)",
        "old_name": "COLECO",
        "convert_7zips": True,
        "fix_mrdo": True,
    },
    {
        "name": "Commodore 64 (C64)",
        "old_name": "COMMODORE",
        "subdirs": [
            {
                "name": "0)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (Commodore 64)",
            },
        ],
        "convert_7zips": True,
    },
    {
        "name": "Nintendo Entertainment System (FC)",
        "old_name": "FC",
        "subdirs": [
            {
                "name": "00)More Games ---",
                "old_name": "All but the Best (NES)",
            },
            {
                "name": "01)Translations ---",
                "old_name": "Translated (NES)",
            },
            {
                "name": "02)Unlicensed & Homebrews ---",
                "old_name": "Unlicenced and Homebrew (NES)",
            },
            {
                "name": "03)Hacks ---",
                "old_name": "Hacks (NES)",
            },
        ],
        "files_to_delete": [
            {
                "file": "gamelist.Missing.Serial.txt",
                "reason": "clutter",
                "crc32": "77B5F2D6",
            },
        ],
        "extensions_to_zip": [".nes"],
    },
    {
        "name": "Famicom Disk System (FDS)",
        "old_name": "FDS",
        "subdirs": [
            {
                "name": "0)Translations ---",
                "old_name": "Translated (Famicom Disk System)",
            },
            {
                "name": "1)Unlicensed ---",
                "old_name": "Unlicensed (Famicom Disk System)",
            },
        ],
        "files_to_delete": [
            {
                "file": "Family Computer Golf Tournament - Japan Course.fds",
                "reason": "mislabeled, actually Golf",
                "crc32": "CE3404A8",
            },
            {
                "file": "0)Translations ---/Eggerland (Translated En).fds",
                "reason": "duplicate of Eggerland in main folder",
                "crc32": "8DF6CAB8",
            },
            {
                "file": "1)Unlicensed ---/Golf, The - Bishoujo Classic (Unl).fds",
                "reason": "mislabeled, actually Golf",
                "crc32": "CE3404A8",
            },
        ],
        "files_to_rename": [
            {
                "file": "Eggerland - Souzou heno Tabidachi.fds",
                "new_file": "Eggerland.fds",
                "reason": "mislabeled, just regular Eggerland",
                "crc32": "8DF6CAB8",
            },
        ],
        "extensions_to_zip": [".fds"],
    },
    {
        "name": "Atari 5200 (A5200)",
        "old_name": "FIFTYTWOHUNDRED",
    },
    {
        "name": "Game Boy (GB)",
        "old_name": "GB",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (Gameboy)",
            },
            {
                "name": "1)Translations ---",
                "old_name": "Translations (Gameboy)",
            },
            {
                "name": "2)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (Gameboy)",
            },
        ],
        "files_to_delete": [
            {
                "file": "0)More Games ---/Daffy Duck.zip",
                "reason": "duplicate, keeping SGB enhanced version",
                "crc32": "C17FF922",
            },
            {
                "file": "2)Unlicensed & Homebrews ---/Quartet.7z",
                "reason": "duplicate, older version",
                "crc32": "67D32B9A",
            },
        ],
        "files_to_rename": [
            {
                "file": "0)More Games ---/Lock n' Chase ~ Lock 'n' Chase.zip",
                "new_file": "0)More Games ---/Lock 'n' Chase.zip",
                "reason": "fixing name",
                "crc32": "A959AA4C",
            },
        ],
        "convert_7zips": True,
        "fix_mrdo": True,
    },
    {
        "name": "Game Boy Advance (MGBA)",
        "old_name": "GBA",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All of the Rest of the Best but Not the Rest of All (GameBoy Advance)",
            },
            {
                "name": "1)Translations ---",
                "old_name": "Translations (GameBoy Advance)",
            },
            {
                "name": "2)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (GameBoy Advance)",
            },
            {
                "name": "3)Hacks ---",
                "old_name": "Hacks (GameBoy Advance)",
            },
            {
                "name": "4)Pokémon Hacks ---",
                "old_name": "PokemonHacks (GameBoy Advance)",
            },
        ],
        "subdirs_to_delete": [
            {
                "subdir": "0)More Games ---/.game_config",
                "reason": "clutter",
            },
            {
                "subdir": "2)Unlicensed & Homebrews ---/.game_config",
                "reason": "clutter",
            },
        ],
        "files_to_delete": [
            {
                "file": "2)Unlicensed & Homebrews ---/Super Bust-A-Move (USA) (En,Fr,Es).7z",
                "reason": "duplicate, exists in main folder",
                "crc32": "65BE60B0",
            },
        ],
        "extensions_to_zip": [".gba"],
        "convert_7zips": True,
    },
    {
        "name": "Game Boy Color (GBC)",
        "old_name": "GBC",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (GameBoy Color)",
            },
            {
                "name": "1)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (GameBoy Color)",
            },
            {
                "name": "2)Hacks ---",
                "old_name": "Hacks (GameBoy Color)",
            },
            {
                "name": "3)Pokémon Hacks ---",
                "old_name": "PokemonHacks (GameBoy Color)",
            },
        ],
        "files_to_delete": [
            {
                "file": "0)More Games ---/10-Pin Bowling.zip",
                "reason": "duplicate, keeping rumble version",
                "crc32": "E061D283",
            },
            {
                "file": "0)More Games ---/Little Mermaid II, The - Pinball Frenzy.zip",
                "reason": "duplicate, keeping rumble version",
                "crc32": "75130CB7",
            },
            {
                "file": "0)More Games ---/Missile Command.zip",
                "reason": "duplicate, keeping rumble version",
                "crc32": "E383AC51",
            },
            {
                "file": "0)More Games ---/Ready 2 Rumble Boxing.zip",
                "reason": "duplicate, keeping rumble version",
                "crc32": "6ED05218",
            },
            {
                "file": "0)More Games ---/Tonka Raceway.zip",
                "reason": "duplicate, keeping rumble version",
                "crc32": "88DC4521",
            },
        ],
        "convert_7zips": True,
    },
    {
        "name": "Sega Game Gear (GG)",
        "old_name": "GG",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (Game Gear)",
            },
            {
                "name": "1)Translations ---",
                "old_name": "Translations (Game Gear)",
            },
            {
                "name": "2)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (Game Gear)",
            },
        ],
        "convert_7zips": True,
    },
    {
        "name": "Atari Lynx (LYNX)",
        "old_name": "LYNX",
    },
    {
        "name": "Sega Genesis (MD)",
        "old_name": "MD",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (Genesis)",
            },
            {
                "name": "1)Sega 32X ---",
                "old_name": "32X Games (Genesis)",
            },
            {
                "name": "2)Translations ---",
                "old_name": "Translations (Genesis)",
            },
            {
                "name": "3)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (Genesis)",
            },
            {
                "name": "4)Hacks ---",
                "old_name": "Hacks (Genesis)",
            },
        ],
        "files_to_delete": [
            {
                "file": "4)Hacks ---/OutRun 2019 (USA).zip",
                "reason": "duplicate, exists in More Games",
                "crc32": "2BE84C8E",
            },
            {
                "file": "4)Hacks ---/Ultimate Mortal Kombat Trilogy (Music Mod).zip",
                "reason": "sounds bad, regular version exists",
                "crc32": "AD0229E3",
            },
        ],
        "files_to_rename": [
            {
                "file": "0)More Games ---/Spider-Man (Sega).7z",
                "new_file": "0)More Games ---/Spider-Man vs. The Kingpin.7z",
                "reason": "less ambiguous",
                "crc32": "8EC5BEE0",
            },
        ],
        "convert_7zips": True,
    },
    {
        "name": "Sega Master System (SMS)",
        "old_name": "MS",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (Master System)",
            },
            {
                "name": "1)Translations ---",
                "old_name": "Translations (Master System)",
            },
            {
                "name": "2)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (Master System)",
            },
        ],
        "convert_7zips": True,
    },
    {
        "name": "TurboGrafx-16 (PCE)",
        "old_name": "PCE",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (TurboGrafx-16)",
            },
            {
                "name": "1)Translations ---",
                "old_name": "Translations (TurboGrafx-16)",
            },
            {
                "name": "2)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (TurboGrafx-16)",
            },
        ],
        "convert_7zips": True,
    },
    {
        "name": "PICO-8 (P8)",
        "old_name": "PICO",
        "subdirs_to_delete": [
            {
                "subdir": "POOM",
                "reason": "cluttery, can't get it to work",
            },
        ],
        "extensions_to_zip": [".p8.png"],
    },
    {
        "name": "Satellaview (SFC)",
        "old_name": "SATELLAVIEW",
    },
    {
        "name": "Atari 7800 (A7800)",
        "old_name": "SEVENTYEIGHTHUNDRED",
    },
    {
        "name": "Super Nintendo Entertainment System (SFC)",
        "old_name": "SFC",
        "subdirs": [
            {
                "name": "0)More Games ---",
                "old_name": "All but the Best (SNES)",
            },
            {
                "name": "1)Translations ---",
                "old_name": "Translations (SNES)",
            },
            {
                "name": "2)Unlicensed & Homebrews ---",
                "old_name": "Unlicensed Homebrew (SNES)",
            },
            {
                "name": "3)Hacks ---",
                "old_name": "Hacks (SNES)",
            },
        ],
        "subdirs_to_delete": [
            {
                "subdir": ".game_config",
                "reason": "clutter",
            },
            {
                "subdir": "3)Hacks ---/.game_config",
                "reason": "clutter",
            },
        ],
        "files_to_delete": [
            {
                "file": "1)Translations ---/Gunple - Gunman's Proof.zip",
                "reason": "duplicate, older version",
                "crc32": "B2A9B2BC",
            },
        ],
        "extensions_to_zip": [".sfc", ".smc"],
        "convert_7zips": True,
        "fix_mrdo": True,
    },
]
