import requests
import pytest

# 1. Создаем фикстуру. Декоратор @pytest.fixture говорит pytest, что это не просто функция, а подготовка данных.
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

# 2. В параметры теста мы добавляем имя фикстуры (base_url)
def test_get_post(base_url):
    # Теперь мы используем base_url вместо длинной строки
    response = requests.get(f"{base_url}/posts/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_post_not_found(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404

    # Параметризация: передаем список ID и список ожидаемых заголовков (или просто проверяем статус)
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_multiple_posts(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    
    assert response.status_code == 200
    data = response.json()
    
    # Проверяем, что сервер вернул именно тот ID, который мы запросили
    assert data["id"] == post_id
    print(f"\nУспешно проверен пост с ID: {post_id}")