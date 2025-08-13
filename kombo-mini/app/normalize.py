from datetime import datetime, date
from typing import Dict, List
from .schemas import Employee
from .providers.alpha import ALPHA_EMPLOYEES
from .providers.beta import BETA_EMPLOYEES

# Enum harmonization
def normalize_employment(value: str) -> str:
    v = value.strip().lower()
    if v in ["full_time", "full-time", "full time", "fulltime", "full", "full_time".lower(), "full_time".lower()]:
        return "full_time"
    if v in ["part_time", "part-time", "part time", "parttime"]:
        return "part_time"
    if v in ["contractor", "contract", "vendor"]:
        return "contractor"
    if v in ["intern", "internship"]:
        return "intern"
    if v in ["temp", "temporary"]:
        return "temp"
    # fallback
    return "contractor" if "contract" in v else v

def parse_date(s: str) -> date:
    return date.fromisoformat(s)

def parse_dt(s: str) -> datetime:
    # Accepts '...Z' by replacing with +00:00
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def alpha_to_employee(row: Dict) -> Employee:
    return Employee(
        id=f"alpha:{row['id']}",
        firstName=row["first_name"],
        lastName=row["last_name"],
        email=row["mail"],
        employmentType=normalize_employment(row["employment"]),
        startDate=parse_date(row["start_date"]),
        department=row.get("dept"),
        managerId=(f"alpha:{row['manager_id']}" if row.get("manager_id") else None),
        lastSyncedAt=parse_dt(row["updated_at"]),
        provider="alpha",
    )

def beta_to_employee(row: Dict) -> Employee:
    return Employee(
        id=f"beta:{row['uuid']}",
        firstName=row["given_name"],
        lastName=row["surname"],
        email=row["emailAddress"],
        employmentType=normalize_employment(row["employmentType"]),
        startDate=parse_date(row["start"]),
        department=row.get("org"),
        managerId=(f"beta:{row['reportsTo']}" if row.get("reportsTo") else None),
        lastSyncedAt=parse_dt(row["lastModified"]),
        provider="beta",
    )

def fetch_all_employees(providers: List[str]) -> List[Employee]:
    out: List[Employee] = []
    if "alpha" in providers:
        out += [alpha_to_employee(r) for r in ALPHA_EMPLOYEES]
    if "beta" in providers:
        out += [beta_to_employee(r) for r in BETA_EMPLOYEES]
    return out
