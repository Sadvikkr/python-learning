from fastapi import APIRouter, Depends

from app.schemas.student import Student, StudentResponse

from app.dependencies import get_current_user

from app.services.student_service import (
    home,
    get_all_students,
    get_student_by_id,
    create_student,
    update_student,
    delete_student,
)

router = APIRouter()


@router.get("/")
def home_route():
    return home()

@router.get("/students", response_model=list[StudentResponse])
def get_students(
    user=Depends(get_current_user),
    age: int = None,
    name: str = None,
    marks: int = None,
    sort: str = None,
    search: str = None,
    page: int = 1,
    limit: int = 10,
):
    print(user)

    return get_all_students(
        age,
        name,
        marks,
        sort,
        search,
        page,
        limit,
    )


@router.get("/students/{id}")
def get_student(id: int):
    return get_student_by_id(id)

@router.post("/students")
def add_student(student: Student):
    return create_student(student)

@router.put("/students/{id}")
def edit_student(id: int, student: Student):
    return update_student(id, student)

@router.delete("/students/{id}")
def remove_student(id: int):
    return delete_student(id)
