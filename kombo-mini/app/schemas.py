from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

class Employee(BaseModel):
    id: str                 # stable unified id
    firstName: str
    lastName: str
    email: EmailStr
    employmentType: str     # full_time | part_time | contractor | intern | temp
    startDate: date
    department: Optional[str] = None
    managerId: Optional[str] = None
    lastSyncedAt: datetime
    provider: str           # which provider this record came from
