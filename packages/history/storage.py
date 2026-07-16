import json
import os
from datetime import datetime

SNAPSHOT_FOLDER = "snapshots"


def save_snapshot(report):

    os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.json")

    filepath = os.path.join(
        SNAPSHOT_FOLDER,
        filename
    )

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=4
        )

    return filepath