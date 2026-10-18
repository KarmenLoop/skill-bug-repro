"""Turn scattered bug observations into a reproducible investigation."""
from runtime import *

def process(data):
    summary=text(data["summary"],"summary")
    expected=text(data["expected"],"expected")
    steps=strings(data["steps"],"steps")
    if not steps: raise ValueError("provide at least one reproduction step")
    env=data["environment"]
    if not isinstance(env,dict): raise ValueError("environment must be an object")
    attempts=records(data,"attempts")
    unique(attempts)
    count=0
    for row in attempts:
        if type(row.get("reproduced")) is not bool: raise ValueError("reproduced must be boolean")
        text(row.get("actual"),"actual")
        text(row.get("evidence"),"evidence")
        count+=row["reproduced"]
    classification="not_run" if not attempts else "consistent_failure" if count==len(attempts) else "intermittent" if count else "not_reproduced"
    return {"summary":summary,"expected":expected,"steps":steps,"environment":env,"missing_environment":[k for k in ("os","runtime","version") if not env.get(k)],"attempts":attempts,"reproduced_count":count,"reproduction_rate":count/len(attempts) if attempts else None,"classification":classification}

if __name__ == "__main__":
    sys.exit(main(process, "Turn scattered bug observations into a reproducible investigation."))
