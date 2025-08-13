from datetime import datetime
# Alpha’s schema
ALPHA_EMPLOYEES = [
    {
        "id": "a_101",
        "first_name": "Alice",
        "last_name": "Nguyen",
        "mail": "alice@example.com",
        "employment": "FULL_TIME",
        "start_date": "2022-03-01",
        "dept": "Engineering",
        "manager_id": None,
        "updated_at": "2025-07-01T10:00:00Z"
    },
    {
        "id": "a_102",
        "first_name": "Ben",
        "last_name": "Singh",
        "mail": "ben@example.com",
        "employment": "CONTRACTOR",
        "start_date": "2024-11-15",
        "dept": "Data",
        "manager_id": "a_101",
        "updated_at": "2025-07-02T09:30:00Z"
    },
]
