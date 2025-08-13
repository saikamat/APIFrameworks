from fastapi import FastAPI, Query, HTTPException
from typing import List, Literal, Optional
from .schemas import Employee
from .normalize import fetch_all_employees

app = FastAPI(title="Kombo Mini Unified API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/employees", response_model=List[Employee])
def list_employees(
    providers: Optional[List[Literal["alpha", "beta"]]] = Query(default=None),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    employmentType: Optional[str] = None,
):
    active = providers or ["alpha", "beta"]
    employees = fetch_all_employees(active)

    if employmentType:
        et = employmentType.strip().lower()
        employees = [e for e in employees if e.employmentType == et]

    # sort by startDate desc for a stable default
    employees.sort(key=lambda e: e.startDate, reverse=True)
    return employees[offset: offset + limit]

@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: str):
    employees = fetch_all_employees(["alpha", "beta"])
    for e in employees:
        if e.id == employee_id:
            return e
    raise HTTPException(status_code=404, detail="Employee not found")
