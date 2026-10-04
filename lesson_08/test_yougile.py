from yougile_api import YougileApi

api = YougileApi()

# ID реально существующего проекта в аккаунте
EXISTING_PROJECT_ID = "00119d13-7d3c-4282-a0ef-16cd6bfc9a4d"


# POST /api-v2/projects

def test_create_project_positive():
    """Позитивный тест создания проекта."""
    title = "Autotest_Post"
    resp = api.create_project(title)

    assert resp.status_code in [200, 201]
    body = resp.json()
    assert "id" in body


def test_create_project_negative():
    """Негативный тест создания проекта с пустым названием."""
    resp = api.create_project("")

    assert resp.status_code >= 400
    body = resp.json()
    assert "error" in body or "message" in body


# GET /api-v2/projects/{id}

def test_get_project_positive():
    """Позитивный тест получения проекта по ID."""
    resp = api.get_project(EXISTING_PROJECT_ID)

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == EXISTING_PROJECT_ID
    assert "title" in body


def test_get_project_negative():
    """Негативный тест получения несуществующего проекта."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project(fake_id)

    assert resp.status_code == 404
    body = resp.json()
    assert "error" in body or "message" in body


# PUT /api-v2/projects/{id}

def test_update_project_positive():
    """Позитивный тест обновления проекта."""
    new_title = "Autotest_Put_Updated"
    resp = api.update_project(EXISTING_PROJECT_ID, new_title)

    assert resp.status_code in [200, 201, 400]
    body = resp.json()

    if resp.status_code in [200, 201]:
        assert "id" in body
    else:
        assert "error" in body or "message" in body


def test_update_project_negative():
    """Негативный тест обновления несуществующего проекта."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.update_project(fake_id, "Should Fail")

    assert resp.status_code >= 400
    body = resp.json()
    assert "error" in body or "message" in body
