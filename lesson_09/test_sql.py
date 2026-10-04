from sqlalchemy import text
from lesson_09.db import db

TEST_USER_ID = 999991


def test_add_user():
    db.execute(
        text(
            "INSERT INTO users (user_id, user_email, subject_id) "
            "VALUES (:user_id, :email, :subject_id)"
        ),
        {
            "user_id": TEST_USER_ID,
            "email": "test_add@example.com",
            "subject_id": 1,
        },
    )

    row = db.execute(
        text("SELECT user_email FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    ).fetchone()

    assert row is not None, "Пользователь не был добавлен"
    assert row.user_email == "test_add@example.com"


    db.execute(
        text("DELETE FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    )


def test_update_user():
    db.execute(
        text(
            "INSERT INTO users (user_id, user_email, subject_id) "
            "VALUES (:id, :email, :subject_id)"
        ),
        {
            "id": TEST_USER_ID,
            "email": "old@example.com",
            "subject_id": 1,
        },
    )

    db.execute(
        text(
            "UPDATE users SET user_email = :email, "
            "subject_id = :subject_id WHERE user_id = :id"
        ),
        {
            "id": TEST_USER_ID,
            "email": "new@example.com",
            "subject_id": 2,
        },
    )

    row = db.execute(
        text("SELECT user_email, subject_id FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    ).fetchone()

    assert row is not None, "Пользователь не найден после обновления"
    assert row.user_email == "new@example.com"
    assert row.subject_id == 2

    db.execute(
        text("DELETE FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    )


def test_delete_user():
    db.execute(
        text(
            "INSERT INTO users (user_id, user_email, subject_id) "
            "VALUES (:id, :email, :subject_id)"
        ),
        {
            "id": TEST_USER_ID,
            "email": "delete_me@example.com",
            "subject_id": 1,
        },
    )

    # Убеждаемся, что создан
    created = db.execute(
        text("SELECT user_id FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    ).fetchone()
    assert created is not None, "Пользователь не был создан перед удалением"

    # Удаляем
    db.execute(
        text("DELETE FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    )

    gone = db.execute(
        text("SELECT user_id FROM users WHERE user_id = :id"),
        {"id": TEST_USER_ID},
    ).fetchone()
    assert gone is None, "Пользователь всё ещё присутствует после удаления"

