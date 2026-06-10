import os
import shutil
import json

# last config
with open("fileserver.config") as f:
    config = json.load(f)

# eksempel: mapping fra rot → mappe
# du kan justere dette etter hvordan filene dine faktisk ligger nå
rules = {
    "forms": ".xml",
    "form_scripts": ".js",
    "opts": ".opt",
    "data": ".json",
    "vaqms": ".vaqm",
    "archetypes": ".adl",
    "templates": ".t.json",
    "queries": ".aql"
}

for key, extension in rules.items():
    target_dir = config.get(key)

    if not target_dir:
        continue

    os.makedirs(target_dir, exist_ok=True)

    for file in os.listdir("."):
        if file.endswith(extension):
            src = file
            dst = os.path.join(target_dir, file)

            print(f"Flytter {src} → {dst}")
            shutil.move(src, dst)
``