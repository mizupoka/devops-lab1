from hello import get_hello_message

def test_get_hello_message():
    assert get_hello_message() == "Hello, CI/CD Pipeline!"
