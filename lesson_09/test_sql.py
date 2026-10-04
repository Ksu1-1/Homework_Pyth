from sqlalchemy import text
from lesson_09.db import db

TEST_USER_ID = 999991
TEST_LEVEL = "Beginner"
TEST_EDUCATION_FORM = "personal"
TEST_SUBJECT_ID = 1

SQL_INSERT_USER = text(
    "INSERT INTO users (user_id, user_email, subject_id) "
    "VALUES (:user_id, :email, :subject_id)"
)

SQL_INSERT_STUDENT = text(
    'INSERT INTO student (user_id, "level", education_form, subject_id) '
    "VALUES (:user_id, :level, :education_form, :subject_id)"
)

SQL_SELECT_STUDENT = text(
    'SELECT "level", education_form, subject_id '
    "FROM student WHERE user_id = :id"
)

SQL_SELECT_STUDENT_LEVEL = text(
    'SELECT "level", education_form FROM student WHERE user_id = :id'
)

SQL_UPDATE_STUDENT = text(
    'UPDATE student SET "level" = :level, '
    "education_form = :education_form "
    "WHERE user_id = :id"
)

SQL_SELECT_STUDENT_ID = text(
    "SELECT user_id FROM student WHERE user_id = :id"
)

SQL_DELETE_STUDENT = text(
    "DELETE FROM student WHERE user_id = :id"
)

SQL_DELETE_USER = text(
    "DELETE FROM users WHERE user_id = :id"
)


def test_add_student():
    db.execute(SQL_INSERT_USER, {
        "user_id": TEST_USER_ID,
        "email": "student_test@example.com",
        "subject_id": TEST_SUBJECT_ID,
    })
    db.execute(SQL_INSERT_STUDENT, {
        "user_id": TEST_USER_ID,
        "level": TEST_LEVEL,
        "education_form": TEST_EDUCATION_FORM,
        "subject_id": TEST_SUBJECT_ID,
    })

    row = db.execute(SQL_SELECT_STUDENT, {"id": TEST_USER_ID}).fetchone()

    assert row is not None, "Студент не был добавлен"
    assert row.level == TEST_LEVEL
    assert row.education_form == TEST_EDUCATION_FORM
    assert row.subject_id == TEST_SUBJECT_ID

    db.execute(SQL_DELETE_STUDENT, {"id": TEST_USER_ID})
    db.execute(SQL_DELETE_USER, {"id": TEST_USER_ID})


def test_update_student():
    NEW_LEVEL = "Advanced"
    NEW_EDUCATION_FORM = "group"

    db.execute(SQL_INSERT_USER, {
        "user_id": TEST_USER_ID,
        "email": "student_test@example.com",
        "subject_id": TEST_SUBJECT_ID,
    })
    db.execute(SQL_INSERT_STUDENT, {
        "user_id": TEST_USER_ID,
        "level": TEST_LEVEL,
        "education_form": TEST_EDUCATION_FORM,
        "subject_id": TEST_SUBJECT_ID,
    })

    db.execute(SQL_UPDATE_STUDENT, {
        "id": TEST_USER_ID,
        "level": NEW_LEVEL,
        "education_form": NEW_EDUCATION_FORM,
    })

    row = db.execute(
        SQL_SELECT_STUDENT_LEVEL, {"id": TEST_USER_ID}
    ).fetchone()

    assert row is not None, "Студент не найден после обновления"
    assert row.level == NEW_LEVEL
    assert row.education_form == NEW_EDUCATION_FORM

    db.execute(SQL_DELETE_STUDENT, {"id": TEST_USER_ID})
    db.execute(SQL_DELETE_USER, {"id": TEST_USER_ID})


def test_delete_student():
    db.execute(SQL_INSERT_USER, {
        "user_id": TEST_USER_ID,
        "email": "student_test@example.com",
        "subject_id": TEST_SUBJECT_ID,
    })
    db.execute(SQL_INSERT_STUDENT, {
        "user_id": TEST_USER_ID,
        "level": TEST_LEVEL,
        "education_form": TEST_EDUCATION_FORM,
        "subject_id": TEST_SUBJECT_ID,
    })

    created = db.execute(
        SQL_SELECT_STUDENT_ID, {"id": TEST_USER_ID}
    ).fetchone()
    assert created is not None, "Студент не был создан перед удалением"

    db.execute(SQL_DELETE_STUDENT, {"id": TEST_USER_ID})

    gone = db.execute(
        SQL_SELECT_STUDENT_ID, {"id": TEST_USER_ID}
    ).fetchone()
    assert gone is None, "Студент всё ещё присутствует после удаления"

    db.execute(SQL_DELETE_USER, {"id": TEST_USER_ID})
