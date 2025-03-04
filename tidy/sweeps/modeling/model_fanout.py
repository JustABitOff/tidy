from collections import Counter

from tidy.sweeps.base import sweep
from tidy.manifest.types import ManifestType


@sweep("Model Fanout")
def model_fanout(manifest: ManifestType) -> list:
    failures = []

    for key, value in manifest.child_map.items():
        if (
            key.startswith("model.")
            and Counter(s.startswith("model.") for s in value)[True] > 3
        ):
            failures.append(f"{key}")
    
    return failures
            